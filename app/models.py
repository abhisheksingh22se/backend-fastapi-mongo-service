from typing import Optional, Any
from pydantic import BaseModel, Field, BeforeValidator
from typing_extensions import Annotated

PyObjectId = Annotated[str, BeforeValidator(str)]

class PatientBase(BaseModel):
    name: str = Field(..., min_length=1, description="Patient's full name")
    age: int = Field(..., gt=0, lt=150, description="Patient's age")
    gender: str = Field(..., pattern="^(Male|Female|Other)$")
    condition: str
    disease: str  

class PatientCreate(PatientBase):
    """Model used for validating incoming data"""
    pass

class PatientResponse(PatientBase):
    """Model used for returning data (handles _id conversion)"""
    id: Optional[PyObjectId] = Field(alias="_id", default=None)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "name": "John Doe",
                "age": 30,
                "gender": "Male",
                "condition": "Stable",
                "disease": "Flu"
            }
        }