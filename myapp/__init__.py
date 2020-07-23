from flask import Flask

from .routes import main
from .commands import commands
from .extentions import db, migrate


def create_app(config_file='settings.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(main)
    app.register_blueprint(commands)
    
    return app
