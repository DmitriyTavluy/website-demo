"""
Sample data for server configurator
Contains example components and compatibility rules
"""

from data_models import (
    Component, ComponentType, ComponentAttribute, 
    CompatibilityRule, CompatibilityType, ServerConfiguratorData
)


def create_sample_data() -> ServerConfiguratorData:
    """Create sample data for testing the configurator"""
    
    data = ServerConfiguratorData()
    
    # ADD SERVERS
    servers = [
        Component(
            id="hp_ml350g4p",
            name="HP ProLiant ML350 G4p",
            component_type=ComponentType.SERVER,
            manufacturer="HP",
            model="ML350 G4p",
            attributes=[
                ComponentAttribute("form_factor", "4U Rack"),
                ComponentAttribute("max_processors", "2"),
                ComponentAttribute("max_memory_slots", "8"),
                ComponentAttribute("max_memory_gb", "32"),
                ComponentAttribute("storage_bays", "6"),
                ComponentAttribute("power_supply_slots", "2"),
                ComponentAttribute("socket_type", "Socket 604"),
                ComponentAttribute("chipset", "Intel E7520")
            ],
            price=1500.00,
            description="Entry-level rack server with dual processor support"
        ),
        Component(
            id="dell_poweredge_r710",
            name="Dell PowerEdge R710",
            component_type=ComponentType.SERVER,
            manufacturer="Dell",
            model="R710",
            attributes=[
                ComponentAttribute("form_factor", "2U Rack"),
                ComponentAttribute("max_processors", "2"),
                ComponentAttribute("max_memory_slots", "18"),
                ComponentAttribute("max_memory_gb", "144"),
                ComponentAttribute("storage_bays", "6"),
                ComponentAttribute("power_supply_slots", "2"),
                ComponentAttribute("socket_type", "Socket 1366"),
                ComponentAttribute("chipset", "Intel 5520")
            ],
            price=2000.00,
            description="Mid-range rack server with high memory capacity"
        )
    ]
    
    # ADD PROCESSORS
    processors = [
        Component(
            id="intel_xeon_3_0_604",
            name="Intel Xeon 3.0GHz",
            component_type=ComponentType.PROCESSOR,
            manufacturer="Intel",
            model="Xeon 3.0GHz",
            attributes=[
                ComponentAttribute("frequency", "3.0", "GHz"),
                ComponentAttribute("cores", "1"),
                ComponentAttribute("socket", "604"),
                ComponentAttribute("cache", "1", "MB"),
                ComponentAttribute("tdp", "89", "W")
            ],
            price=150.00
        ),
        Component(
            id="intel_xeon_3_2_604",
            name="Intel Xeon 3.2GHz",
            component_type=ComponentType.PROCESSOR,
            manufacturer="Intel",
            model="Xeon 3.2GHz",
            attributes=[
                ComponentAttribute("frequency", "3.2", "GHz"),
                ComponentAttribute("cores", "1"),
                ComponentAttribute("socket", "604"),
                ComponentAttribute("cache", "1", "MB"),
                ComponentAttribute("tdp", "103", "W")
            ],
            price=200.00
        ),
        Component(
            id="intel_xeon_e5620",
            name="Intel Xeon E5620",
            component_type=ComponentType.PROCESSOR,
            manufacturer="Intel",
            model="E5620",
            attributes=[
                ComponentAttribute("frequency", "2.4", "GHz"),
                ComponentAttribute("cores", "4"),
                ComponentAttribute("socket", "1366"),
                ComponentAttribute("cache", "12", "MB"),
                ComponentAttribute("tdp", "80", "W")
            ],
            price=300.00
        )
    ]
    
    # ADD MEMORY
    memory_modules = [
        Component(
            id="kingston_1gb_ddr2_400",
            name="Kingston 1GB DDR2-400",
            component_type=ComponentType.MEMORY,
            manufacturer="Kingston",
            model="1GB DDR2-400",
            attributes=[
                ComponentAttribute("capacity", "1", "GB"),
                ComponentAttribute("type", "DDR2"),
                ComponentAttribute("speed", "400", "MHz"),
                ComponentAttribute("form_factor", "DIMM"),
                ComponentAttribute("voltage", "1.8", "V")
            ],
            price=25.00
        ),
        Component(
            id="corsair_2gb_ddr2_533",
            name="Corsair 2GB DDR2-533",
            component_type=ComponentType.MEMORY,
            manufacturer="Corsair",
            model="2GB DDR2-533",
            attributes=[
                ComponentAttribute("capacity", "2", "GB"),
                ComponentAttribute("type", "DDR2"),
                ComponentAttribute("speed", "533", "MHz"),
                ComponentAttribute("form_factor", "DIMM"),
                ComponentAttribute("voltage", "1.8", "V")
            ],
            price=45.00
        ),
        Component(
            id="samsung_4gb_ddr3_1333",
            name="Samsung 4GB DDR3-1333",
            component_type=ComponentType.MEMORY,
            manufacturer="Samsung",
            model="4GB DDR3-1333",
            attributes=[
                ComponentAttribute("capacity", "4", "GB"),
                ComponentAttribute("type", "DDR3"),
                ComponentAttribute("speed", "1333", "MHz"),
                ComponentAttribute("form_factor", "DIMM"),
                ComponentAttribute("voltage", "1.5", "V")
            ],
            price=80.00
        )
    ]
    
    # ADD STORAGE
    storage_devices = [
        Component(
            id="seagate_500gb_sata",
            name="Seagate 500GB SATA",
            component_type=ComponentType.STORAGE,
            manufacturer="Seagate",
            model="500GB SATA",
            attributes=[
                ComponentAttribute("capacity", "500", "GB"),
                ComponentAttribute("interface", "SATA"),
                ComponentAttribute("speed", "7200", "RPM"),
                ComponentAttribute("form_factor", "3.5"),
                ComponentAttribute("cache", "16", "MB")
            ],
            price=60.00
        ),
        Component(
            id="wd_1tb_sata",
            name="Western Digital 1TB SATA",
            component_type=ComponentType.STORAGE,
            manufacturer="Western Digital",
            model="1TB SATA",
            attributes=[
                ComponentAttribute("capacity", "1", "TB"),
                ComponentAttribute("interface", "SATA"),
                ComponentAttribute("speed", "7200", "RPM"),
                ComponentAttribute("form_factor", "3.5"),
                ComponentAttribute("cache", "64", "MB")
            ],
            price=100.00
        )
    ]
    
    # ADD POWER SUPPLIES
    power_supplies = [
        Component(
            id="hp_460w_psu",
            name="HP 460W Power Supply",
            component_type=ComponentType.POWER_SUPPLY,
            manufacturer="HP",
            model="460W PSU",
            attributes=[
                ComponentAttribute("power", "460", "W"),
                ComponentAttribute("efficiency", "80+"),
                ComponentAttribute("form_factor", "Standard"),
                ComponentAttribute("modular", "No")
            ],
            price=120.00
        ),
        Component(
            id="dell_750w_psu",
            name="Dell 750W Power Supply",
            component_type=ComponentType.POWER_SUPPLY,
            manufacturer="Dell",
            model="750W PSU",
            attributes=[
                ComponentAttribute("power", "750", "W"),
                ComponentAttribute("efficiency", "80+ Gold"),
                ComponentAttribute("form_factor", "Standard"),
                ComponentAttribute("modular", "No")
            ],
            price=180.00
        )
    ]
    
    # ADD ALL COMPONENTS TO DATA
    all_components = servers + processors + memory_modules + storage_devices + power_supplies
    for component in all_components:
        data.add_component(component)
    
    # ADD COMPATIBILITY RULES
    compatibility_rules = [
        # Socket compatibility
        CompatibilityRule(
            id="socket_604_compatibility",
            rule_type=CompatibilityType.EXCLUDED,
            primary_component_id="hp_ml350g4p",
            secondary_component_id="intel_xeon_e5620",
            condition="Socket 604 vs Socket 1366"
        ),
        CompatibilityRule(
            id="socket_1366_compatibility",
            rule_type=CompatibilityType.EXCLUDED,
            primary_component_id="dell_poweredge_r710",
            secondary_component_id="intel_xeon_3_0_604",
            condition="Socket 1366 vs Socket 604"
        ),
        
        # Memory type compatibility
        CompatibilityRule(
            id="ddr2_ddr3_incompatible",
            rule_type=CompatibilityType.EXCLUDED,
            primary_component_id="kingston_1gb_ddr2_400",
            secondary_component_id="samsung_4gb_ddr3_1333",
            condition="DDR2 and DDR3 cannot be mixed"
        ),
        CompatibilityRule(
            id="ddr2_ddr3_incompatible_reverse",
            rule_type=CompatibilityType.EXCLUDED,
            primary_component_id="samsung_4gb_ddr3_1333",
            secondary_component_id="kingston_1gb_ddr2_400",
            condition="DDR3 and DDR2 cannot be mixed"
        ),
        
        # Quantity limits
        CompatibilityRule(
            id="max_processors_hp",
            rule_type=CompatibilityType.LIMITED,
            primary_component_id="intel_xeon_3_0_604",
            max_quantity=2,
            condition="HP ML350 G4p supports max 2 processors"
        ),
        CompatibilityRule(
            id="max_memory_slots_hp",
            rule_type=CompatibilityType.LIMITED,
            primary_component_id="kingston_1gb_ddr2_400",
            max_quantity=8,
            condition="HP ML350 G4p has 8 memory slots"
        ),
        CompatibilityRule(
            id="max_memory_slots_dell",
            rule_type=CompatibilityType.LIMITED,
            primary_component_id="samsung_4gb_ddr3_1333",
            max_quantity=18,
            condition="Dell R710 has 18 memory slots"
        ),
        
        # Required components - these rules are too restrictive, removing them
        # CompatibilityRule(
        #     id="require_server",
        #     rule_type=CompatibilityType.REQUIRED,
        #     primary_component_id="hp_ml350g4p",
        #     condition="At least one server chassis is required"
        # ),
        # CompatibilityRule(
        #     id="require_power_supply",
        #     rule_type=CompatibilityType.REQUIRED,
        #     primary_component_id="hp_460w_psu",
        #     condition="At least one power supply is required"
        # )
    ]
    
    for rule in compatibility_rules:
        data.add_compatibility_rule(rule)
    
    return data


