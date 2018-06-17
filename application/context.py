#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""
Author: Kevin Murillo Fernández
Email: kevin92dev@gmail.com
Copyright 2018
"""

from flask_sqlalchemy import SQLAlchemy
from infrastructure.persistence.mapping import mapping
from infrastructure.model.user.user_repository import UserRepository
from infrastructure.model.bank_account.bank_account_repository \
    import BankAccountRepository
from application.service.authentication_service import AuthenticationService
from application.service.transfer_service import TransferService


class SQLContext(object):

    def __init__(self, app):
        db = SQLAlchemy(app)
        mapping.init(db)

        self.db = db

        self.user_repository = UserRepository(app, db)
        self.bank_account_repository = BankAccountRepository(app, db)
        self.authentication_service = \
            AuthenticationService(app, self.user_repository)
        self.transfer_service = TransferService(db)

    def setup(self):
        self.db.create_all()