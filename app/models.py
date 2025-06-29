

from sqlalchemy import Boolean, Integer, String, text
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Person(Base):
    __tablename__ = "pessoas"

    id :Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),primary_key=True,default=text("gen_random_uuid()")
    )
    nome:Mapped[str]= mapped_column(String)
    sobrenome:Mapped[str]= mapped_column(String)
    idade:Mapped[int]= mapped_column(Integer)
    ativo:Mapped[bool]= mapped_column(Boolean,default=True)
