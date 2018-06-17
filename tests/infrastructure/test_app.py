#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""
Author: Kevin Murillo Fernández
Email: kevin92dev@gmail.com
Copyright 2018
"""

import unittest
import json
import uuid
from infrastructure.app import app
from domain.model.user.user import User
from domain.model.bank_account.bank_account import BankAccount


class TestApp(unittest.TestCase):

    def setUp(self):
        # creates a test client
        self.app = app.test_client()

        # propagate the exceptions to the test client
        self.app.testing = True

        self.bank_account1 = BankAccount(
            str(uuid.uuid4()),
            'ES0000000000000000',
            2500
        )

        self.bank_account2 = BankAccount(
            str(uuid.uuid4()),
            'ES1111111111111111',
            5000
        )

        self.user = User(
            str(uuid.uuid4()),
            'John',
            'Doe',
            'johndoe',
            '123456',
            [
                self.bank_account1,
                self.bank_account2
            ]
        )

    def read_json(self, json_url):
        f = open(json_url, 'r')
        return json.loads(f.read())

    def test_signup(self):
        json_cart = self.read_json('fixture1.json')
        result = self.app.post('/signup', data=json.dumps(json_cart),
                               content_type='application/json')

        # assert the status code of the response
        self.assertEqual(result.status, True)

        # TODO Now we should check if the new User is really in the DB

    def test_login(self):
        json_cart = self.read_json('fixture1.json')
        result = self.app.post('/login', data=json.dumps(json_cart),
                               content_type='application/json')

        # assert the status code of the response
        self.assertEqual(result.status, True)

        # TODO Now we should check if user is logged

    def test_my_balance(self):
        result = self.app.get('/my_balance', data=None)

        self.assertEqual(result[0].iban, 'ES00000000000000')
        self.assertEqual(result[0].balance, 3000)

    def test_transfer(self):
        json_cart = self.read_json('transfer_fixture.json')
        result = self.app.post('/transfer', data=json.dumps(json_cart),
                               content_type='application/json')

        # assert the status code of the response
        self.assertEqual(result.status, True)

        # TODO Now we should check the balances of both Users