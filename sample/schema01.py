import pydantic


class Model(pydantic.BaseModel):
    name: str = 'John Doe'
    age: int = 20
