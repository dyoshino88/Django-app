from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_email(subject, message, to_emails):
    sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
    from_email = settings.DEFAULT_FROM_EMAIL

    mail = Mail(
        from_email=from_email,
        to_emails=to_emails,
        subject=subject,
        plain_text_content=message
    )

    try:
        response = sg.send(mail)
        return response.status_code
    except Exception as e:
        return e
