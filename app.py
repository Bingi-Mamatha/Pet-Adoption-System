
from flask import Flask, render_template, request

app = Flask(__name__)

pets = [
    {"name": "Buddy", "type": "Dog", "age": "2 years"},
    {"name": "Milo", "type": "Cat", "age": "1 year"},
    {"name": "Coco", "type": "Rabbit", "age": "6 months"}
]


@app.route("/")
def home():
    return render_template("index.html", pets=pets)


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    pet = request.form.get("pet", "").strip()

    if not name or not email or not pet:
        return "Please fill in all fields.", 400

    if pet not in [p["name"] for p in pets]:
        return "Please select a valid pet.", 400

    return f"""
    <h1>Adoption Request Submitted!</h1>
    <p>Thank you, {name}.</p>
    <p>Your request for {pet} has been received.</p>
    <p>Confirmation email: {email}</p>
    <a href="/">Back to Home</a>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
