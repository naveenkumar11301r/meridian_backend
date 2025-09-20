from pydantic import BaseModel, EmailStr
from typing import Optional

class QuoteRequest(BaseModel):
    type: str  # "individual" or "organization"
    full_name: str
    email: EmailStr
    phone: str
    organization_name: Optional[str] = None
    gst_number: Optional[str] = None
    location: str
    quantity: int
    contact_method: str
    notes: Optional[str] = None
