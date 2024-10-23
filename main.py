import json
import os
from typing import List, Union
from models import *
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select

import sqlalchemy
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv
from sqlalchemy.engine import Connection

load_dotenv()
app = FastAPI()

user = os.getenv("USER")
secret_key = os.getenv("SECRET_KEY")
server = os.getenv("SERVER")

database_name = "eventsmanager"

mysql_url = f"mysql+mysqlconnector://{user}:{
    secret_key}@{server}"

mysql_url_db = f"mysql+mysqlconnector://{user}:{
    secret_key}@{server}/{database_name}"


""" sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args) """


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


def create_database(engine: Connection, database_name: str):
    with engine.connect() as conn:
        conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {database_name}"))
        conn.execute(text(f"USE {database_name}"))
        conn.commit()


engine = create_engine(mysql_url, echo=True)
enginedb = create_engine(mysql_url_db, echo=True)


@app.on_event("startup")
def on_startup(engine=engine, enginedb=enginedb):
    create_database(engine, database_name)
    SQLModel.metadata.create_all(enginedb)


# CRUD for Locals


@app.post("/locals/", response_model=Local, tags=["Locals"], summary='Creates a new local', description="Creates a new local (location) by accepting details such as name, address, city, capacity, and phone number. The local information is stored in a JSON database.")
def create_local(local: Local, session: SessionDep) -> Local:
    session.add(local)
    session.commit()
    session.refresh(local)
    return local

