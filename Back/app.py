from flask import Flask
from flask_cors import CORS

from Back.config import Config
from Back.database import db
from Back.Routes.creature_routes import creature_bp


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    CORS(app)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(creature_bp, url_prefix="/api/creatures")

    @app.route("/")
    def home():
        return "Flask running"

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
