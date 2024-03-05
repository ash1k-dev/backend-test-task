def to_pydantic(db_object, pydantic_model):
    """Преобразование объекта базы данных в модель Pydantic"""
    return pydantic_model(**db_object.__dict__)
