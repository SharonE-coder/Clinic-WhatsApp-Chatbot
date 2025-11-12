from flask import Blueprint, request, jsonify
import os

webhook_bp = Blueprint("webhook", __name__)

@webhook_bp.route("/", methods=["GET"])
def verify():
    # simple verification for now
    verify_token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")
    expected = os.getenv("WHATSAPP_VERIFY_TOKEN", "replace_verify_token")
    if verify_token == expected:
        return challenge or "OK", 200
    return "Verification failed", 403

@webhook_bp.route("/", methods=["POST"])
def receive_message():
    data = request.get_json(silent=True)
    print("Incoming JSON:", data)
    # placeholder: we will parse & respond later
    return jsonify({"status": "received"}), 200
