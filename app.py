from flask import Flask
from config import Config
from ext import db, bcrypt, login_manager, migrate
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Ensure the upload folder exists
    app.config['UPLOAD_FOLDER'] = 'uploads/'
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    # Set the login view for the login manager
    login_manager.login_view = 'main.login'

    # Importing and registering blueprints and models
    with app.app_context():
        from models import User  # Ensure User model is imported
        from routes import main_blueprint

        # Register the blueprint
        app.register_blueprint(main_blueprint)

        # Define the user_loader callback
        @login_manager.user_loader
        def load_user(user_id):
            return User.query.get(int(user_id))  # Load user from the database by ID

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
