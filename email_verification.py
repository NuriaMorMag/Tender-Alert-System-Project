# email_verification.py
from email.mime.text import MIMEText
import smtplib
from urllib.parse import urlencode

# In a real system, load these from environment variables (.env)
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_USER = "your_email@example.com"
SMTP_PASS = "your_password"

# Base URL of your deployed app (for example, on Google Cloud)
BASE_URL = "https://your-domain.com"  # change this in production


def send_verification_email(to_email: str, token: str):
    """
    Send an email with a verification link.
    The link looks like:
    https://your-domain.com/verify?token=abc123
    """
    params = urlencode({"token": token})
    verification_link = f"{BASE_URL}/verify?{params}"

    subject = "Verify your email for Tender Alerts"
    body = (
        "Hello,\n\n"
        "Thank you for registering for Tender Alerts.\n"
        "Please click the link below to verify your email address:\n\n"
        f"{verification_link}\n\n"
        "If you did not request this, you can ignore this email.\n"
    )

    send_email(to_email, subject, body)


def send_email(to_email: str, subject: str, body: str):
    """
    Send a plain text email using SMTP.
    This needs a real SMTP server to work in production.
    """
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SMTP_USER
    msg["To"] = to_email

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(msg)