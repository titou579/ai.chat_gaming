from flask import Flask, render_template, request, jsonify
from ultimate_ai import UltimateAI

app = Flask(__name__)
ai = UltimateAI()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "Message vide"}), 400

    response = ai.respond(user_message)

    return jsonify({
        "response": response
    })

if __name__ == "__main__":
    app.run(debug=True)
