from dal.email_client import send_email

def send_notification(recipients, subject, message):
    try:
        send_email(recipients=recipients, subject=subject, message=message)
        return{"message": "Notification sent successfully"}
    except Exception as e:
        print(f"Error sending notification: {e}")
        return{"message": "An error occurred while sending the notification"}