# app/utils/email_service.py
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from dotenv import load_dotenv
import os

load_dotenv()  # Load .env file if you're using one

def send_admin_notification(quote_data):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = os.getenv("BREVO_API_KEY")

    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

    subject = f"New Quote Request from {quote_data.full_name}"
    html_content = f"""
    <h3>New Quote Request Details</h3>
    <ul>
        <li><strong>Name:</strong> {quote_data.full_name}</li>
        <li><strong>Email:</strong> {quote_data.email}</li>
        <li><strong>Phone:</strong> {quote_data.phone}</li>
        <li><strong>Type:</strong> {quote_data.type}</li>
        {"<li><strong>Organization:</strong> " + quote_data.organization_name + "</li>" if quote_data.organization_name else ""}
        {"<li><strong>GST Number:</strong> " + quote_data.gst_number + "</li>" if quote_data.gst_number else ""}
        <li><strong>Location:</strong> {quote_data.location}</li>
        <li><strong>Quantity:</strong> {quote_data.quantity}</li>
        <li><strong>Contact Method:</strong> {quote_data.contact_method}</li>
        <li><strong>Notes:</strong> {quote_data.notes or 'None'}</li>
    </ul>
    """

    sender = {"name": "Meridian Quotes", "email": "nksmarty701@gmail.com"}
    to = [{"email": "nksmarty701@gmail.com", "name": "Admin"}]  # Replace with actual admin email

    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=to,
        sender=sender,
        subject=subject,
        html_content=html_content,
    )

    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        print("Email sent: ", api_response)
    except ApiException as e:
        print("Exception when sending email: %s\n" % e)
