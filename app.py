def index():
    return render_template("index.html")

# Route to handle form submission
@app.route("/register", methods=["POST"])
def register():
    # Get data from form
    email = request.form["email"]
    description = request.form["description"]

    # Save user to database
    save_user(email, description)

    # Send verification email
    send_verification_email(email)

    return "Check your email to verify your account!"

# Run the app
if __name__ == "__main__":git init
    app.run(debug=True)