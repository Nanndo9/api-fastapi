from fastapi import APIRouter, Depends, HTTPException, status
from app.dependencies.services import get_person_service
from app.schemas import PersonCreate, PersonRead
from app.services.PersonService import PersonService
import uuid

router = APIRouter(
    prefix="/persons", tags=["Persons"], responses={404: {"description": "Not Found"}}
)


@router.post("/", response_model=PersonRead, status_code=status.HTTP_201_CREATED)
def create_new_person(
    person: PersonCreate, person_service: PersonService = Depends(get_person_service)
):
    db_person = person_service.create_person_service(person)
    return db_person


@router.get("/{person_id}", response_model=PersonRead)
def read_person(
    person_id: uuid.UUID, person_service: PersonService = Depends(get_person_service)
):
    db_person = person_service.get_person_by_id_service(person_id)
    if db_person is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Person not found"
        )
    return db_person