def create_compatibility_matrix() -> dict:
    """
    Create a compatibility matrix for quick lookup
    Returns dict with component_id -> list of compatible component_ids
    """
    matrix = {
        # HP ML350 G4p compatibility - server is compatible with all its components
        "hp_ml350g4p": [
            "intel_xeon_3_0_604", "intel_xeon_3_2_604",
            "kingston_1gb_ddr2_400", "corsair_2gb_ddr2_533",
            "seagate_500gb_sata", "wd_1tb_sata",
            "hp_460w_psu"
        ],
        
        # Dell R710 compatibility - server is compatible with all its components
        "dell_poweredge_r710": [
            "intel_xeon_e5620",
            "samsung_4gb_ddr3_1333",
            "seagate_500gb_sata", "wd_1tb_sata",
            "dell_750w_psu"
        ],
        
        # Socket 604 processors - compatible with HP server and other Socket 604 components
        "intel_xeon_3_0_604": ["hp_ml350g4p", "intel_xeon_3_2_604", "kingston_1gb_ddr2_400", "corsair_2gb_ddr2_533", "seagate_500gb_sata", "wd_1tb_sata", "hp_460w_psu"],
        "intel_xeon_3_2_604": ["hp_ml350g4p", "intel_xeon_3_0_604", "kingston_1gb_ddr2_400", "corsair_2gb_ddr2_533", "seagate_500gb_sata", "wd_1tb_sata", "hp_460w_psu"],
        
        # Socket 1366 processors - compatible with Dell server and other Socket 1366 components
        "intel_xeon_e5620": ["dell_poweredge_r710", "samsung_4gb_ddr3_1333", "seagate_500gb_sata", "wd_1tb_sata", "dell_750w_psu"],
        
        # DDR2 memory - compatible with HP server and Socket 604 processors
        "kingston_1gb_ddr2_400": ["hp_ml350g4p", "intel_xeon_3_0_604", "intel_xeon_3_2_604", "corsair_2gb_ddr2_533", "seagate_500gb_sata", "wd_1tb_sata", "hp_460w_psu"],
        "corsair_2gb_ddr2_533": ["hp_ml350g4p", "intel_xeon_3_0_604", "intel_xeon_3_2_604", "kingston_1gb_ddr2_400", "seagate_500gb_sata", "wd_1tb_sata", "hp_460w_psu"],
        
        # DDR3 memory - compatible with Dell server and Socket 1366 processors
        "samsung_4gb_ddr3_1333": ["dell_poweredge_r710", "intel_xeon_e5620", "seagate_500gb_sata", "wd_1tb_sata", "dell_750w_psu"],
        
        # Storage (compatible with all servers and processors)
        "seagate_500gb_sata": ["hp_ml350g4p", "dell_poweredge_r710", "intel_xeon_3_0_604", "intel_xeon_3_2_604", "intel_xeon_e5620", "kingston_1gb_ddr2_400", "corsair_2gb_ddr2_533", "samsung_4gb_ddr3_1333", "wd_1tb_sata", "hp_460w_psu", "dell_750w_psu"],
        "wd_1tb_sata": ["hp_ml350g4p", "dell_poweredge_r710", "intel_xeon_3_0_604", "intel_xeon_3_2_604", "intel_xeon_e5620", "kingston_1gb_ddr2_400", "corsair_2gb_ddr2_533", "samsung_4gb_ddr3_1333", "seagate_500gb_sata", "hp_460w_psu", "dell_750w_psu"],
        
        # Power supplies - compatible with their respective servers and all components
        "hp_460w_psu": ["hp_ml350g4p", "intel_xeon_3_0_604", "intel_xeon_3_2_604", "kingston_1gb_ddr2_400", "corsair_2gb_ddr2_533", "seagate_500gb_sata", "wd_1tb_sata"],
        "dell_750w_psu": ["dell_poweredge_r710", "intel_xeon_e5620", "samsung_4gb_ddr3_1333", "seagate_500gb_sata", "wd_1tb_sata"]
    }
    
    return matrix
