"""
Translations for Server Configurator
Support for Russian and English languages
"""

from typing import Dict

class Translations:
    """Translation manager"""
    
    def __init__(self, language: str = "ru"):
        self.language = language
        self.translations = {
            "ru": RUSSIAN,
            "en": ENGLISH
        }
    
    def get(self, key: str) -> str:
        """Get translation for key"""
        return self.translations.get(self.language, ENGLISH).get(key, key)
    
    def set_language(self, language: str) -> None:
        """Set current language"""
        if language in self.translations:
            self.language = language


# Russian translations
RUSSIAN = {
    # Component types
    "component_type_server": "Сервер",
    "component_type_processor": "Процессор",
    "component_type_memory": "Оперативная память",
    "component_type_storage": "Накопитель",
    "component_type_network": "Сетевой адаптер",
    "component_type_power_supply": "Блок питания",
    "component_type_cooling": "Система охлаждения",
    "component_type_chassis": "Корпус",
    
    # Component attributes
    "attr_form_factor": "Форм-фактор",
    "attr_max_processors": "Макс. процессоров",
    "attr_max_memory_slots": "Слотов памяти",
    "attr_max_memory_gb": "Макс. памяти (ГБ)",
    "attr_storage_bays": "Отсеков для дисков",
    "attr_power_supply_slots": "Слотов БП",
    "attr_socket_type": "Сокет",
    "attr_chipset": "Чипсет",
    "attr_frequency": "Частота",
    "attr_cores": "Ядер",
    "attr_cache": "Кэш",
    "attr_tdp": "TDP",
    "attr_capacity": "Объем",
    "attr_type": "Тип",
    "attr_speed": "Скорость",
    "attr_voltage": "Напряжение",
    "attr_interface": "Интерфейс",
    "attr_power": "Мощность",
    "attr_efficiency": "КПД",
    "attr_modular": "Модульный",
    
    # Messages
    "component_added": "Компонент добавлен",
    "component_removed": "Компонент удален",
    "component_not_found": "Компонент не найден",
    "already_in_config": "уже добавлен в конфигурацию",
    "not_compatible": "несовместим с",
    "too_many_components": "Слишком много компонентов",
    "not_enough_components": "Недостаточно компонентов",
    "required_component_missing": "Обязательный компонент отсутствует",
    "components_incompatible": "Компоненты несовместимы",
    
    # Configuration
    "configuration": "Конфигурация",
    "total_price": "Общая стоимость",
    "valid": "Действительна",
    "invalid": "Недействительна",
    "validation_errors": "Ошибки валидации",
    "no_errors": "Ошибок нет",
    
    # Actions
    "add": "Добавить",
    "remove": "Удалить",
    "clear": "Очистить",
    "search": "Поиск",
    "export": "Экспорт",
    "import": "Импорт",
    "save": "Сохранить",
    "load": "Загрузить",
    
    # Units
    "unit_ghz": "ГГц",
    "unit_mhz": "МГц",
    "unit_gb": "ГБ",
    "unit_mb": "МБ",
    "unit_tb": "ТБ",
    "unit_w": "Вт",
    "unit_v": "В",
    "unit_rpm": "об/мин",
    
    # UI
    "available_components": "Доступные компоненты",
    "selected_components": "Выбранные компоненты",
    "compatibility_info": "Информация о совместимости",
    "compatible_with": "Совместим с",
    "incompatible_with": "Несовместим с",
    "specifications": "Характеристики",
    "price": "Цена",
    "manufacturer": "Производитель",
    "model": "Модель",
    "description": "Описание",
    "availability": "Наличие",
    "in_stock": "В наличии",
    "out_of_stock": "Нет в наличии",
    
    # CLI
    "cli_welcome": "Конфигуратор серверов",
    "cli_help": "Введите 'help' для списка команд",
    "cli_goodbye": "До свидания!",
    "cli_unknown_command": "Неизвестная команда",
    "cli_list_components": "Список всех компонентов",
    "cli_current_config": "Текущая конфигурация",
    "cli_config_cleared": "Конфигурация очищена",
    "cli_search_results": "Результаты поиска для",
    "cli_no_results": "Ничего не найдено",
    
    # Errors
    "error": "Ошибка",
    "warning": "Предупреждение",
    "info": "Информация",
    "success": "Успешно",
}

