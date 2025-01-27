from flask import Flask

from src.config import Config
from src.views import main_bp, auth_bp, library_bp
from src.models import db, User
from src.commands import init_db, populate_db
from src.extensions import migrate, login_manager


BLUEPRINTS = [main_bp, auth_bp, library_bp]
COMMANDS = [init_db, populate_db]


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_blueprints(app)
    register_extensions(app)
    register_commands(app)

    return app


def register_blueprints(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)


def register_extensions(app):

    # Flask-SQLAlchemy
    db.init_app(app)

    # Flask-Migrate
    migrate.init_app(app, db)

    # Flask-Login
    login_manager.init_app(app)

    @login_manager.user_loader
    def login_user(user_id):
        return User.query.get(user_id)


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)
