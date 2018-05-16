import uuid

from flask import jsonify, request
from werkzeug.security import generate_password_hash

from app.db import db, User
from app.helper import Helper

class AuthController:
    
    def register(self):
        if (not request.json) or (not self._required_post_data_are_provided(request.json)):
            output = {            
                "message": "Username or Password field not provided."
            }
            res = jsonify(output)
            res.status_code = 400
            
            return res

        user = User.query.filter_by(username=request.json['username']).first()

        if user:
            output = {            
                "message": "Username already exist."
            }
            res = jsonify(output)
            res.status_code = 409
            
            return res

        hashed_password = generate_password_hash(request.json['password'], method='sha256')
        new_user = User(public_id=str(uuid.uuid4()), username=request.json['username'], password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        output = {            
                "message": "User successfully created."
            }
        res = jsonify(output)
        res.status_code = 201
        
        return res        
        

    def _required_post_data_are_provided(self, data):
        required_strings = ['username', 'password']
        if not Helper.keysExistAndNotEmptyString(required_strings, data):
            return False
        
        return True