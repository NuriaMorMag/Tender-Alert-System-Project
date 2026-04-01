import uuid

# Generate a unique token for email verification
def generate_token():
    return str(uuid.uuid4())

def send_verification_email(email):
    # Create a unique token
    token = generate_token()

    # Create verification link
    link = f"http://localhost:5000/verify/{token}"

    # Simulate sending email (for now just print)
    print(f"[EMAIL] Send this link to {email}: {link}")