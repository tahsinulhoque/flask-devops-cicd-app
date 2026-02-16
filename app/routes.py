from flask import Blueprint, jsonify

main_routes = Blueprint("main", __name__)

@main_routes.route("/")
def home():
    return jsonify({
        "message": "Flask DevOps CI/CD App Running 🚀"
    })

@main_routes.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })
