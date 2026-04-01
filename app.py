from flask import Flask, render_template, request
from database_helper import save_user
from email_verification import send_verification_email

# Create Flask app
app = Flask(__name__)

# Home page (shows the form)
@app.route("/")
def index():
    return render_template("index.html")


# Route to handle form submission
@app.route("/register", methods=["POST"])
def register():
    # Get data from the form
    email = request.form["email"]
    description = request.form["description"]

    # Save user in database
    save_user(email, description)

    # Send email to verify the account
    send_verification_email(email)

    return "Check your email to verify your account!"


# Run the app
if __name__ == "__main__":
    app.run(debug=True)