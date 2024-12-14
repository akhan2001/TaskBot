from flask import Flask
from app.routes import tasks, suggestions, email, auth

def create_app():
    app = Flask(__name__)

    # Add routes
    app.register_blueprint(tasks.bp)
    app.register_blueprint(suggestions.bp)
    app.register_blueprint(email.bp)
    app.register_blueprint(auth.bp)

    return app
