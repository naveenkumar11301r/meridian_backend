# app/schemas/contact.py
from pydantic import BaseModel, EmailStr

class ContactRequest(BaseModel):
    name: str
    email: EmailStr
    company: str | None = None
    message: str
