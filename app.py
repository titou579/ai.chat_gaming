from flask import Flask, request, jsonify
from ultimate_ai import UltimateAI

# Création de l'application Flask
app = Flask(__name__)

# Instance de ton moteur AI
ai = UltimateAI()


# Route principale (test)
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "Ultimate AI running",
        "endpoints": {
            "POST /chat": {"message": "your message here"}
        }
    })


# Route principale de chat
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "Missing 'message' field"}), 400

    user_message = data["message"]
    response = ai.respond(user_message)

    return jsonify({
        "user": user_message,
        "response": response
    })


# Lancement en mode local
if __name__ == "__main__":
    app.run(debug=True)
