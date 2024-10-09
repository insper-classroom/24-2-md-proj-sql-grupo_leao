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
@app.post("/locals/", response_model=Local)
def create_local(local: Local):
    locais_db = load_data(LOCAL_FILE)
    locais_db.append(local.dict())
    save_data(LOCAL_FILE, locais_db)
    return local

@app.get("/locals/", response_model=List[Local])
def read_locals():
    locais_db = load_data(LOCAL_FILE)
    return locais_db

@app.get("/locals/{local_id}", response_model=Local)
def read_local(local_id: int):
    locais_db = load_data(LOCAL_FILE)
    local = next((l for l in locais_db if l["id"] == local_id), None)
    if local is None:
        raise HTTPException(status_code=404, detail="Local not found")
    return local

@app.put("/locals/{local_id}", response_model=Local)
def update_local_partial(local_id: int, local_update: LocalUpdate):
    locais_db = load_data(LOCAL_FILE)
    for i, local in enumerate(locais_db):
        if local["id"] == local_id:
            update_data = local_update.dict(exclude_unset=True) 
            locais_db[i].update(update_data)
            save_data(LOCAL_FILE, locais_db)
            return locais_db[i]
    raise HTTPException(status_code=404, detail="Local not found")

@app.delete("/locals/{local_id}")
def delete_local(local_id: int):
    locais_db = load_data(LOCAL_FILE)
    locais_db = [l for l in locais_db if l["id"] != local_id]
    save_data(LOCAL_FILE, locais_db)
    return {"detail": "Local deleted successfully"}

# CRUD for Event Types

@app.post("/eventtypes/", response_model=EventType)
def create_event_type(event_type: EventType):
    event_types_db = load_data(EVENT_TYPE_FILE)
    event_types_db.append(event_type.dict())
    save_data(EVENT_TYPE_FILE, event_types_db)
    return event_type

@app.get("/eventtypes/", response_model=List[EventType])
def read_event_types():
    event_types_db = load_data(EVENT_TYPE_FILE)
    return event_types_db

@app.get("/eventtypes/{tipo_evento_id}", response_model=EventType)
def read_event_type(tipo_evento_id: int):
    event_types_db = load_data(EVENT_TYPE_FILE)
    event_type = next((et for et in event_types_db if et["id"] == tipo_evento_id), None)
    if event_type is None:
        raise HTTPException(status_code=404, detail="Event Type not found")
    return event_type

@app.put("/eventtypes/{event_type_id}", response_model=EventType)
def update_local_partial(local_id: int, event_type_update: EventTypeUpdate):
    eventtype_db = load_data(EVENT_TYPE_FILE)
    for i, eventtype in enumerate(eventtype_db):
        if eventtype["id"] == event_type_id:
            update_data = event_type_update.dict(exclude_unset=True) 
            eventtype_db[i].update(update_data)
            save_data(EVENT_TYPE_FILE, eventtype_db)
            return eventtype_db[i]
    raise HTTPException(status_code=404, detail="Event Type not found")

@app.delete("/eventtypes/{tipo_evento_id}")
def delete_event_type(tipo_evento_id: int):
    event_types_db = load_data(EVENT_TYPE_FILE)
    event_types_db = [et for et in event_types_db if et["id"] != tipo_evento_id]
    save_data(EVENT_TYPE_FILE, event_types_db)
    return {"detail": "Event Type deleted successfully"}

# CRUD for Events

@app.post("/events/", response_model=Event)
def create_event(event: Event):
    events_db = load_data(EVENT_FILE)
    events_db.append(event.dict())
    save_data(EVENT_FILE, events_db)
    return event

@app.get("/events/", response_model=List[Event])
def read_events():
    events_db = load_data(EVENT_FILE)
    return events_db

@app.get("/events/{event_id}", response_model=Event)
def read_event(event_id: int):
    events_db = load_data(EVENT_FILE)
    event = next((e for e in events_db if e["id"] == event_id), None)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@app.put("/events/{event_id}", response_model=Event)
def update_local_partial(local_id: int, event_update: EventUpdate):
    event_db = load_data(EVENT_FILE)
    for i, event in enumerate(event_db):
        if event["id"] == event_id:
            update_data = event_update.dict(exclude_unset=True) 
            event_db[i].update(update_data)
            save_data(EVENT_FILE, event_db)
            return event_db[i]
    raise HTTPException(status_code=404, detail="Event not found")

@app.delete("/eventos/{event_id}")
def delete_event(event_id: int):
    events_db = load_data(EVENT_FILE)
    events_db = [e for e in events_db if e["id"] != event_id]
    save_data(EVENT_FILE, events_db)
    return {"detail": "Event deleted successfully"}
