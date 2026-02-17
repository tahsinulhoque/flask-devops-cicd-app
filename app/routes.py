from flask import Blueprint, jsonify

main_routes = Blueprint("main", __name__)

@main_routes.route("/")
def home():
    return jsonify({
        "message": "version 2 deployed 🚀"
    })

@main_routes.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })
