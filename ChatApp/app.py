from flask import Flask, app
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_socketio import SocketIO
from extensions import db, login_manager, socketio
from models import User  # Make sure the User model is correctly imported




def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    socketio.init_app(app)

    # Set the login view for flask-login
    login_manager.login_view = "auth.login"

    migrate = Migrate(app, db)

    # Register blueprints
    from routes.auth_routes import auth_bp
    from routes.chat_routes import chat_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(chat_bp)

    return app

# Define the user_loader function
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  # Ensure that your User model is properly set up

if __name__ == "__main__":
    app = create_app()
    socketio.run(app)