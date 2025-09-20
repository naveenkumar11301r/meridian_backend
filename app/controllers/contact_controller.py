# app/controllers/contact_controller.py
from app.schemas.contact import ContactRequest
from app.database import db
from app.utils.contact.email_service import send_contact_notification

def submit_contact_controller(contact: ContactRequest):
    # Save contact form in DB
    db.contacts.insert_one(contact.dict())

    # Send email notification to admin
    send_contact_notification(contact)

    return {"message": "Contact form submitted successfully"}
