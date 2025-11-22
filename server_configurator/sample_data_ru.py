"""
Sample data for server configurator in RUSSIAN
Russian component names and descriptions
"""

from data_models import (
    Component, ComponentType, ComponentAttribute, 
    CompatibilityRule, CompatibilityType, ServerConfiguratorData
)


def create_sample_data_ru() -> ServerConfiguratorData:
    """Create sample data with Russian names and descriptions"""
    
    data = ServerConfiguratorData()
    
    # СЕРВЕРЫ
    servers = [
        Component(
            id="hp_ml350g4p",
            name="HP ProLiant ML350 G4p",
            component_type=ComponentType.SERVER,
            manufacturer="HP",
            model="ML350 G4p",
            attributes=[
                ComponentAttribute("Форм-фактор", "4U Стойка"),
                ComponentAttribute("Макс. процессоров", "2"),
                ComponentAttribute("Слотов памяти", "8"),
                ComponentAttribute("Макс. памяти", "32", "ГБ"),
                ComponentAttribute("Отсеков для дисков", "6"),
                ComponentAttribute("Слотов БП", "2"),
                ComponentAttribute("Сокет", "Socket 604"),
                ComponentAttribute("Чипсет", "Intel E7520")
            ],
            price=1500.00,
            description="Начальный серверный стоечный сервер с поддержкой двух процессоров"
        ),
        Component(
            id="dell_poweredge_r710",
            name="Dell PowerEdge R710",
            component_type=ComponentType.SERVER,
            manufacturer="Dell",
            model="R710",
            attributes=[
                ComponentAttribute("Форм-фактор", "2U Стойка"),
                ComponentAttribute("Макс. процессоров", "2"),
                ComponentAttribute("Слотов памяти", "18"),
                ComponentAttribute("Макс. памяти", "144", "ГБ"),
                ComponentAttribute("Отсеков для дисков", "6"),
                ComponentAttribute("Слотов БП", "2"),
                ComponentAttribute("Сокет", "Socket 1366"),
                ComponentAttribute("Чипсет", "Intel 5520")
            ],
            price=2000.00,
            description="Серверный стоечный сервер среднего уровня с большой емкостью памяти"
        ),
        Component(
            id="ibm_x3650_m3",
            name="IBM System x3650 M3",
            component_type=ComponentType.SERVER,
            manufacturer="IBM",
            model="x3650 M3",
            attributes=[
                ComponentAttribute("Форм-фактор", "2U Стойка"),
                ComponentAttribute("Макс. процессоров", "2"),
                ComponentAttribute("Слотов памяти", "18"),
                ComponentAttribute("Макс. памяти", "192", "ГБ"),
                ComponentAttribute("Отсеков для дисков", "8"),
                ComponentAttribute("Слотов БП", "2"),
                ComponentAttribute("Сокет", "Socket 1366"),
                ComponentAttribute("Чипсет", "Intel 5520")
            ],
            price=2500.00,
            description="Высокопроизводительный стоечный сервер для критичных нагрузок"
        )
    ]
    
    # ПРОЦЕССОРЫ
    processors = [
        Component(
            id="intel_xeon_3_0_604",
            name="Intel Xeon 3.0 ГГц",
            component_type=ComponentType.PROCESSOR,
            manufacturer="Intel",
            model="Xeon 3.0GHz Socket 604",
            attributes=[
                ComponentAttribute("Частота", "3.0", "ГГц"),
                ComponentAttribute("Ядер", "1"),
                ComponentAttribute("Сокет", "604"),
                ComponentAttribute("Кэш", "1", "МБ"),
                ComponentAttribute("TDP", "89", "Вт")
            ],
            price=150.00,
            description="Одноядерный процессор для серверов начального уровня"
        ),
        Component(
            id="intel_xeon_3_2_604",
            name="Intel Xeon 3.2 ГГц",
            component_type=ComponentType.PROCESSOR,
            manufacturer="Intel",
            model="Xeon 3.2GHz Socket 604",
            attributes=[
                ComponentAttribute("Частота", "3.2", "ГГц"),
                ComponentAttribute("Ядер", "1"),
                ComponentAttribute("Сокет", "604"),
                ComponentAttribute("Кэш", "1", "МБ"),
                ComponentAttribute("TDP", "103", "Вт")
            ],
            price=200.00,
            description="Одноядерный процессор с повышенной частотой"
        ),
        Component(
            id="intel_xeon_e5620",
            name="Intel Xeon E5620",
            component_type=ComponentType.PROCESSOR,
            manufacturer="Intel",
            model="E5620",
            attributes=[
                ComponentAttribute("Частота", "2.4", "ГГц"),
                ComponentAttribute("Ядер", "4"),
                ComponentAttribute("Сокет", "1366"),
                ComponentAttribute("Кэш", "12", "МБ"),
                ComponentAttribute("TDP", "80", "Вт")
            ],
            price=300.00,
            description="Четырехядерный процессор для высокопроизводительных задач"
        ),
        Component(
            id="intel_xeon_x5670",
            name="Intel Xeon X5670",
            component_type=ComponentType.PROCESSOR,
            manufacturer="Intel",
            model="X5670",
            attributes=[
                ComponentAttribute("Частота", "2.93", "ГГц"),
                ComponentAttribute("Ядер", "6"),
                ComponentAttribute("Сокет", "1366"),
                ComponentAttribute("Кэш", "12", "МБ"),
                ComponentAttribute("TDP", "95", "Вт")
            ],
            price=450.00,
            description="Шестиядерный процессор топового уровня"
        )
    ]
    
    # ОПЕРАТИВНАЯ ПАМЯТЬ
    memory_modules = [
        Component(
            id="kingston_1gb_ddr2_400",
            name="Kingston 1 ГБ DDR2-400",
            component_type=ComponentType.MEMORY,
            manufacturer="Kingston",
            model="1GB DDR2-400",
            attributes=[
                ComponentAttribute("Объем", "1", "ГБ"),
                ComponentAttribute("Тип", "DDR2"),
                ComponentAttribute("Частота", "400", "МГц"),
                ComponentAttribute("Форм-фактор", "DIMM"),
                ComponentAttribute("Напряжение", "1.8", "В")
            ],
            price=25.00,
            description="Модуль памяти DDR2 начального уровня"
        ),
        Component(
            id="corsair_2gb_ddr2_533",
            name="Corsair 2 ГБ DDR2-533",
            component_type=ComponentType.MEMORY,
            manufacturer="Corsair",
            model="2GB DDR2-533",
            attributes=[
                ComponentAttribute("Объем", "2", "ГБ"),
                ComponentAttribute("Тип", "DDR2"),
                ComponentAttribute("Частота", "533", "МГц"),
                ComponentAttribute("Форм-фактор", "DIMM"),
                ComponentAttribute("Напряжение", "1.8", "В")
            ],
            price=45.00,
            description="Модуль памяти DDR2 повышенной емкости"
        ),
        Component(
            id="samsung_4gb_ddr3_1333",
            name="Samsung 4 ГБ DDR3-1333",
            component_type=ComponentType.MEMORY,
            manufacturer="Samsung",
            model="4GB DDR3-1333",
            attributes=[
                ComponentAttribute("Объем", "4", "ГБ"),
                ComponentAttribute("Тип", "DDR3"),
                ComponentAttribute("Частота", "1333", "МГц"),
                ComponentAttribute("Форм-фактор", "DIMM"),
                ComponentAttribute("Напряжение", "1.5", "В")
            ],
            price=80.00,
            description="Современный модуль памяти DDR3"
        ),
        Component(
            id="crucial_8gb_ddr3_1600",
            name="Crucial 8 ГБ DDR3-1600",
            component_type=ComponentType.MEMORY,
            manufacturer="Crucial",
            model="8GB DDR3-1600",
            attributes=[
                ComponentAttribute("Объем", "8", "ГБ"),
                ComponentAttribute("Тип", "DDR3"),
                ComponentAttribute("Частота", "1600", "МГц"),
                ComponentAttribute("Форм-фактор", "DIMM"),
                ComponentAttribute("Напряжение", "1.5", "В")
            ],
            price=150.00,
            description="Высокоемкий модуль памяти DDR3 с высокой частотой"
        )
    ]
    
    # НАКОПИТЕЛИ
    storage_devices = [
        Component(
            id="seagate_500gb_sata",
            name="Seagate 500 ГБ SATA",
            component_type=ComponentType.STORAGE,
            manufacturer="Seagate",
            model="500GB SATA",
            attributes=[
                ComponentAttribute("Объем", "500", "ГБ"),
                ComponentAttribute("Интерфейс", "SATA"),
                ComponentAttribute("Скорость", "7200", "об/мин"),
                ComponentAttribute("Форм-фактор", "3.5\""),
                ComponentAttribute("Кэш", "16", "МБ")
            ],
            price=60.00,
            description="Надежный жесткий диск для базовых задач"
        ),
        Component(
            id="wd_1tb_sata",
            name="Western Digital 1 ТБ SATA",
            component_type=ComponentType.STORAGE,
            manufacturer="Western Digital",
            model="1TB SATA",
            attributes=[
                ComponentAttribute("Объем", "1", "ТБ"),
                ComponentAttribute("Интерфейс", "SATA"),
                ComponentAttribute("Скорость", "7200", "об/мин"),
                ComponentAttribute("Форм-фактор", "3.5\""),
                ComponentAttribute("Кэш", "64", "МБ")
            ],
            price=100.00,
            description="Емкий жесткий диск для хранения данных"
        ),
        Component(
            id="intel_ssd_240gb",
            name="Intel SSD 240 ГБ SATA",
            component_type=ComponentType.STORAGE,
            manufacturer="Intel",
            model="240GB SSD",
            attributes=[
                ComponentAttribute("Объем", "240", "ГБ"),
                ComponentAttribute("Интерфейс", "SATA 3.0"),
                ComponentAttribute("Тип", "SSD"),
                ComponentAttribute("Форм-фактор", "2.5\""),
                ComponentAttribute("Скорость чтения", "550", "МБ/с")
            ],
            price=180.00,
            description="Быстрый твердотельный накопитель"
        )
    ]
    
    # БЛОКИ ПИТАНИЯ
    power_supplies = [
        Component(
            id="hp_460w_psu",
            name="HP Блок питания 460 Вт",
            component_type=ComponentType.POWER_SUPPLY,
            manufacturer="HP",
            model="460W PSU",
            attributes=[
                ComponentAttribute("Мощность", "460", "Вт"),
                ComponentAttribute("КПД", "80+"),
                ComponentAttribute("Форм-фактор", "Стандартный"),
                ComponentAttribute("Модульный", "Нет")
            ],
            price=120.00,
            description="Блок питания для серверов HP"
        ),
        Component(
            id="dell_750w_psu",
            name="Dell Блок питания 750 Вт",
            component_type=ComponentType.POWER_SUPPLY,
            manufacturer="Dell",
            model="750W PSU",
            attributes=[
                ComponentAttribute("Мощность", "750", "Вт"),
                ComponentAttribute("КПД", "80+ Gold"),
                ComponentAttribute("Форм-фактор", "Стандартный"),
                ComponentAttribute("Модульный", "Нет")
            ],
            price=180.00,
            description="Энергоэффективный блок питания для серверов Dell"
        ),
        Component(
            id="ibm_835w_psu",
            name="IBM Блок питания 835 Вт",
            component_type=ComponentType.POWER_SUPPLY,
            manufacturer="IBM",
            model="835W PSU",
            attributes=[
                ComponentAttribute("Мощность", "835", "Вт"),
                ComponentAttribute("КПД", "80+ Platinum"),
                ComponentAttribute("Форм-фактор", "Стандартный"),
                ComponentAttribute("Модульный", "Нет")
            ],
            price=220.00,
            description="Высокоэффективный блок питания для серверов IBM"
        )
    ]
    
    # Добавление всех компонентов
    all_components = servers + processors + memory_modules + storage_devices + power_supplies
    for component in all_components:
        data.add_component(component)
    
    # ПРАВИЛА СОВМЕСТИМОСТИ
    compatibility_rules = [
        # Совместимость сокетов
        CompatibilityRule(
            id="socket_604_compatibility",
            rule_type=CompatibilityType.EXCLUDED,
            primary_component_id="hp_ml350g4p",
            secondary_component_id="intel_xeon_e5620",
            condition="Socket 604 против Socket 1366"
        ),
        CompatibilityRule(
            id="socket_1366_compatibility_hp",
            rule_type=CompatibilityType.EXCLUDED,
            primary_component_id="hp_ml350g4p",
            secondary_component_id="intel_xeon_x5670",
            condition="Socket 604 против Socket 1366"
        ),
        
        # Совместимость типов памяти
        CompatibilityRule(
            id="ddr2_ddr3_incompatible_1",
            rule_type=CompatibilityType.EXCLUDED,
            primary_component_id="kingston_1gb_ddr2_400",
            secondary_component_id="samsung_4gb_ddr3_1333",
            condition="DDR2 и DDR3 нельзя использовать вместе"
        ),
        CompatibilityRule(
            id="ddr2_ddr3_incompatible_2",
            rule_type=CompatibilityType.EXCLUDED,
            primary_component_id="corsair_2gb_ddr2_533",
            secondary_component_id="crucial_8gb_ddr3_1600",
            condition="DDR2 и DDR3 нельзя использовать вместе"
        ),
        
        # Лимиты количества
        CompatibilityRule(
            id="max_processors_2",
            rule_type=CompatibilityType.LIMITED,
            primary_component_id="intel_xeon_3_0_604",
            max_quantity=2,
            condition="Максимум 2 процессора на сервер"
        ),
        CompatibilityRule(
            id="max_memory_slots_hp",
            rule_type=CompatibilityType.LIMITED,
            primary_component_id="kingston_1gb_ddr2_400",
            max_quantity=8,
            condition="HP ML350 G4p имеет 8 слотов памяти"
        ),
        CompatibilityRule(
            id="max_memory_slots_dell",
            rule_type=CompatibilityType.LIMITED,
            primary_component_id="samsung_4gb_ddr3_1333",
            max_quantity=18,
            condition="Dell R710 имеет 18 слотов памяти"
        )
    ]
    
    for rule in compatibility_rules:
        data.add_compatibility_rule(rule)
    
    return data


