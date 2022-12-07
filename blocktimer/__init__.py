import os

from flask import Flask


def create_app(test_config=None):
    # Create and configure app.
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'timer.sqlite'),
    )

    if test_config is None:
        # Load the instance configuration, if it exists, when not testing.
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test configuration if passed in.
        app.config.from_mapping(test_config)

    # Ensure instance folder exists.
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from blocktimer import db
    db.init_app(app)

    from blocktimer import auth, entry, timer

    app.register_blueprint(auth.bp)

    app.register_blueprint(timer.bp)

    app.register_blueprint(entry.bp)

    app.add_url_rule('/', endpoint='index')

    return app
