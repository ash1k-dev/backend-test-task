TEST_DATA_ADD_TASKS = [
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
TEST_DATA_ADD_TASKS_STATUS_CODE = 200
TEST_DATA_ADD_TASKS_LEN = 2
TEST_DATA_ADD_TASKS2 = [
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
TEST_DATA_ADD_TASKS_STATUS_CODE2 = 200
TEST_DATA_ADD_TASKS_LEN2 = 1
TEST_DATA_ADD_TASKS3 = [
    {
        "СтатусЗакрытия": True,
        "ПредставлениеЗаданияНаСмену": "string",
        "Линия": "string",
        "Смена": "string",
        "Бригада": "string",
        "НомерПартии": 0,
        "Номенклатура": "string",
        "КодЕКН": "string",
        "ИдентификаторРЦ": "string",
        "ДатаВремяНачалаСмены": "2024-03-04T08:10:38.110Z",
        "ДатаВремяОкончанияСмены": "2024-03-04T08:10:38.110Z",
    },
]
TEST_DATA_ADD_TASKS_STATUS_CODE3 = 422
TEST_DATA_ADD_TASKS_LEN3 = 0
LIST_DATA_ADD_TASKS = [
    (TEST_DATA_ADD_TASKS, TEST_DATA_ADD_TASKS_LEN, TEST_DATA_ADD_TASKS_STATUS_CODE),
    (TEST_DATA_ADD_TASKS2, TEST_DATA_ADD_TASKS_LEN2, TEST_DATA_ADD_TASKS_STATUS_CODE2),
    (TEST_DATA_ADD_TASKS3, TEST_DATA_ADD_TASKS_LEN3, TEST_DATA_ADD_TASKS_STATUS_CODE3),
]


TEST_DATA_TASK_ID = 0
TEST_DATA_GET_TASK_ID_STATUS_CODE = 200
LIST_DATA_GET_TASK_ID = [
    (TEST_DATA_ADD_TASKS, TEST_DATA_TASK_ID, TEST_DATA_ADD_TASKS_STATUS_CODE),
]


TEST_DATA_GET_TASKS_STATUS_CODE = 200
TEST_DATA_GET_TASKS_LEN = 2
TEST_DATA_GET_TASKS_STATUS_CODE2 = 200
TEST_DATA_GET_TASKS_LEN2 = 1
TEST_DATA_GET_TASKS_STATUS_CODE3 = 200
TEST_DATA_GET_TASKS_LEN3 = 0
LIST_DATA_GET_TASKS = [
    (TEST_DATA_ADD_TASKS, TEST_DATA_GET_TASKS_LEN, TEST_DATA_GET_TASKS_STATUS_CODE),
    (TEST_DATA_ADD_TASKS2, TEST_DATA_GET_TASKS_LEN2, TEST_DATA_GET_TASKS_STATUS_CODE2),
    (TEST_DATA_ADD_TASKS3, TEST_DATA_GET_TASKS_LEN3, TEST_DATA_GET_TASKS_STATUS_CODE3),
]

TEST_DATA_UPDATE_TASK = {
    "squad": "second squad",
}
TEST_DATA_UPDATE_TASK_STATUS_CODE = 200
LIST_DATA_UPDATE_TASK = [
    (TEST_DATA_ADD_TASKS, TEST_DATA_UPDATE_TASK, TEST_DATA_UPDATE_TASK_STATUS_CODE),
]
