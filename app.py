# app.py
from flask import Flask, render_template, request, redirect, url_for
from database_helper import (
    init_db,
    create_company,
    verify_company_email,
    get_company_by_token,
    unsubscribe_company
)
from email_verification import send_verification_email
from keyword_extractor import generate_keywords
from website_analyzer import analyze_website

app = Flask(__name__)

# Create tables when app starts
init_db()

@app.route("/", methods=["GET", "POST"])
def index():
    """
    Registration page.
    User enters:
    - company name
    - email
    - website (optional)
    - description
    """
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        website = request.form["website"]
        description = request.form["description"]

        # Optional: analyze website text
        website_text = analyze_website(website)

        # Combine description + website text
        full_profile = description + " " + website_text

        # Generate keywords using AI (placeholder)
        keywords = generate_keywords(full_profile)

        # Save company and create verification token
        company_id, token = create_company(name, email, description, website, keywords)

        # Send verification email
        send_verification_email(email, token)

        return render_template("verification_result.html", message="Check your email to verify your account.")

    return render_template("index.html")


@app.route("/verify")
def verify():
    """User clicks email link to verify account."""
    token = request.args.get("token", "")
    company = get_company_by_token(token)

    if not company:
        return render_template("verification_result.html", message="Invalid or expired link.")

    verify_company_email(company["id"])
    return render_template("verification_result.html", message="Your email is now verified.")


@app.route("/unsubscribe", methods=["GET", "POST"])
def unsubscribe():
    """User can stop receiving alerts."""
    if request.method == "POST":
        email = request.form["email"]
        unsubscribe_company(email)
        return render_template("unsubscribe.html", message="You are unsubscribed.")

    return render_template("unsubscribe.html", message=None)


if __name__ == "__main__":
    app.run(debug=True)