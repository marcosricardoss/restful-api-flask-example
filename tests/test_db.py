from app.db import db

def test_user_table_created(app):
    result = db.engine.execute('SELECT null FROM user LIMIT 1')
    assert result