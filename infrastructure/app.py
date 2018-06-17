#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""
Author: Kevin Murillo Fernández
Email: kevin92dev@gmail.com
Copyright 2018
"""

from flask import Flask, request
from domain.model.user.user import User

app = Flask(__name__)
#app.config.from_envvar("BLOGEX_SETTINGS_MODULE")
Context = app.config["SQLContext"](app)

response = {'status': True, 'error_message': ''}


@app.route('/signup', methods=['POST'])
def signup():
    try:
        user_data = request.get_json(force=True)

        new_user = User(
            user_data['firstname'],
            user_data['lastname'],
            user_data['username'],
            user_data['password']
        )

        Context.user_repository.create(new_user)

        return response
    except Exception as e:
        response['status'] = False
        response['error_message'] = e

        return response


@app.route('/login', methods=['POST'])
def login():
    try:
        user_data = request.get_json(force=True)

        user = User(
            username=user_data['username'],
            password=user_data['password']
        )
        Context.authentication_service.login_user(user)

        return response
    except Exception as e:
        response['status'] = False
        response['error_message'] = e

        return response


@app.route('/logout', methods=['GET'])
def logout():
    try:
        Context.authentication_service.logout_current_user()
        return response
    except Exception as e:
        response['status'] = False
        response['error_message'] = e

        return response
