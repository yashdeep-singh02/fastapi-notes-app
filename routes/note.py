from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from models.note import Note
from config.db import conn
from schemas.note import noteEntity, notesEntity

note=APIRouter()

templates = Jinja2Templates(directory="templates")

@note.get("/",response_class=HTMLResponse)
async def read_root(request: Request):
    docs = conn.notes.notes.find({})
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id": doc["_id"],
            "note": doc["note"]
        })
    return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})

@note.post("/")
async def add_note(note: Note):
    inserted_note = conn.notes.notes.insert_one(dict(note))
    return noteEntity(inserted_note)