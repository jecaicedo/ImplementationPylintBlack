from pydantic import BaseModel

class Doctor(BaseModel):
    id: int
    name: str
    phone: int