@app.get("/locals/", response_model=List[Local], tags=["Locals"], summary='Fetches all locals', description="Retrieves all locals (locations) from the database. The list includes all the locals stored, with details like name, address, city, capacity, and phone number.")
def read_locals(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[Local]:
    heroes = session.exec(select(Local).offset(offset).limit(limit)).all()
    return heroes


@app.get("/locals/{local_id}", response_model=Local, tags=["Locals"], summary='Fetches a specific local', description="Fetches the details of a specific local by providing the local ID. Returns the local's name, address, city, capacity, and phone number if found, otherwise returns an error.")
def read_local(local_id: int, session: SessionDep) -> Local:
    local = session.get(Local, local_id)
    if not local:
        raise HTTPException(status_code=404, detail="Local not found")
    return local


@app.patch("/locals/{local_id}", response_model=Local, tags=["Locals"], summary='Updates a specific local', description="Partially updates an existing local by providing the local ID and the new details to be updated. Only the fields that are passed will be updated in the JSON database.")
def update_local(local_id: int, local: LocalUpdate, session: SessionDep):
    local_db = session.get(Local, local_id)
    if not local_db:
        raise HTTPException(status_code=404, detail="Local not found")
    local_data = local.model_dump(exclude_unset=True)
    local_db.sqlmodel_update(local_data)
    session.add(local_db)
    session.commit()
    session.refresh(local_db)
    return local_db


@app.delete("/locals/{local_id}", tags=["Locals"], summary='Deletes a local', description="Deletes a specific local from the database by providing the local ID. If the local is found, it will be removed from the JSON database, otherwise an error will be returned.")
def delete_hero(local_id: int, session: SessionDep):
    local = session.get(Local, local_id)
    if not local:
        raise HTTPException(status_code=404, detail="Local not found")
    session.delete(local)
    session.commit()
    return {"ok": True}

# CRUD for Event Types


@app.post("/eventtypes/", response_model=EventType, tags=["Event Type"], summary='Creates a new event type', description="Creates a new event type by accepting details such as category, description, and target audience. The event type information is stored in a JSON database.")
def create_event_types(event: EventType, session: SessionDep) -> EventType:
    session.add(event)
    session.commit()
    session.refresh(event)
    return event


@app.get("/eventtypes/", response_model=List[EventType], tags=["Event Type"], summary='Fetches all event types', description="Retrieves all event types from the database. The list includes all the event types stored, with details like category, description, and target audience.")
def read_event_types(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[EventType]:
    heroes = session.exec(select(EventType).offset(offset).limit(limit)).all()
    return heroes


@app.get("/eventtypes/{tipo_evento_id}", response_model=EventType, tags=["Event Type"], summary='Fetches a specific event type', description="Fetches the details of a specific event type by providing the event type ID. Returns the event type's category, description, and target audience if found, otherwise returns an error.")
def read_event_type(event_type_id: int, session: SessionDep) -> EventType:
    event_type = session.get(EventType, event_type_id)
    if not event_type:
        raise HTTPException(status_code=404, detail="event_type not found")
    return event_type


@app.patch("/eventtypes/{event_type_id}", response_model=EventType, tags=["Event Type"], summary='Updates a specific event type', description="Partially updates an existing event type by providing the event type ID and the new details to be updated. Only the fields that are passed will be updated in the JSON database.")
def update_event(event_type_id: int, event_type: EventTypeUpdate, session: SessionDep):
    event_type_db = session.get(Local, event_type_id)
    if not event_type_db:
        raise HTTPException(status_code=404, detail="Event type not found")
    event_type_data = event_type.model_dump(exclude_unset=True)
    event_type_db.sqlmodel_update(event_type_data)
    session.add(event_type_db)
    session.commit()
    session.refresh(event_type_db)
    return event_type_db


@app.delete("/eventtypes/{tipo_evento_id}", tags=["Event Type"], summary='Deletes an event type', description="Deletes a specific event type from the database by providing the event type ID. If the event type is found, it will be removed from the JSON database, otherwise an error will be returned.")
def delete_event_type(tipo_evento_id: int, session: SessionDep):
    event_type = session.get(EventType, tipo_evento_id)
    if not event_type:
        raise HTTPException(status_code=404, detail="Event type not found")
    session.delete(event_type)
    session.commit()
    return {"ok": True}

# CRUD for Events


@app.post("/events/", response_model=Event, tags=["Event"], summary='Creates a new event', description="Creates a new event by accepting details such as name, description, start and end dates, times, location, and event type. The event information is stored in a JSON database.")
def create_event(event: Event, session: SessionDep) -> Event:
    session.add(event)
    session.commit()
    session.refresh(event)
    return event


@app.get("/events/", response_model=List[Event], tags=["Event"], summary='Fetches all events', description="Retrieves all events from the database. The list includes all the events stored, with details like name, description, start and end dates, times, location, and event type.")
def read_events(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[Event]:
    heroes = session.exec(select(Event).offset(offset).limit(limit)).all()
    return heroes


@app.get("/events/{event_id}", response_model=Event, tags=["Event"], summary='Fetches a specific event', description="Fetches the details of a specific event by providing the event ID. Returns the event's name, description, start and end dates, times, location, and event type if found, otherwise returns an error.")
def read_event(event_id: int, session: SessionDep) -> Event:
    event = session.get(Event, event_id)
    if not event:
        raise HTTPException(status_code=404, detail="event not found")
    return event


@app.patch("/events/{event_id}", response_model=Event, tags=["Event"], summary='Updates a specific event', description="Partially updates an existing event by providing the event ID and the new details to be updated. Only the fields that are passed will be updated in the JSON database.")
def update_event(event_id: int, event: EventUpdate, session: SessionDep):
    event_db = session.get(Local, event_id)
    if not event_db:
        raise HTTPException(status_code=404, detail="Event not found")
    event_data = event.model_dump(exclude_unset=True)
    event_db.sqlmodel_update(event_data)
    session.add(event_db)
    session.commit()
    session.refresh(event_db)
    return event_db


@app.delete("/eventos/{event_id}", tags=["Event"], summary='Deletes an event', description="Deletes a specific event from the database by providing the event ID. If the event is found, it will be removed from the JSON database, otherwise an error will be returned.")
def delete_event(evento_id: int, session: SessionDep):
    event = session.get(Event, evento_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    session.delete(event)
    session.commit()
    return {"ok": True}


@app.post("/local_event/", response_model=LocalEventLink, tags=["LocalEvent"],
          summary="Creates a new local-event relationship",
          description="Creates a new relationship between a location and an event by accepting the local_id and event_id. The relationship is stored in a JSON database.")
def create_local_event_link(local_event_link: LocalEventLink, session: SessionDep) -> LocalEventLink:
    # Verifica se o local existe
    local_exists = session.exec(select(Local).where(
        Local.id == local_event_link.local_id)).first()
    if not local_exists:
        raise HTTPException(status_code=404, detail="Location not found")

    # Verifica se o evento existe
    event_exists = session.exec(select(Event).where(
        Event.id == local_event_link.event_id)).first()
    if not event_exists:
        raise HTTPException(status_code=404, detail="Event not found")

    # Adiciona a relação entre Local e Event
    session.add(local_event_link)
    session.commit()
    session.refresh(local_event_link)
    return local_event_link


@app.get("/local_event/", response_model=List[LocalEventLink], tags=["LocalEvent"],
         summary="Retrieve all local-event relationships",
         description="Fetches all the relationships between locations and events.")
def get_all_local_event_links(session: SessionDep) -> List[LocalEventLink]:
    local_event_links = session.exec(select(LocalEventLink)).all()
    return local_event_links


@app.get("/local_event/{link_id}", response_model=LocalEventLink, tags=["LocalEvent"],
         summary="Retrieve a specific local-event relationship",
         description="Fetches a specific relationship between a location and an event by ID.")
def get_local_event_link(link_id: int, session: SessionDep) -> LocalEventLink:
    local_event_link = session.get(LocalEventLink, link_id)
    if not local_event_link:
        raise HTTPException(
            status_code=404, detail="Local-Event relationship not found")
    return local_event_link


@app.delete("/local_event/{link_id}", response_model=LocalEventLink, tags=["LocalEvent"])
def delete_local_event_link(local_event_link_id: int, session: SessionDep):
    local_event_link = session.get(LocalEventLink, local_event_link_id)
    if not local_event_link:
        raise HTTPException(
            status_code=404, detail="Local event link not found")
    session.delete(local_event_link)
    session.commit()
    return {"ok": True}
