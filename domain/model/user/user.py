#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""
Author: Kevin Murillo Fernández
Email: kevin92dev@gmail.com
Copyright 2018
"""


class User(object):

    def __init__(self,
                 id,
                 firstname,
                 lastname,
                 username,
                 password,
                 bank_accounts
                 ):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.bank_accounts = bank_accounts

    def get_default_bank_account(self):
        return self.bank_accounts[0]

    def get_balances(self):
        balances = []

        for bank_account in self.bank_accounts:
            balances.append(
                {'iban': bank_account.iban, 'balance': bank_account.balance}
            )

        return balances

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id
