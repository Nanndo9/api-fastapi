from fastapi import FastAPI
from app.routes import personRoute
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(personRoute.router)


@app.get("/listar") 
def read_root():
    return {"Hello": "World"}
