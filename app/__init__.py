import os

from flask import Flask

from app.db import db
from app.blueprints import auth
from app.handler import register_handlers

def create_app(test_config=None):
    
    '''Create and configure the app.'''
    
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',        
        SQLALCHEMY_DATABASE_URI='sqlite:///{}/database.sqlite3'.format(app.instance_path),
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )
    
    # push an application to Flask Sqlalchemy
    app.app_context().push()
    
    # initializing the database
    db.init_app(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
        db.create_all()
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)    

    # ensure the instance folder exists
    create_instance_folder(app)    
    
    # creating the base routes of the application
    create_routes(app)

    # registering the blueprint to application
    app.register_blueprint(auth.bp)
    
    # attaching the custom handlers
    register_handlers(app)

    return app


def create_instance_folder(app):

    '''Create the instance folder.'''

    try: 
        os.makedirs(app.instance_path)
    except OSError: 
        pass


def create_routes(app):    

    '''Create the route bases of the application'''

    @app.route('/')
    def home():return 'Flask Restful API'       