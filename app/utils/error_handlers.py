from flask import jsonify
from marshmallow import ValidationError


def register_error_handlers(app):
    @app.errorhandler(ValidationError)
    def handle_validation_error(err):
        return jsonify({"message": "Validation error", "errors": err.messages}), 400

    @app.errorhandler(404)
    def nf(e):
        return jsonify({"message": "Not found"}), 404

    @app.errorhandler(Exception)
    def ie(e):
        app.logger.exception(e);
        return jsonify({"message": "Internal server error"}), 500
