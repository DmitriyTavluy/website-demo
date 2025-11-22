"""
Data models for server configurator
Defines the structure for categories, components, and compatibility
"""

from dataclasses import dataclass
from typing import List, Dict, Optional, Set
from enum import Enum


class ComponentType(Enum):
    """Main component categories"""
    SERVER = "server"
    PROCESSOR = "processor"
    MEMORY = "memory"
    SSD = "ssd"  # Solid State Drives (SATA)
    NVME = "nvme"  # NVMe drives
    HDD_SAS_SATA = "hdd_sas_sata"  # SAS/SATA HDD
    HDD_U320 = "hdd_u320"  # U320 SCSI (legacy)
    CONTROLLER = "controller"
    NETWORK = "network"
    POWER_SUPPLY = "power_supply"
    COOLING = "cooling"
    CHASSIS = "chassis"


class CompatibilityType(Enum):
    """Types of compatibility rules"""
    REQUIRED = "required"  # Component must be present
    EXCLUDED = "excluded"  # Component cannot be used together
    LIMITED = "limited"    # Limited quantity or specific models only
    OPTIONAL = "optional"  # Can be added but not required


@dataclass
class ComponentAttribute:
    """Individual attribute of a component"""
    name: str
    value: str
    unit: Optional[str] = None
    is_required: bool = True


@dataclass
class Component:
    """Individual server component"""
    id: str
    name: str
    component_type: ComponentType
    manufacturer: str
    model: str
    attributes: List[ComponentAttribute]
    price: Optional[float] = None
    availability: bool = True
    description: Optional[str] = None


@dataclass
class CompatibilityRule:
    """Rule defining compatibility between components"""
    id: str
    rule_type: CompatibilityType
    primary_component_id: str
    secondary_component_id: Optional[str] = None
    condition: Optional[str] = None  # Additional conditions
    max_quantity: Optional[int] = None
    min_quantity: Optional[int] = None


@dataclass
class ServerConfiguration:
    """Complete server configuration"""
    id: str
    name: str
    components: Dict[ComponentType, List[Component]]
    total_price: float
    is_valid: bool
    validation_errors: List[str]


class ServerConfiguratorData:
    """Main data structure for the configurator"""
    
    def __init__(self):
        self.components: Dict[str, Component] = {}
        self.compatibility_rules: List[CompatibilityRule] = []
        self.categories: Dict[ComponentType, List[str]] = {}
        
    def add_component(self, component: Component) -> None:
        """Add component to the database"""
        self.components[component.id] = component
        
        # Update categories
        if component.component_type not in self.categories:
            self.categories[component.component_type] = []
        self.categories[component.component_type].append(component.id)
    
    def add_compatibility_rule(self, rule: CompatibilityRule) -> None:
        """Add compatibility rule"""
        self.compatibility_rules.append(rule)
    
    def get_components_by_type(self, component_type: ComponentType) -> List[Component]:
        """Get all components of specific type"""
        component_ids = self.categories.get(component_type, [])
        return [self.components[cid] for cid in component_ids if cid in self.components]
    
    def validate_configuration(self, components: Dict[ComponentType, List[Component]]) -> List[str]:
        """Validate configuration against compatibility rules"""
        errors = []
        
        for rule in self.compatibility_rules:
            if rule.rule_type == CompatibilityType.REQUIRED:
                # Check if required component is present
                # Find the component type for the required component
                required_component = self.components.get(rule.primary_component_id)
                if required_component:
                    component_type = required_component.component_type
                    if rule.primary_component_id not in [c.id for c in components.get(component_type, [])]:
                        errors.append(f"Required component {rule.primary_component_id} is missing")
            
            elif rule.rule_type == CompatibilityType.EXCLUDED:
                # Check if excluded components are used together
                primary_component = self.components.get(rule.primary_component_id)
                secondary_component = self.components.get(rule.secondary_component_id) if rule.secondary_component_id else None
                
                if primary_component and secondary_component:
                    primary_present = any(c.id == rule.primary_component_id 
                                        for c in components.get(primary_component.component_type, []))
                    secondary_present = any(c.id == rule.secondary_component_id 
                                          for c in components.get(secondary_component.component_type, []))
                    
                    if primary_present and secondary_present:
                        errors.append(f"Components {rule.primary_component_id} and {rule.secondary_component_id} are incompatible")
            
            elif rule.rule_type == CompatibilityType.LIMITED:
                # Check quantity limits
                primary_component = self.components.get(rule.primary_component_id)
                if primary_component:
                    component_count = len([c for c in components.get(primary_component.component_type, []) 
                                         if c.id == rule.primary_component_id])
                    
                    if rule.max_quantity and component_count > rule.max_quantity:
                        errors.append(f"Too many {rule.primary_component_id} components (max: {rule.max_quantity})")
                    
                    if rule.min_quantity and component_count < rule.min_quantity:
                        errors.append(f"Not enough {rule.primary_component_id} components (min: {rule.min_quantity})")
        
        return errors
