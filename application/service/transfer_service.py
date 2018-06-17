#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""
Author: Kevin Murillo Fernández
Email: kevin92dev@gmail.com
Copyright 2018
"""


class TransferService(object):
    def __init__(self, db):
        self.db = db

    def do_transfer(self, transmitter_user, receiver_user, amount):
        try:
            transmitter_account = transmitter_user.get_default_bank_account()
            receiver_account = receiver_user.get_default_bank_account()

            if self.check_constraints(transmitter_account, amount):
                transmitter_balance = transmitter_account.balance
                transmitter_balance = transmitter_balance - amount

                receiver_balance = receiver_account.balance
                receiver_balance = receiver_balance + amount

                transmitter_account.balance = transmitter_balance
                receiver_account.balance = receiver_balance

                self.db.session.commit()
            else:
                print('Transfer error: Insufficient balance.')
        except Exception as e:
            raise e

    def check_constraints(self, transmitter_account, amount):
        if amount > transmitter_account.balance:
            return False

        return True
