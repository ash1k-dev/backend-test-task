TEST_DATA_ADD_PRODUCTS_TASK = [
    {
        "СтатусЗакрытия": True,
        "ПредставлениеЗаданияНаСмену": "string",
        "Линия": "string",
        "Смена": "string",
        "Бригада": "string",
        "НомерПартии": 1,
        "ДатаПартии": "2024-03-04",
        "Номенклатура": "string",
        "КодЕКН": "string",
        "ИдентификаторРЦ": "string",
        "ДатаВремяНачалаСмены": "2024-03-04T08:10:38.110Z",
        "ДатаВремяОкончанияСмены": "2024-03-04T08:10:38.110Z",
    },
]
TEST_DATA_ADD_PRODUCTS = [
    {"УникальныйКодПродукта": "string", "НомерПартии": 1, "ДатаПартии": "2024-03-04"},
    {"УникальныйКодПродукта": "string2", "НомерПартии": 1, "ДатаПартии": "2024-03-04"},
]
TEST_DATA_ADD_PRODUCTS_STATUS_CODE = 200
TEST_DATA_ADD_PRODUCTS_LEN = 2
TEST_DATA_ADD_PRODUCTS_TASK2 = [
    {
        "СтатусЗакрытия": True,
        "ПредставлениеЗаданияНаСмену": "string",
        "Линия": "string",
        "Смена": "string",
        "Бригада": "string",
        "НомерПартии": 0,
        "ДатаПартии": "2024-03-04",
        "Номенклатура": "string",
        "КодЕКН": "string",
        "ИдентификаторРЦ": "string",
        "ДатаВремяНачалаСмены": "2024-03-04T08:10:38.110Z",
        "ДатаВремяОкончанияСмены": "2024-03-04T08:10:38.110Z",
    },
]
TEST_DATA_ADD_PRODUCTS2 = [
    {"УникальныйКодПродукта": "string", "НомерПартии": 1, "ДатаПартии": "2024-03-04"}
]
TEST_DATA_ADD_PRODUCTS_STATUS_CODE2 = 400
TEST_DATA_ADD_PRODUCTS_LEN2 = 0
LIST_DATA_PRODUCTS_TASKS = [
    (
        TEST_DATA_ADD_PRODUCTS_TASK,
        TEST_DATA_ADD_PRODUCTS,
        TEST_DATA_ADD_PRODUCTS_LEN,
        TEST_DATA_ADD_PRODUCTS_STATUS_CODE,
    ),
    (
        TEST_DATA_ADD_PRODUCTS_TASK2,
        TEST_DATA_ADD_PRODUCTS2,
        TEST_DATA_ADD_PRODUCTS_LEN2,
        TEST_DATA_ADD_PRODUCTS_STATUS_CODE2,
    ),
]


TEST_DATA_AGGREGATE_PRODUCTS_STATUS_CODE = 200
TEST_DATA_AGGREGATE_PRODUCT = "string2"
TEST_DATA_AGGREGATE_TASK = 1
LIST_DATA_AGGREGATE_PRODUCTS = [
    (
        TEST_DATA_ADD_PRODUCTS_TASK,
        TEST_DATA_ADD_PRODUCTS,
        TEST_DATA_AGGREGATE_PRODUCT,
        TEST_DATA_AGGREGATE_TASK,
        TEST_DATA_AGGREGATE_PRODUCTS_STATUS_CODE,
    ),
]
