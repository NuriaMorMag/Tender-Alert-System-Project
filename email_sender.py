# email_sender.py - FIXED SECURITY

import smtplib
import os
from email.mime.text import MIMEText


def send_email(to_email, tender_text):
    """
    Send an email alert with tender information.
    """

    # Get credentials from environment variables
    sender = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASS")

    if not sender or not password:
        print("Email credentials not set!")
        return

    msg = MIMEText(f"New relevant tender found:\n\n{tender_text}")
    msg["Subject"] = "Tender Alert 🚨"
    msg["From"] = sender
    msg["To"] = to_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.send_message(msg)
    except Exception as e:
        print(f"Error sending email to {to_email}: {e}")