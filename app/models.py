from typing import Optional
from pydantic import BaseModel, Field
from bson import ObjectId
from pydantic_core import core_schema
from pydantic import GetCoreSchemaHandler


# ✅ Custom ObjectId type compatible with Pydantic v2
class PyObjectId(ObjectId):
    @classmethod
    def __get_pydantic_core_schema__(cls, source_type, handler: GetCoreSchemaHandler) -> core_schema.CoreSchema:
        return core_schema.json_or_python_schema(
            python_schema=core_schema.with_info_plain_validator_function(cls.validate),
            json_schema=core_schema.str_schema()
        )

    @classmethod
    def validate(cls, v, info):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return str(v)


# ✅ Base model for shared patient fields
class PatientBase(BaseModel):
    name: str
    age: int
    gender: str
    condition: str


# ✅ Model for incoming data (POST request)
class PatientCreate(PatientBase):
    name: str


# ✅ Model for data returned to the client (includes MongoDB _id)
class PatientResponse(PatientBase):
    id: Optional[PyObjectId] = Field(alias="_id")

    class Config:
        populate_by_name = True
        json_encoders = {ObjectId: str}
        from_attributes = True
