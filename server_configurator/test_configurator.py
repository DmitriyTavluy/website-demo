"""
Tests for server configurator
"""

import pytest
from configurator import ServerConfigurator
from data_models import ComponentType


class TestServerConfigurator:
    """Test cases for ServerConfigurator"""
    
    def setup_method(self):
        """Setup test environment"""
        self.configurator = ServerConfigurator()
    
    def test_add_compatible_components(self):
        """Test adding compatible components"""
        # Add HP server
        success, errors = self.configurator.add_component("hp_ml350g4p")
        assert success
        assert len(errors) == 0
        
        # Add compatible processor
        success, errors = self.configurator.add_component("intel_xeon_3_0_604")
        assert success
        assert len(errors) == 0
        
        # Add compatible memory
        success, errors = self.configurator.add_component("kingston_1gb_ddr2_400")
        assert success
        assert len(errors) == 0
    
    def test_add_incompatible_components(self):
        """Test adding incompatible components"""
        # Add HP server
        self.configurator.add_component("hp_ml350g4p")
        
        # Try to add incompatible processor (wrong socket)
        success, errors = self.configurator.add_component("intel_xeon_e5620")
        assert not success
        assert len(errors) > 0
        assert "not compatible" in errors[0].lower()
    
    def test_memory_type_compatibility(self):
        """Test memory type compatibility"""
        # Add HP server
        self.configurator.add_component("hp_ml350g4p")
        
        # Add DDR2 memory
        success, errors = self.configurator.add_component("kingston_1gb_ddr2_400")
        assert success
        
        # Try to add DDR3 memory (incompatible)
        success, errors = self.configurator.add_component("samsung_4gb_ddr3_1333")
        assert not success
        assert len(errors) > 0
    
    def test_quantity_limits(self):
        """Test quantity limits"""
        # Add HP server
        self.configurator.add_component("hp_ml350g4p")
        
        # Add first processor
        success, errors = self.configurator.add_component("intel_xeon_3_0_604")
        assert success
        
        # Add second processor
        success, errors = self.configurator.add_component("intel_xeon_3_2_604")
        assert success
        
        # Try to add third processor (should fail due to limit)
        success, errors = self.configurator.add_component("intel_xeon_3_0_604")
        assert not success
        assert "already in configuration" in errors[0].lower()
    
    def test_remove_component(self):
        """Test removing components"""
        # Add components
        self.configurator.add_component("hp_ml350g4p")
        self.configurator.add_component("intel_xeon_3_0_604")
        
        # Remove component
        success = self.configurator.remove_component("intel_xeon_3_0_604")
        assert success
        
        # Try to remove non-existent component
        success = self.configurator.remove_component("non_existent")
        assert not success
    
    def test_get_available_components(self):
        """Test getting available components"""
        # Add HP server
        self.configurator.add_component("hp_ml350g4p")
        
        # Get available processors
        available_processors = self.configurator.get_available_components(ComponentType.PROCESSOR)
        processor_ids = [p.id for p in available_processors]
        
        # Should include compatible processors
        assert "intel_xeon_3_0_604" in processor_ids
        assert "intel_xeon_3_2_604" in processor_ids
        
        # Should not include incompatible processors
        assert "intel_xeon_e5620" not in processor_ids
    
    def test_configuration_validation(self):
        """Test configuration validation"""
        # Add valid configuration
        self.configurator.add_component("hp_ml350g4p")
        self.configurator.add_component("intel_xeon_3_0_604")
        self.configurator.add_component("kingston_1gb_ddr2_400")
        self.configurator.add_component("hp_460w_psu")
        
        config = self.configurator.get_current_configuration()
        assert config.is_valid
        assert len(config.validation_errors) == 0
        assert config.total_price > 0
    
    def test_search_components(self):
        """Test component search"""
        # Search by manufacturer
        results = self.configurator.search_components("Intel")
        assert len(results) > 0
        assert all("Intel" in comp.manufacturer for comp in results)
        
        # Search by model
        results = self.configurator.search_components("ML350")
        assert len(results) > 0
        assert any("ML350" in comp.model for comp in results)
        
        # Search by component type
        results = self.configurator.search_components("Xeon", ComponentType.PROCESSOR)
        assert len(results) > 0
        assert all(comp.component_type == ComponentType.PROCESSOR for comp in results)
    
    def test_clear_configuration(self):
        """Test clearing configuration"""
        # Add components
        self.configurator.add_component("hp_ml350g4p")
        self.configurator.add_component("intel_xeon_3_0_604")
        
        # Clear configuration
        self.configurator.clear_configuration()
        
        # Check that configuration is empty
        config = self.configurator.get_current_configuration()
        assert len(config.components) == 0
        assert config.total_price == 0.0
    
    def test_export_configuration(self):
        """Test configuration export"""
        # Add components
        self.configurator.add_component("hp_ml350g4p")
        self.configurator.add_component("intel_xeon_3_0_604")
        
        # Export as JSON
        json_export = self.configurator.export_configuration("json")
        assert "hp_ml350g4p" in json_export
        assert "intel_xeon_3_0_604" in json_export
        
        # Export as CSV
        csv_export = self.configurator.export_configuration("csv")
        assert "HP ProLiant ML350 G4p" in csv_export
        assert "Intel Xeon 3.0GHz" in csv_export
    
    def test_compatibility_info(self):
        """Test compatibility information"""
        compat_info = self.configurator.get_compatibility_info("hp_ml350g4p")
        
        assert "compatible_with" in compat_info
        assert "incompatible_with" in compat_info
        assert "intel_xeon_3_0_604" in compat_info["compatible_with"]
        assert "intel_xeon_e5620" in compat_info["incompatible_with"]


def test_sample_data_creation():
    """Test sample data creation"""
    from sample_data import create_sample_data, create_compatibility_matrix
    
    # Test data creation
    data = create_sample_data()
    assert len(data.components) > 0
    assert len(data.compatibility_rules) > 0
    
    # Test compatibility matrix
    matrix = create_compatibility_matrix()
    assert len(matrix) > 0
    assert "hp_ml350g4p" in matrix


if __name__ == "__main__":
    pytest.main([__file__])
