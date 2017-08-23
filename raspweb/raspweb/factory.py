import os
from flask import Flask, g
from werkzeug.utils import find_modules, import_string
from raspweb.model import init_db


def create_app(config=None):
    app = Flask('raspweb')

    app.config.update(dict(
        DATABASE=os.path.join(app.root_path, 'raspweb.db'),
        DEBUG=True,
        SECRET_KEY=os.urandom(24),
        USERNAME='admin',
        PASSWORD='default',
        ALLOWED_EXTENSIONS=set(['png', 'jpg', 'jpeg', 'gif']),
        UPLOAD_FOLDER='images'
    ))
    app.config.update(config or {})
    app.config.from_envvar('RASPWEB_SETTINGS', silent=True)

    register_blueprints(app)
    register_cli(app)
    register_teardowns(app)

    return app


def register_blueprints(app):
    """Register all blueprint modules."""
    for name in find_modules('raspweb.blueprints'):
        mod = import_string(name)
        if hasattr(mod, 'bp'):
            app.register_blueprint(mod.bp)
    return None


def register_cli(app):
    @app.cli.command('initdb')
    def initdb_command():
        """Creates the database tables."""
        init_db()
        print('Initialized the database.')


def register_teardowns(app):
    @app.teardown_appcontext
    def close_db(error):
        """Closes the database again at the end of the request."""
        if hasattr(g, 'sqlite_db'):
            g.sqlite_db.close()