def create_compatibility_matrix_extended() -> dict:
    """
    Extended compatibility matrix with all components
    """
    matrix = {
        # HP ML350 G4p - Socket 604, DDR2
        "hp_ml350g4p": [
            "intel_xeon_3_0_604", "intel_xeon_3_2_604",
            "kingston_1gb_ddr2_400", "corsair_2gb_ddr2_533",
            "seagate_500gb_sata", "wd_1tb_sata", "intel_ssd_240gb",
            "hp_460w_psu"
        ],
        
        # Dell R710 - Socket 1366, DDR3
        "dell_poweredge_r710": [
            "intel_xeon_e5620", "intel_xeon_x5670",
            "samsung_4gb_ddr3_1333", "crucial_8gb_ddr3_1600",
            "seagate_500gb_sata", "wd_1tb_sata", "intel_ssd_240gb",
            "dell_750w_psu"
        ],
        
        # IBM x3650 M3 - Socket 1366, DDR3
        "ibm_x3650_m3": [
            "intel_xeon_e5620", "intel_xeon_x5670",
            "samsung_4gb_ddr3_1333", "crucial_8gb_ddr3_1600",
            "seagate_500gb_sata", "wd_1tb_sata", "intel_ssd_240gb",
            "ibm_835w_psu"
        ],
        
        # Socket 604 процессоры
        "intel_xeon_3_0_604": ["hp_ml350g4p", "intel_xeon_3_2_604", "kingston_1gb_ddr2_400", "corsair_2gb_ddr2_533", "seagate_500gb_sata", "wd_1tb_sata", "intel_ssd_240gb", "hp_460w_psu"],
        "intel_xeon_3_2_604": ["hp_ml350g4p", "intel_xeon_3_0_604", "kingston_1gb_ddr2_400", "corsair_2gb_ddr2_533", "seagate_500gb_sata", "wd_1tb_sata", "intel_ssd_240gb", "hp_460w_psu"],
        
        # Socket 1366 процессоры
        "intel_xeon_e5620": ["dell_poweredge_r710", "ibm_x3650_m3", "intel_xeon_x5670", "samsung_4gb_ddr3_1333", "crucial_8gb_ddr3_1600", "seagate_500gb_sata", "wd_1tb_sata", "intel_ssd_240gb", "dell_750w_psu", "ibm_835w_psu"],
        "intel_xeon_x5670": ["dell_poweredge_r710", "ibm_x3650_m3", "intel_xeon_e5620", "samsung_4gb_ddr3_1333", "crucial_8gb_ddr3_1600", "seagate_500gb_sata", "wd_1tb_sata", "intel_ssd_240gb", "dell_750w_psu", "ibm_835w_psu"],
        
        # DDR2 память
        "kingston_1gb_ddr2_400": ["hp_ml350g4p", "intel_xeon_3_0_604", "intel_xeon_3_2_604", "corsair_2gb_ddr2_533", "seagate_500gb_sata", "wd_1tb_sata", "intel_ssd_240gb", "hp_460w_psu"],
        "corsair_2gb_ddr2_533": ["hp_ml350g4p", "intel_xeon_3_0_604", "intel_xeon_3_2_604", "kingston_1gb_ddr2_400", "seagate_500gb_sata", "wd_1tb_sata", "intel_ssd_240gb", "hp_460w_psu"],
        
        # DDR3 память
        "samsung_4gb_ddr3_1333": ["dell_poweredge_r710", "ibm_x3650_m3", "intel_xeon_e5620", "intel_xeon_x5670", "crucial_8gb_ddr3_1600", "seagate_500gb_sata", "wd_1tb_sata", "intel_ssd_240gb", "dell_750w_psu", "ibm_835w_psu"],
        "crucial_8gb_ddr3_1600": ["dell_poweredge_r710", "ibm_x3650_m3", "intel_xeon_e5620", "intel_xeon_x5670", "samsung_4gb_ddr3_1333", "seagate_500gb_sata", "wd_1tb_sata", "intel_ssd_240gb", "dell_750w_psu", "ibm_835w_psu"],
        
        # Накопители (совместимы со всеми)
        "seagate_500gb_sata": ["hp_ml350g4p", "dell_poweredge_r710", "ibm_x3650_m3", "intel_xeon_3_0_604", "intel_xeon_3_2_604", "intel_xeon_e5620", "intel_xeon_x5670", "kingston_1gb_ddr2_400", "corsair_2gb_ddr2_533", "samsung_4gb_ddr3_1333", "crucial_8gb_ddr3_1600", "wd_1tb_sata", "intel_ssd_240gb", "hp_460w_psu", "dell_750w_psu", "ibm_835w_psu"],
        "wd_1tb_sata": ["hp_ml350g4p", "dell_poweredge_r710", "ibm_x3650_m3", "intel_xeon_3_0_604", "intel_xeon_3_2_604", "intel_xeon_e5620", "intel_xeon_x5670", "kingston_1gb_ddr2_400", "corsair_2gb_ddr2_533", "samsung_4gb_ddr3_1333", "crucial_8gb_ddr3_1600", "seagate_500gb_sata", "intel_ssd_240gb", "hp_460w_psu", "dell_750w_psu", "ibm_835w_psu"],
        "intel_ssd_240gb": ["hp_ml350g4p", "dell_poweredge_r710", "ibm_x3650_m3", "intel_xeon_3_0_604", "intel_xeon_3_2_604", "intel_xeon_e5620", "intel_xeon_x5670", "kingston_1gb_ddr2_400", "corsair_2gb_ddr2_533", "samsung_4gb_ddr3_1333", "crucial_8gb_ddr3_1600", "seagate_500gb_sata", "wd_1tb_sata", "hp_460w_psu", "dell_750w_psu", "ibm_835w_psu"],
        
        # Блоки питания
        "hp_460w_psu": ["hp_ml350g4p", "intel_xeon_3_0_604", "intel_xeon_3_2_604", "kingston_1gb_ddr2_400", "corsair_2gb_ddr2_533", "seagate_500gb_sata", "wd_1tb_sata", "intel_ssd_240gb"],
        "dell_750w_psu": ["dell_poweredge_r710", "intel_xeon_e5620", "intel_xeon_x5670", "samsung_4gb_ddr3_1333", "crucial_8gb_ddr3_1600", "seagate_500gb_sata", "wd_1tb_sata", "intel_ssd_240gb"],
        "ibm_835w_psu": ["ibm_x3650_m3", "intel_xeon_e5620", "intel_xeon_x5670", "samsung_4gb_ddr3_1333", "crucial_8gb_ddr3_1600", "seagate_500gb_sata", "wd_1tb_sata", "intel_ssd_240gb"]
    }
    
    return matrix
