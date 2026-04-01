import smtplib
from email.mime.text import MIMEText

# Send a verification email to the user
def send_verification_email(email):
    # Create email message
    msg = MIMEText("Click this link to verify your account")
    msg["Subject"] = "Verify your account"
    msg["From"] = "your_email@gmail.com"
    msg["To"] = email

    try:
        # Connect to Gmail SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Secure connection

        # Login to email account
        server.login("your_email@gmail.com", "your_password")

        # Send email
        server.send_message(msg)

        # Close connection
        server.quit()

    except Exception as e:
        print("Error sending email:", e)