# app/routes/contact.py
from fastapi import APIRouter
from app.schemas.contact import ContactRequest
from app.controllers.contact_controller import submit_contact_controller

router = APIRouter()

@router.post("/contact")
def submit_contact(contact: ContactRequest):
    return submit_contact_controller(contact)
