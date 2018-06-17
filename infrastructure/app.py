#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""
Author: Kevin Murillo Fernández
Email: kevin92dev@gmail.com
Copyright 2018
"""

from flask import Flask, request, jsonify
from domain.model.user.user import User
from domain.model.bank_account.bank_account import BankAccount
from application.context import SQLContext
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/payments.db'
app.secret_key = "123456789abcdefghijk"

Context = SQLContext(app)
Context.setup()

response = {'status': True, 'error_message': ''}


@app.route('/signup', methods=['POST'])
def signup():
    try:
        user_data = request.get_json(force=True)

        new_bank_account = BankAccount(
            str(uuid.uuid4()),
            user_data['bank_account']['iban'],
            user_data['bank_account']['balance']
        )

        new_user = User(
            str(uuid.uuid4()),
            user_data['firstname'],
            user_data['lastname'],
            user_data['username'],
            user_data['password'],
            [new_bank_account]
        )

        Context.bank_account_repository.create(new_bank_account)
        Context.user_repository.create(new_user)

        return jsonify(response)
    except Exception as e:
        response['status'] = False
        response['error_message'] = str(e)

        return jsonify(response)


@app.route('/login', methods=['POST'])
def login():
    try:
        user_data = request.get_json(force=True)

        user = Context.user_repository.get_by_username(user_data['username'])

        if user is not None:
            if user_data['password'] == user.password:
                Context.authentication_service.login_user(user)
            else:
                print('Wrong password')
        else:
            print('Username not found.')

        return jsonify(response)
    except Exception as e:
        response['status'] = False
        response['error_message'] = str(e)

        return jsonify(response)


@app.route('/logout', methods=['GET'])
def logout():
    try:
        Context.authentication_service.logout_current_user()
        return jsonify(response)
    except Exception as e:
        response['status'] = False
        response['error_message'] = str(e)

        return jsonify(response)


@app.route('/my_balance', methods=['GET'])
@Context.authentication_service.login_required
def my_balance():
    user = Context.authentication_service.get_current_user()

    try:
        return jsonify(user.get_balances())
    except Exception as e:
        response['status'] = False
        response['error_message'] = str(e)

        return jsonify(response)


@app.route('/transfer', methods=['POST'])
@Context.authentication_service.login_required
def transfer():
    user = Context.authentication_service.get_current_user()

    try:
        request_data = request.get_json(force=True)

        receiver_user = Context.user_repository.\
            get_by_username(request_data['username'])

        Context.transfer_service.\
            do_transfer(user, receiver_user, request_data['amount'])

        return jsonify(user.get_balances())
    except Exception as e:
        response['status'] = False
        response['error_message'] = str(e)

        return jsonify(response)