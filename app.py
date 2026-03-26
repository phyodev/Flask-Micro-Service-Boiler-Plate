import os
from flask import Flask, request, jsonify
from services import create_user
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/are-you-alive", methods=["GET"])
def are_you_alive():
    return {"status_code": "200", "message": "Alive Bro!!"}, 200

@app.route("/users", methods=["POST"])
def create_user_endpoint():
    data = request.json
    user = create_user(data["name"], data["email"])
    return jsonify({"id": user.id, "name": user.name, "email": user.email}), 201

@app.route("/health", methods=["GET"])
def health_check():
    return {"status": "ok"}, 200
