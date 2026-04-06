# --------------------------------------------------
# FUNCTION: send_email
# --------------------------------------------------
# This simulates sending an email.
#
# In production:
# - Use SMTP or services like:
#   - SendGrid
#   - AWS SES
# --------------------------------------------------
def send_email(to, subject, body):

    print("------ EMAIL SENT ------")
    print(f"To: {to}")
    print(f"Subject: {subject}")
    print(f"Message: {body}")
    print("------------------------")