#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""
Author: Kevin Murillo Fernández
Email: kevin92dev@gmail.com
Copyright 2018
"""


class BankAccount(object):

    def __init__(self, id, user, iban, balance):
        self.id = id
        self.user = user
        self.iban = iban
        self.balance = balance