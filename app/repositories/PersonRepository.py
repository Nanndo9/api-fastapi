from sqlalchemy.orm import Session
from typing import Optional
import uuid

from app.models import Person
from app.schemas import PersonCreate


class PersonRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, person_id: uuid.UUID) -> Optional[Person]:
        return self.db.query(Person).filter(Person.id == person_id).one_or_none()

    def create(self, person: PersonCreate) -> Person:
        db_person = Person(**person.model_dump())
        self.db.add(db_person)
        self.db.commit()
        self.db.refresh(db_person)
        return db_person
