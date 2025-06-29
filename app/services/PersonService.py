from sqlalchemy.orm import Session
from typing import Optional
import uuid

from app.schemas import PersonCreate, PersonRead
from app.repositories.PersonRepository import PersonRepository


class PersonService:
    def __init__(self, person_repo: PersonRepository):
        self.person_repo = person_repo

    def create_person_service(self, person: PersonCreate) -> PersonRead:
        db_person = self.person_repo.create(person)
        return PersonRead.model_validate(db_person)

    def get_person_by_id_service(self, person_id: uuid.UUID) -> Optional[PersonRead]:
        db_person = self.person_repo.get_by_id(person_id)
        if db_person:
            return PersonRead.model_validate(db_person)
        return None