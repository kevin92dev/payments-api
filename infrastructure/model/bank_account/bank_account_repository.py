#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""
Author: Kevin Murillo Fernández
Email: kevin92dev@gmail.com
Copyright 2018
"""

from domain.model.bank_account.bank_account import BankAccount
from infrastructure.model.repository_base import RepositoryBase


class BankAccountRepository(RepositoryBase):
    def __init__(self, app, db):
        super(BankAccountRepository, self).__init__(db)

    def get_by_user(self, user):
        try:
            return self.session().query(BankAccount).filter_by(user=user).all()
        except Exception:
            return None
