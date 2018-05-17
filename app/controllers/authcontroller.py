import uuid

from flask import jsonify, request
from werkzeug.security import generate_password_hash

from app.db import db, User
from app.helper import Helper

class AuthController:
    
    def register(self):
        
        # checking data request
        if (not request.json) or (not self._required_post_data_are_provided(request.json)):
            output = {            
                "message": "Username or Password field not provided."
            }
            res = jsonify(output)
            res.status_code = 400
            
            return res

        user = User.query.filter_by(username=request.json['username']).first()

        # checking if username already exist
        if user:
            output = {            
                "message": "Username already exist."
            }
            res = jsonify(output)
            res.status_code = 409
            
            return res
        
        self._save(request.json)

        output = {            
                "message": "User successfully created."
            }
        res = jsonify(output)
        res.status_code = 201
        
        return res        


    def _save(self, data):
        
        data['public_id'] = str(uuid.uuid4())
        
        if "password" in data:
            data['password'] = generate_password_hash(data['password'], method='sha256')
        
        if ("admin" in data) and (data['admin'].lower()=="true"):
            data['admin'] = True
        else:
            data['admin'] = False
        
        user = User(**data)
        db.session.add(user)
        db.session.commit()
        
        return user


    def _required_post_data_are_provided(self, data):
        required_strings = ['username', 'password']
        if not Helper.keysExistAndNotEmptyString(required_strings, data):
            return False
        
        return True