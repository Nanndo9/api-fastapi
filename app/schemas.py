from pydantic import BaseModel, Field
from typing import Optional
import uuid


class PersonBase(BaseModel):
    nome: str
    sobrenome: str
    idade: int
    ativo: Optional[bool] = True


class PersonCreate(PersonBase):
    pass


class PersonUpdate(PersonBase):
    nome: Optional[str] = None
    sobrenome: Optional[str] = None
    idade: Optional[int] = None
    ativo: Optional[bool] = None


class PersonRead(PersonBase):
    id: uuid.UUID

    class Config:
        from_attributes = True