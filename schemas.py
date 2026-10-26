from pydantic import BaseModel,ConfigDict

class Student(BaseModel):
    name:str
    age:int
    course:str

class Response(Student):
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "Praneetha",
                "age": 21,
                "course": "CSE"
            }
        }
    )
    