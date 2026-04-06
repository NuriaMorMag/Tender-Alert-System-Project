from flask import Flask, request, render_template
from database_helper import save_company

app = Flask(__name__)


# --------------------------------------------------
# ROUTE: HOME PAGE
# --------------------------------------------------
# Shows a form where companies register
# --------------------------------------------------
@app.route("/", methods=["GET", "POST"])
def index():

    # If user submits form
    if request.method == "POST":

        # Create company object
        company = {
            "email": request.form["email"],
            "description": request.form["description"]
        }

        # Save company
        save_company(company)

        return "Company registered successfully!"

    # If GET → show form
    return render_template("index.html")


# Run app
if __name__ == "__main__":
    app.run(debug=True)