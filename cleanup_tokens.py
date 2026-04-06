# cleanup_tokens.py
from database_helper import delete_expired_tokens

def run_cleanup():
    """Remove expired email verification tokens."""
    delete_expired_tokens()
    print("Expired verification tokens removed.")

if __name__ == "__main__":
    run_cleanup()