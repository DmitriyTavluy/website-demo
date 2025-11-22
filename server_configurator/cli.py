"""
Command Line Interface for Server Configurator
Simple CLI for testing and demonstrating the configurator
"""

from configurator import ServerConfigurator
from data_models import ComponentType


def print_separator():
    """Print visual separator"""
    print("=" * 60)


def print_component(component):
    """Print component information"""
    print(f"  ID: {component.id}")
    print(f"  Name: {component.name}")
    print(f"  Manufacturer: {component.manufacturer}")
    print(f"  Model: {component.model}")
    print(f"  Price: ${component.price or 0:.2f}")
    if component.attributes:
        print("  Attributes:")
        for attr in component.attributes:
            unit_str = f" {attr.unit}" if attr.unit else ""
            print(f"    {attr.name}: {attr.value}{unit_str}")
    print()


def print_configuration(config):
    """Print current configuration"""
    print_separator()
    print(f"CONFIGURATION: {config.name}")
    print(f"Total Price: ${config.total_price:.2f}")
    print(f"Valid: {'✅' if config.is_valid else '❌'}")
    
    if config.validation_errors:
        print("Validation Errors:")
        for error in config.validation_errors:
            print(f"  ❌ {error}")
        print()
    
    print("Components:")
    for comp_type, components in config.components.items():
        if components:
            print(f"  {comp_type.value.upper()}:")
            for comp in components:
                print(f"    - {comp.name} (${comp.price or 0:.2f})")
    print_separator()


def main():
    """Main CLI loop"""
    configurator = ServerConfigurator()
    
    print("🖥️  SERVER CONFIGURATOR")
    print("Type 'help' for available commands")
    print_separator()
    
    while True:
        try:
            command = input("configurator> ").strip().lower()
            
            if command == "help":
                print_help()
            
            elif command == "list":
                list_components(configurator)
            
            elif command.startswith("add "):
                component_id = command[4:].strip()
                add_component(configurator, component_id)
            
            elif command.startswith("remove "):
                component_id = command[7:].strip()
                remove_component(configurator, component_id)
            
            elif command == "config":
                config = configurator.get_current_configuration()
                print_configuration(config)
            
            elif command == "clear":
                configurator.clear_configuration()
                print("Configuration cleared")
            
            elif command.startswith("search "):
                query = command[7:].strip()
                search_components(configurator, query)
            
            elif command.startswith("compat "):
                component_id = command[7:].strip()
                show_compatibility(configurator, component_id)
            
            elif command == "export":
                export_configuration(configurator)
            
            elif command == "quit" or command == "exit":
                print("Goodbye!")
                break
            
            else:
                print("Unknown command. Type 'help' for available commands.")
        
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")


def print_help():
    """Print help information"""
    print("Available commands:")
    print("  help                    - Show this help")
    print("  list                    - List all available components")
    print("  add <component_id>      - Add component to configuration")
    print("  remove <component_id>   - Remove component from configuration")
    print("  config                  - Show current configuration")
    print("  clear                   - Clear current configuration")
    print("  search <query>          - Search components")
    print("  compat <component_id>   - Show compatibility info")
    print("  export                  - Export configuration")
    print("  quit/exit               - Exit program")


def list_components(configurator):
    """List all available components"""
    print_separator()
    print("AVAILABLE COMPONENTS:")
    print()
    
    for comp_type in ComponentType:
        components = configurator.data.get_components_by_type(comp_type)
        if components:
            print(f"{comp_type.value.upper()}:")
            for comp in components:
                print(f"  {comp.id}: {comp.name} (${comp.price or 0:.2f})")
            print()


def add_component(configurator, component_id):
    """Add component to configuration"""
    success, errors = configurator.add_component(component_id)
    
    if success:
        component = configurator.get_component_details(component_id)
        print(f"✅ Added {component.name} to configuration")
    else:
        print("❌ Failed to add component:")
        for error in errors:
            print(f"  - {error}")


def remove_component(configurator, component_id):
    """Remove component from configuration"""
    success = configurator.remove_component(component_id)
    
    if success:
        component = configurator.get_component_details(component_id)
        print(f"✅ Removed {component.name} from configuration")
    else:
        print(f"❌ Component {component_id} not found in configuration")


def search_components(configurator, query):
    """Search components"""
    results = configurator.search_components(query)
    
    if results:
        print(f"Search results for '{query}':")
        for comp in results:
            print(f"  {comp.id}: {comp.name} ({comp.component_type.value})")
    else:
        print(f"No components found for '{query}'")


def show_compatibility(configurator, component_id):
    """Show compatibility information"""
    compat_info = configurator.get_compatibility_info(component_id)
    component = configurator.get_component_details(component_id)
    
    if not component:
        print(f"❌ Component {component_id} not found")
        return
    
    print(f"Compatibility for {component.name}:")
    print(f"  Compatible with: {', '.join(compat_info['compatible_with']) or 'None'}")
    print(f"  Incompatible with: {', '.join(compat_info['incompatible_with']) or 'None'}")


def export_configuration(configurator):
    """Export current configuration"""
    try:
        json_export = configurator.export_configuration("json")
        print("JSON Export:")
        print(json_export)
        
        print("\n" + "="*40 + "\n")
        
        csv_export = configurator.export_configuration("csv")
        print("CSV Export:")
        print(csv_export)
        
    except Exception as e:
        print(f"❌ Export failed: {e}")


if __name__ == "__main__":
    main()
