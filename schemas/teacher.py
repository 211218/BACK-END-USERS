from typing import Optional
from pydantic import BaseModel

class Teacher(BaseModel):
    id: Optional[int]
    name: str
    lastNameFather: str
    email: str
    password: str
    teacher: bool = False