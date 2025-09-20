from fastapi import APIRouter
from app.schemas.quote import QuoteRequest
from app.controllers.quote_controller import submit_quote_controller

router = APIRouter()

@router.post("/quote")
def submit_quote(quote: QuoteRequest):
    return submit_quote_controller(quote)
