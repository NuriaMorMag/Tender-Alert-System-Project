# app.py

from flask import Flask, request, render_template
from database_helper import init_db, save_user

app = Flask(__name__)

# Initialize database when app starts
init_db()


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Main page where users can subscribe using their email.
    """

    if request.method == "POST":
        email = request.form.get("email")

        if not email:
            return "Email is required!", 400

        # Save user email into database
        save_user(email)

        return "Successfully subscribed to tender alerts!"

    # Show HTML form
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

from database_helper import remove_user


@app.route("/unsubscribe", methods=["POST"])
def unsubscribe():
    """
    Remove user from database.
    """
    email = request.form.get("email")

    if email:
        remove_user(email)
        return "You have been unsubscribed."

    return "Invalid request", 400