import os
import tempfile

import pytest
from app import create_app
from app.db import db

@pytest.fixture
def app():    

    db_fd, db_path = tempfile.mkstemp()    
    
    app = create_app({
        'TESTING': True,        
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///{}'.format(db_path),
        'SQLALCHEMY_TRACK_MODIFICATIONS': False
    })            
    
    db.create_all()
    
    yield app    

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()