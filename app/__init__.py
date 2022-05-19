from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)

    # Registering the main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Registering the auth blueprint
    from .auth import auth as auth_blueprint
    # The url_prefix argument will add a prefix to all the routes registered with that blueprint Eg:-localhost:5000/authenticate/login
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    return app