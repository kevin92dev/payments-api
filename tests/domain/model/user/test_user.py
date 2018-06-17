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
from domain.model.user.user import User
from domain.model.bank_account.bank_account import BankAccount


class TestUser(unittest.TestCase):

    def setUp(self):
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

    def test_get_default_bank_account(self):
        self.assertEqual(
            self.user.get_default_bank_account(),
            self.bank_account1
        )

    def test_get_balances(self):
        data = [
            {'iban': 'ES0000000000000000', 'balance': 2500},
            {'iban': 'ES1111111111111111', 'balance': 5000}
        ]

        json_balances = json.dumps(data)

        self.assertEqual(
            json.dumps(self.user.get_balances()),
            json_balances
        )
