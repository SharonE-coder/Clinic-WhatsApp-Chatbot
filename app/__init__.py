# app package initializer
from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()  # loads .env if present

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'devkey')
    # register blueprints
    from app.routes.webhook import webhook_bp
    app.register_blueprint(webhook_bp, url_prefix="/webhook")
    return app
