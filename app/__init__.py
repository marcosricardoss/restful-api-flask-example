import os
import app.handler as handler

from flask import Flask

from app.db import db
from app.blueprints import auth

def create_app(test_config=None):
    
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',        
        SQLALCHEMY_DATABASE_URI='sqlite:///{}/database.sqlite3'.format(app.instance_path),
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )
    
    # initializing the database
    app.app_context().push()
    db.init_app(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
        db.create_all()
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)    

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple home page
    @app.route('/')
    def home():
        return 'Flask Restful API'       
    
    app.register_blueprint(auth.bp)
    handler.handlers(app)

    return app
    