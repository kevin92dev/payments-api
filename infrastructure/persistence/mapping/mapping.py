#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""
Author: Kevin Murillo Fernández
Email: kevin92dev@gmail.com
Copyright 2018
"""

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import relationship
from domain.model.user.user import User
from domain.model.bank_account.bank_account import BankAccount


def init(db):
    user_mapping = db.Table('user',
        db.Column('id', String(36), primary_key=True),
        db.Column('firstname', String(50)),
        db.Column('lastname', String(50)),
        db.Column('username', String(50), unique=True),
        db.Column('password', String(100))
    )

    bank_account_mapping = db.Table('bank_account',
        db.Column('id', String(36), primary_key=True),
        db.Column('iban', String(50)),
        db.Column('balance', String(10), unique=True),
        db.Column('user', String(36), ForeignKey("user.id"), nullable=False),
    )

    db.mapper(BankAccount, bank_account_mapping)
    db.mapper(User, user_mapping, properties={
        'bank_accounts': relationship(
            BankAccount,
            backref='user_id',
            lazy=True
        )
    })