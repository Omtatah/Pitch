from flask_login import LoginManager
from flask import Flask
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask Extensions
photos = UploadSet('photos', IMAGES)
bootstrap = Bootstrap()
mail = Mail()
db = SQLAlchemy()

login_manager.login_view = 'auth.login'
login_manager = LoginManager()
login_manager.session_protection = 'strong'


def create_app(config_name):
    app = Flask(__name__)

    # Create app configurations
    app.config.from_object(config_options[config_name])

    # Initialize flask extensions
    mail.init_app(app)
    login_manager.init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)

    # Register BluePrint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Register auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/authenticate')

    # configure UploadSet
    configure_uploads(app, photos)

    return app
