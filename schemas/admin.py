from typing import Optional
from pydantic import BaseModel

class Admin(BaseModel):
    id: Optional[int]
    name: str
    lastNameFather: str
    email: str
    password: str
    admin: bool = False