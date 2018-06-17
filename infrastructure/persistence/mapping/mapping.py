#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""
Author: Kevin Murillo Fernández
Email: kevin92dev@gmail.com
Copyright 2018
"""

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from domain.model.user.user import User
from domain.model.bank_account.bank_account import BankAccount


def init(db):
    user_mapping = db.Table('user',
        db.Column('id', Integer, primary_key=True),
        db.Column('firstname', String(50)),
        db.Column('lastname', String(50)),
        db.Column('username', String(50)),
        db.Column('email', String(100)),
        db.Column('password', String(100))
    )

    bank_account_mapping = db.Table('bank_account',
        db.Column('id', Integer, primary_key=True),
        db.Column('iban', String(50)),
        db.Column('balance', Integer),
        db.Column('user',
                  String(50),
                  ForeignKey(
                      "user.id",
                      onupdate="CASCADE",
                      ondelete="CASCADE"
                  ),
                  nullable=False
                  ),
    )

    db.mapper(User, user_mapping, properties={
        'bank_accounts': relationship(
            BankAccount,
            backref='user'
        )
    })

    db.mapper(BankAccount, bank_account_mapping)

    db.mapper(User, user_mapping, properties={
        'bank_accounts': relationship(
            BankAccount,
            backref='user'
        )
    })