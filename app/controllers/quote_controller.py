# from app.database import db
# from app.schemas.quote import QuoteRequest

# def submit_quote_controller(quote: QuoteRequest):
#     db.quotes.insert_one(quote.dict())
#     return {"message": "Quote submitted successfully"}




from app.database import db
from app.schemas.quote import QuoteRequest
from app.utils.email_service import send_admin_notification 

def submit_quote_controller(quote: QuoteRequest):
    db.quotes.insert_one(quote.dict())  # Save to DB
    send_admin_notification(quote)      # Send email to admin
    return {"message": "Quote submitted successfully"}
