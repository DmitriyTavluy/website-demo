# Быстрый старт

## Что создано

Полнофункциональный конфигуратор серверов с:
- Проверкой совместимости компонентов
- Матрицей совместимости для быстрого поиска
- Валидацией конфигураций
- Экспортом в JSON/CSV
- Полным тестовым покрытием

## Установка

```bash
cd server_configurator
pip install -r requirements.txt
```

## Запуск тестов

```bash
python -m pytest test_configurator.py -v
```

Все 12 тестов должны пройти успешно.

## Использование в коде

```python
from configurator import ServerConfigurator

# Создать конфигуратор
configurator = ServerConfigurator()

# Добавить сервер
success, errors = configurator.add_component("hp_ml350g4p")
print(f"Success: {success}")

# Добавить процессор
success, errors = configurator.add_component("intel_xeon_3_0_604")
print(f"Success: {success}")

# Добавить память
success, errors = configurator.add_component("kingston_1gb_ddr2_400")
print(f"Success: {success}")

# Получить конфигурацию
config = configurator.get_current_configuration()
print(f"Total price: ${config.total_price}")
print(f"Valid: {config.is_valid}")

# Экспорт
json_data = configurator.export_configuration("json")
print(json_data)
```

## Структура проекта

```
server_configurator/
├── data_models.py          # Модели данных
├── sample_data.py          # Примеры и матрица совместимости
├── configurator.py         # Основная логика
├── cli.py                  # CLI интерфейс
├── test_configurator.py    # Тесты
├── README.md              # Документация
├── ARCHITECTURE.md        # Архитектура
├── QUICK_START.md         # Этот файл
└── requirements.txt       # Зависимости
```

## Ключевые концепции

### 1. Матрица совместимости

Вместо сложной логики используется матрица:

```python
{
    "hp_ml350g4p": ["intel_xeon_3_0_604", "kingston_1gb_ddr2_400", ...],
    "intel_xeon_3_0_604": ["hp_ml350g4p", "kingston_1gb_ddr2_400", ...]
}
```

**Преимущества:**
- Быстрый поиск O(1)
- Меньше кода
- Легко добавлять новые компоненты

### 2. Двунаправленная проверка

При добавлении компонента проверяется:
- Совместим ли новый компонент с существующими
- Совместимы ли существующие с новым

Это гарантирует полную совместимость.

### 3. Правила совместимости

Дополнительные правила для сложных случаев:
- Лимиты количества (max 2 процессора)
- Обязательные компоненты
- Взаимоисключающие компоненты

## Как добавить новый компонент

### 1. Создать компонент в `sample_data.py`

```python
Component(
    id="new_component_id",
    name="New Component Name",
    component_type=ComponentType.PROCESSOR,
    manufacturer="Manufacturer",
    model="Model",
    attributes=[
        ComponentAttribute("frequency", "3.5", "GHz"),
        ComponentAttribute("cores", "4")
    ],
    price=200.00
)
```

### 2. Добавить в матрицу совместимости

```python
"new_component_id": ["compatible_id_1", "compatible_id_2", ...]
```

### 3. Добавить в список совместимых компонентов других

```python
"existing_component_id": [..., "new_component_id"]
```

## Как добавить правило совместимости

```python
CompatibilityRule(
    id="unique_rule_id",
    rule_type=CompatibilityType.LIMITED,
    primary_component_id="component_id",
    max_quantity=2,
    condition="Description"
)
```

## Пример полной конфигурации

```python
from configurator import ServerConfigurator

configurator = ServerConfigurator()

# Добавляем компоненты
components_to_add = [
    "hp_ml350g4p",           # HP Server
    "intel_xeon_3_0_604",    # Processor
    "intel_xeon_3_2_604",    # Second Processor
    "kingston_1gb_ddr2_400", # Memory 1GB
    "kingston_1gb_ddr2_400", # Memory 1GB (duplicate, won't add)
    "corsair_2gb_ddr2_533",  # Memory 2GB
    "seagate_500gb_sata",    # HDD 500GB
    "wd_1tb_sata",           # HDD 1TB
    "hp_460w_psu"            # Power Supply
]

for component_id in components_to_add:
    success, errors = configurator.add_component(component_id)
    if not success:
        print(f"Failed to add {component_id}: {errors}")

# Получить конфигурацию
config = configurator.get_current_configuration()

print(f"\nConfiguration Summary:")
print(f"Total components: {sum(len(c) for c in config.components.values())}")
print(f"Total price: ${config.total_price:.2f}")
print(f"Valid: {config.is_valid}")

if config.validation_errors:
    print("\nValidation errors:")
    for error in config.validation_errors:
        print(f"  - {error}")
```

## Следующие шаги

1. **Расширить каталог компонентов** - добавить больше серверов, процессоров, памяти
2. **Создать веб-интерфейс** - HTML/CSS/JS или React
3. **Добавить базу данных** - SQLite для начала, PostgreSQL для масштабирования
4. **Создать API** - Flask/FastAPI REST API
5. **Парсинг спецификаций** - автоматический импорт из QuickSpecs

## Вопросы и ответы

**Q: Можно ли добавить один компонент несколько раз?**
A: Нет, система проверяет дубликаты. Для добавления нескольких одинаковых компонентов нужно расширить логику.

**Q: Как проверить совместимость двух компонентов без добавления?**
A: Используйте `get_compatibility_info(component_id)`

**Q: Можно ли изменить количество уже добавленного компонента?**
A: Сейчас нет. Нужно удалить и добавить снова нужное количество раз.

**Q: Как экспортировать конфигурацию?**
A: `configurator.export_configuration("json")` или `configurator.export_configuration("csv")`
