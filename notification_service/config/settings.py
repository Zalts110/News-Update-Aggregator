class Settings:
    SMTP_SERVER = "smtp.gmail.com"  # Replace with your SMTP server
    SMTP_PORT = 587                 # Port for TLS (use 465 for SSL)
    EMAIL_USERNAME = "zalts110@gmail.com"  # Replace with your email address
    EMAIL_PASSWORD = "pnzn lawm xeul lovg"           # Replace with your email password
    DEFAULT_SENDER_EMAIL = "zalts110@gmail.com"  # Replace with the sender email address

    # Optional service-related settings
    NOTIFICATION_RETRY_LIMIT = 3    # Number of retry attempts for failed notifications

# Instantiate the settings object
settings = Settings()
