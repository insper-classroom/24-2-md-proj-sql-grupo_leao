import json
import os
from typing import List, Union
from fastapi import FastAPI, HTTPException
from models import *

app = FastAPI()

DB_DIR = "db"
LOCAL_FILE = os.path.join(DB_DIR, "Local.json")
EVENT_TYPE_FILE = os.path.join(DB_DIR, "EventType.json")
EVENT_FILE = os.path.join(DB_DIR, "Event.json")


def load_data(file_path: str):
    if not os.path.exists(file_path):
        return []
    if os.path.getsize(file_path) == 0:
        return []
    with open(file_path, "r") as file:
        return json.load(file)


def save_data(file_path: str, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

# CRUD for Locals


@app.post("/locals/", response_model=Local, tags=["Locals"], summary='Creates a new local', description="Creates a new local (location) by accepting details such as name, address, city, capacity, and phone number. The local information is stored in a JSON database.")
def create_local(local: Local):
    locais_db = load_data(LOCAL_FILE)
    locais_db.append(local.dict())
    save_data(LOCAL_FILE, locais_db)
    return local


@app.get("/locals/", response_model=List[Local], tags=["Locals"], summary='Fetches all locals', description="Retrieves all locals (locations) from the database. The list includes all the locals stored, with details like name, address, city, capacity, and phone number.")
def read_locals():
    locais_db = load_data(LOCAL_FILE)
    return locais_db


@app.get("/locals/{local_id}", response_model=Local, tags=["Locals"], summary='Fetches a specific local', description="Fetches the details of a specific local by providing the local ID. Returns the local's name, address, city, capacity, and phone number if found, otherwise returns an error.")
def read_local(local_id: int):
    locais_db = load_data(LOCAL_FILE)
    local = next((l for l in locais_db if l["id"] == local_id), None)
    if local is None:
        raise HTTPException(status_code=404, detail="Local not found")
    return local


@app.put("/locals/{local_id}", response_model=Local, tags=["Locals"], summary='Updates a specific local', description="Partially updates an existing local by providing the local ID and the new details to be updated. Only the fields that are passed will be updated in the JSON database.")
def update_local_partial(local_id: int, local_update: LocalUpdate):
    locais_db = load_data(LOCAL_FILE)
    for i, local in enumerate(locais_db):
        if local["id"] == local_id:
            update_data = local_update.dict(exclude_unset=True)
            locais_db[i].update(update_data)
            save_data(LOCAL_FILE, locais_db)
            return locais_db[i]
    raise HTTPException(status_code=404, detail="Local not found")


@app.delete("/locals/{local_id}", tags=["Locals"], summary='Deletes a local', description="Deletes a specific local from the database by providing the local ID. If the local is found, it will be removed from the JSON database, otherwise an error will be returned.")
def delete_local(local_id: int):
    locais_db = load_data(LOCAL_FILE)
    locais_db = [l for l in locais_db if l["id"] != local_id]
    save_data(LOCAL_FILE, locais_db)
    return {"detail": "Local deleted successfully"}

# CRUD for Event Types


@app.post("/eventtypes/", response_model=EventType, tags=["Event Type"], summary='Creates a new event type', description="Creates a new event type by accepting details such as category, description, and target audience. The event type information is stored in a JSON database.")
def create_event_type(event_type: EventType):
    event_types_db = load_data(EVENT_TYPE_FILE)
    event_types_db.append(event_type.dict())
    save_data(EVENT_TYPE_FILE, event_types_db)
    return event_type


@app.get("/eventtypes/", response_model=List[EventType], tags=["Event Type"], summary='Fetches all event types', description="Retrieves all event types from the database. The list includes all the event types stored, with details like category, description, and target audience.")
def read_event_types():
    event_types_db = load_data(EVENT_TYPE_FILE)
    return event_types_db


@app.get("/eventtypes/{tipo_evento_id}", response_model=EventType, tags=["Event Type"], summary='Fetches a specific event type', description="Fetches the details of a specific event type by providing the event type ID. Returns the event type's category, description, and target audience if found, otherwise returns an error.")
def read_event_type(tipo_evento_id: int):
    event_types_db = load_data(EVENT_TYPE_FILE)
    event_type = next(
        (et for et in event_types_db if et["id"] == tipo_evento_id), None)
    if event_type is None:
        raise HTTPException(status_code=404, detail="Event Type not found")
    return event_type


@app.put("/eventtypes/{event_type_id}", response_model=EventType, tags=["Event Type"], summary='Updates a specific event type', description="Partially updates an existing event type by providing the event type ID and the new details to be updated. Only the fields that are passed will be updated in the JSON database.")
def update_local_partial(local_id: int, event_type_update: EventTypeUpdate):
    eventtype_db = load_data(EVENT_TYPE_FILE)
    for i, eventtype in enumerate(eventtype_db):
        if eventtype["id"] == event_type_id:
            update_data = event_type_update.dict(exclude_unset=True)
            eventtype_db[i].update(update_data)
            save_data(EVENT_TYPE_FILE, eventtype_db)
            return eventtype_db[i]
    raise HTTPException(status_code=404, detail="Event Type not found")


@app.delete("/eventtypes/{tipo_evento_id}", tags=["Event Type"], summary='Deletes an event type', description="Deletes a specific event type from the database by providing the event type ID. If the event type is found, it will be removed from the JSON database, otherwise an error will be returned.")
def delete_event_type(tipo_evento_id: int):
    event_types_db = load_data(EVENT_TYPE_FILE)
    event_types_db = [
        et for et in event_types_db if et["id"] != tipo_evento_id]
    save_data(EVENT_TYPE_FILE, event_types_db)
    return {"detail": "Event Type deleted successfully"}

# CRUD for Events


@app.post("/events/", response_model=Event, tags=["Event"], summary='Creates a new event', description="Creates a new event by accepting details such as name, description, start and end dates, times, location, and event type. The event information is stored in a JSON database.")
def create_event(event: Event):
    events_db = load_data(EVENT_FILE)
    events_db.append(event.dict())
    save_data(EVENT_FILE, events_db)
    return event


@app.get("/events/", response_model=List[Event], tags=["Event"], summary='Fetches all events', description="Retrieves all events from the database. The list includes all the events stored, with details like name, description, start and end dates, times, location, and event type.")
def read_events():
    events_db = load_data(EVENT_FILE)
    return events_db


@app.get("/events/{event_id}", response_model=Event, tags=["Event"], summary='Fetches a specific event', description="Fetches the details of a specific event by providing the event ID. Returns the event's name, description, start and end dates, times, location, and event type if found, otherwise returns an error.")
def read_event(event_id: int):
    events_db = load_data(EVENT_FILE)
    event = next((e for e in events_db if e["id"] == event_id), None)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


@app.put("/events/{event_id}", response_model=Event, tags=["Event"], summary='Updates a specific event', description="Partially updates an existing event by providing the event ID and the new details to be updated. Only the fields that are passed will be updated in the JSON database.")
def update_local_partial(local_id: int, event_update: EventUpdate):
    event_db = load_data(EVENT_FILE)
    for i, event in enumerate(event_db):
        if event["id"] == event_id:
            update_data = event_update.dict(exclude_unset=True)
            event_db[i].update(update_data)
            save_data(EVENT_FILE, event_db)
            return event_db[i]
    raise HTTPException(status_code=404, detail="Event not found")


@app.delete("/eventos/{event_id}", tags=["Event"], summary='Deletes an event', description="Deletes a specific event from the database by providing the event ID. If the event is found, it will be removed from the JSON database, otherwise an error will be returned.")
def delete_event(event_id: int):
    events_db = load_data(EVENT_FILE)
    events_db = [e for e in events_db if e["id"] != event_id]
    save_data(EVENT_FILE, events_db)
    return {"detail": "Event deleted successfully"}