# English translations
ENGLISH = {
    # Component types
    "component_type_server": "Server",
    "component_type_processor": "Processor",
    "component_type_memory": "Memory",
    "component_type_storage": "Storage",
    "component_type_network": "Network",
    "component_type_power_supply": "Power Supply",
    "component_type_cooling": "Cooling",
    "component_type_chassis": "Chassis",
    
    # Component attributes
    "attr_form_factor": "Form Factor",
    "attr_max_processors": "Max Processors",
    "attr_max_memory_slots": "Memory Slots",
    "attr_max_memory_gb": "Max Memory (GB)",
    "attr_storage_bays": "Storage Bays",
    "attr_power_supply_slots": "PSU Slots",
    "attr_socket_type": "Socket",
    "attr_chipset": "Chipset",
    "attr_frequency": "Frequency",
    "attr_cores": "Cores",
    "attr_cache": "Cache",
    "attr_tdp": "TDP",
    "attr_capacity": "Capacity",
    "attr_type": "Type",
    "attr_speed": "Speed",
    "attr_voltage": "Voltage",
    "attr_interface": "Interface",
    "attr_power": "Power",
    "attr_efficiency": "Efficiency",
    "attr_modular": "Modular",
    
    # Messages
    "component_added": "Component added",
    "component_removed": "Component removed",
    "component_not_found": "Component not found",
    "already_in_config": "already in configuration",
    "not_compatible": "is not compatible with",
    "too_many_components": "Too many components",
    "not_enough_components": "Not enough components",
    "required_component_missing": "Required component missing",
    "components_incompatible": "Components are incompatible",
    
    # Configuration
    "configuration": "Configuration",
    "total_price": "Total Price",
    "valid": "Valid",
    "invalid": "Invalid",
    "validation_errors": "Validation Errors",
    "no_errors": "No errors",
    
    # Actions
    "add": "Add",
    "remove": "Remove",
    "clear": "Clear",
    "search": "Search",
    "export": "Export",
    "import": "Import",
    "save": "Save",
    "load": "Load",
    
    # Units
    "unit_ghz": "GHz",
    "unit_mhz": "MHz",
    "unit_gb": "GB",
    "unit_mb": "MB",
    "unit_tb": "TB",
    "unit_w": "W",
    "unit_v": "V",
    "unit_rpm": "RPM",
    
    # UI
    "available_components": "Available Components",
    "selected_components": "Selected Components",
    "compatibility_info": "Compatibility Information",
    "compatible_with": "Compatible with",
    "incompatible_with": "Incompatible with",
    "specifications": "Specifications",
    "price": "Price",
    "manufacturer": "Manufacturer",
    "model": "Model",
    "description": "Description",
    "availability": "Availability",
    "in_stock": "In Stock",
    "out_of_stock": "Out of Stock",
    
    # CLI
    "cli_welcome": "Server Configurator",
    "cli_help": "Type 'help' for available commands",
    "cli_goodbye": "Goodbye!",
    "cli_unknown_command": "Unknown command",
    "cli_list_components": "List of all components",
    "cli_current_config": "Current configuration",
    "cli_config_cleared": "Configuration cleared",
    "cli_search_results": "Search results for",
    "cli_no_results": "No results found",
    
    # Errors
    "error": "Error",
    "warning": "Warning",
    "info": "Info",
    "success": "Success",
}


# Global translation instance
_translator = Translations("ru")

def t(key: str) -> str:
    """Get translation for key"""
    return _translator.get(key)

def set_language(language: str) -> None:
    """Set global language"""
    _translator.set_language(language)
