# app/utils/email_service.py (add below existing functions)
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from dotenv import load_dotenv
import os

load_dotenv() 
def send_contact_notification(contact_data):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = os.getenv("BREVO_API_KEY")

    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
        sib_api_v3_sdk.ApiClient(configuration)
    )

    subject = f"New Contact Form Submission from {contact_data.name}"
    html_content = f"""
    <h3>New Contact Message</h3>
    <ul>
        <li><strong>Name:</strong> {contact_data.name}</li>
        <li><strong>Email:</strong> {contact_data.email}</li>
        {"<li><strong>Company:</strong> " + contact_data.company + "</li>" if contact_data.company else ""}
        <li><strong>Message:</strong> {contact_data.message}</li>
    </ul>
    """

    sender = {"name": "Meridian Contact", "email": "kaviyarasan912001@gmail.com"}
    to = [{"email": "kaviyarasan912001@gmail.com", "name": "Admin"}]  # Replace with admin email

    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=to,
        sender=sender,
        subject=subject,
        html_content=html_content,
    )

    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        print("Contact email sent: ", api_response)
    except ApiException as e:
        print("Exception when sending contact email: %s\n" % e)
