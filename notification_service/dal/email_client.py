import smtplib
from email.mime.text import MIMEText
from config.settings import settings

def send_email(recipients, subject, message):
    message_content = "\n".join(f"{item.title}: {item.url}" for item in message)
    
    msg = MIMEText(message_content)
    msg["Subject"] = subject
    msg["From"] = settings.DEFAULT_SENDER_EMAIL
    msg["To"] = ", ".join(recipients)
    
    with smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT) as server:
        server.starttls()
        server.login(settings.EMAIL_USERNAME, settings.EMAIL_PASSWORD)
        server.sendmail(settings.DEFAULT_SENDER_EMAIL, recipients, msg.as_string())

