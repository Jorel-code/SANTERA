from flask import Flask, jsonify
from flask_cors import CORS

from .config import Config
from .extensions import db, migrate


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    CORS(app)

    db.init_app(app)
    migrate.init_app(app, db)

    @app.get("/api/v1/health")
    def health():
        return jsonify({
            "success": True,
            "data": {
                "status": "ok"
            }
        }), 200

    @app.get("/api/v1/health/db")
    def database_health():
        try:
            from sqlalchemy import text

            db.session.execute(text("SELECT 1"))

            return jsonify({
                "success": True,
                "data": {
                    "database": "connected"
                }
            }), 200

        except Exception:
            app.logger.exception("Database connection failed")

            return jsonify({
                "success": False,
                "error": {
                    "message": "Database connection failed"
                }
            }), 503

    return app