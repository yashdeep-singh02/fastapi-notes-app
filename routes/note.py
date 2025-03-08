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
            "title": doc["title"],
            "desc" : doc["desc"],
        })
    return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})

@note.post("/",response_class=HTMLResponse)
async def create_item(request: Request):
    pass
   