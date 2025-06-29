# app/dependencies/services.py
from fastapi import Depends
from sqlalchemy.orm import Session

from app.repositories.PersonRepository import PersonRepository
from app.services.PersonService import PersonService
from app.dependencies.db import get_db


def get_person_service(db: Session = Depends(get_db)) -> PersonService:
    person_repo = PersonRepository(db)
    return PersonService(person_repo)
