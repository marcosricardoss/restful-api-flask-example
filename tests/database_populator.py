
import uuid

from werkzeug.security import generate_password_hash

from app.db import db
from app.db import User

class DatabasePopulator:

    def create_user(username, password, admin):
        hashed_password = generate_password_hash(password, method='sha256')
        user = User(public_id=str(uuid.uuid4()), username=username, password=hashed_password, admin=admin)
        db.session.add(user)
        db.session.commit()

        #return user

    @staticmethod
    def populate():
        user1 = DatabasePopulator.create_user("tester1", "secret", False)
        user2 = DatabasePopulator.create_user("tester2", "secret", False)
        admin1 = DatabasePopulator.create_user("admin1", "secret", True)