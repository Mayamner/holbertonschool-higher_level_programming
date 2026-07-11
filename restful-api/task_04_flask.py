#!/usr/bin/env python3
"""Module for a simple API built with Flask."""
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28,
              "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30,
              "city": "New York"}
}


@app.route("/")
def home():
    """Return a welcome message."""
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    """Return a list of all usernames."""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Return the API status."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Return the full object for a given username, or 404."""
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user to the users dictionary."""
    new_user = request.get_json(silent=True)

    if new_user is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = new_user.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = new_user
    return jsonify({"message": "User added", "user": new_user}), 201


if __name__ == "__main__":
    app.run()
