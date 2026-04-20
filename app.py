from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Phishing triage app is running"

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json(silent=True) or {}

    return jsonify({
        "verdict": "Test only",
        "confidence": "Low",
        "summary": "Endpoint is working and received the request.",
        "received_keys": list(data.keys())
    })
