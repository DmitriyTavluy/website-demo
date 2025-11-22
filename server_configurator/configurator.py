"""
Main server configurator class
Handles configuration logic and validation
"""

from typing import Dict, List, Optional, Tuple
from data_models import (
    Component, ComponentType, ServerConfiguration, 
    ServerConfiguratorData, CompatibilityRule
)
from sample_data import create_sample_data, create_compatibility_matrix


class ServerConfigurator:
    """Main configurator class"""
    
    def __init__(self):
        self.data = create_sample_data()
        self.compatibility_matrix = create_compatibility_matrix()
        self.current_configuration: Dict[ComponentType, List[Component]] = {}
        self.configuration_id = 1
        
    def add_component(self, component_id: str) -> Tuple[bool, List[str]]:
        """
        Add component to current configuration
        Returns (success, error_messages)
        """
        if component_id not in self.data.components:
            return False, [f"Component {component_id} not found"]
        
        component = self.data.components[component_id]
        component_type = component.component_type
        
        # Initialize component type list if not exists
        if component_type not in self.current_configuration:
            self.current_configuration[component_type] = []
        
        # Check if component is already added
        if component in self.current_configuration[component_type]:
            return False, [f"Component {component.name} is already in configuration"]
        
        # Check compatibility with existing components
        compatibility_errors = self._check_compatibility(component)
        if compatibility_errors:
            return False, compatibility_errors
        
        # Add component
        self.current_configuration[component_type].append(component)
        
        return True, []
    
    def remove_component(self, component_id: str) -> bool:
        """Remove component from current configuration"""
        for component_type, components in self.current_configuration.items():
            for component in components:
                if component.id == component_id:
                    components.remove(component)
                    return True
        return False
    
    def get_available_components(self, component_type: ComponentType) -> List[Component]:
        """Get components available for selection based on current configuration"""
        all_components = self.data.get_components_by_type(component_type)
        available = []
        
        for component in all_components:
            # Check if component is compatible with current configuration
            errors = self._check_compatibility(component)
            if not errors:
                available.append(component)
        
        return available
    
    def _check_compatibility(self, new_component: Component) -> List[str]:
        """Check if new component is compatible with current configuration"""
        errors = []
        
        # Check against compatibility matrix
        if new_component.id in self.compatibility_matrix:
            compatible_with = self.compatibility_matrix[new_component.id]
            
            # Check if any existing component is incompatible
            for component_type, components in self.current_configuration.items():
                for existing_component in components:
                    if existing_component.id not in compatible_with:
                        errors.append(
                            f"{new_component.name} is not compatible with {existing_component.name}"
                        )
        
        # Also check reverse compatibility - if existing components are compatible with new component
        for component_type, components in self.current_configuration.items():
            for existing_component in components:
                if existing_component.id in self.compatibility_matrix:
                    compatible_with = self.compatibility_matrix[existing_component.id]
                    if new_component.id not in compatible_with:
                        errors.append(
                            f"{existing_component.name} is not compatible with {new_component.name}"
                        )
        
        # Check compatibility rules
        rule_errors = self._check_compatibility_rules(new_component)
        errors.extend(rule_errors)
        
        return errors
    
    def _check_compatibility_rules(self, new_component: Component) -> List[str]:
        """Check compatibility rules for new component"""
        errors = []
        
        # Create temporary configuration with new component
        temp_config = {}
        for comp_type, components in self.current_configuration.items():
            temp_config[comp_type] = components.copy()
        
        if new_component.component_type not in temp_config:
            temp_config[new_component.component_type] = []
        temp_config[new_component.component_type].append(new_component)
        
        # Validate against rules
        rule_errors = self.data.validate_configuration(temp_config)
        errors.extend(rule_errors)
        
        return errors
    
    def get_current_configuration(self) -> ServerConfiguration:
        """Get current configuration with validation"""
        total_price = self._calculate_total_price()
        validation_errors = self._validate_current_configuration()
        is_valid = len(validation_errors) == 0
        
        return ServerConfiguration(
            id=f"config_{self.configuration_id}",
            name=f"Configuration {self.configuration_id}",
            components=self.current_configuration.copy(),
            total_price=total_price,
            is_valid=is_valid,
            validation_errors=validation_errors
        )
    
    def _calculate_total_price(self) -> float:
        """Calculate total price of current configuration"""
        total = 0.0
        for components in self.current_configuration.values():
            for component in components:
                if component.price:
                    total += component.price
        return total
    
    def _validate_current_configuration(self) -> List[str]:
        """Validate current configuration"""
        return self.data.validate_configuration(self.current_configuration)
    
    def clear_configuration(self) -> None:
        """Clear current configuration"""
        self.current_configuration = {}
        self.configuration_id += 1
    
    def get_component_details(self, component_id: str) -> Optional[Component]:
        """Get detailed information about a component"""
        return self.data.components.get(component_id)
    
    def search_components(self, query: str, component_type: Optional[ComponentType] = None) -> List[Component]:
        """Search components by name, manufacturer, or model"""
        results = []
        query_lower = query.lower()
        
        for component in self.data.components.values():
            if component_type and component.component_type != component_type:
                continue
                
            if (query_lower in component.name.lower() or 
                query_lower in component.manufacturer.lower() or 
                query_lower in component.model.lower()):
                results.append(component)
        
        return results
    
    def get_compatibility_info(self, component_id: str) -> Dict:
        """Get compatibility information for a component"""
        if component_id not in self.compatibility_matrix:
            return {"compatible_with": [], "incompatible_with": []}
        
        compatible_with = self.compatibility_matrix[component_id]
        incompatible_with = []
        
        # Find incompatible components
        for other_id, other_compatible in self.compatibility_matrix.items():
            if other_id != component_id and component_id not in other_compatible:
                incompatible_with.append(other_id)
        
        return {
            "compatible_with": compatible_with,
            "incompatible_with": incompatible_with
        }
    
    def export_configuration(self, format_type: str = "json") -> str:
        """Export current configuration in specified format"""
        config = self.get_current_configuration()
        
        if format_type == "json":
            import json
            return json.dumps({
                "id": config.id,
                "name": config.name,
                "total_price": config.total_price,
                "is_valid": config.is_valid,
                "validation_errors": config.validation_errors,
                "components": {
                    comp_type.value: [
                        {
                            "id": comp.id,
                            "name": comp.name,
                            "manufacturer": comp.manufacturer,
                            "model": comp.model,
                            "price": comp.price,
                            "attributes": [
                                {
                                    "name": attr.name,
                                    "value": attr.value,
                                    "unit": attr.unit
                                } for attr in comp.attributes
                            ]
                        } for comp in components
                    ] for comp_type, components in config.components.items()
                }
            }, indent=2)
        
        elif format_type == "csv":
            import csv
            import io
            
            output = io.StringIO()
            writer = csv.writer(output)
            
            # Write header
            writer.writerow(["Component Type", "Name", "Manufacturer", "Model", "Price"])
            
            # Write components
            for comp_type, components in config.components.items():
                for comp in components:
                    writer.writerow([
                        comp_type.value,
                        comp.name,
                        comp.manufacturer,
                        comp.model,
                        comp.price or 0
                    ])
            
            return output.getvalue()
        
        else:
            raise ValueError(f"Unsupported format: {format_type}")
