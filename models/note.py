from pydantic import BaseModel


class Note(BaseModel):
    title: str
    desc: set
    important: bool = None

