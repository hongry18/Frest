# -*- coding: utf-8 -*-
from flask import request
from flask_api import status
from flask_restful import Resource

from app.models.user_token_model import token_generate
from app.modules import frest
from app.modules.auth.login import verify_password

_URL = '/auth'


class Auth(Resource):
    @frest.API
    def post(self):
        email = request.form.get('email', None)
        password = request.form.get('password', None)

        if verify_password(email, password):
            _return = {
                'data': token_generate(email=email)
            }
        else:
            _return = {
                'message': 'User does not exist or the password does not match.'
            }

        return _return, status.HTTP_201_CREATED
