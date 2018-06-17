#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""
Author: Kevin Murillo Fernández
Email: kevin92dev@gmail.com
Copyright 2018
"""

from domain.model.user.user import User
from infrastructure.model.repository_base import RepositoryBase


class UserRepository(RepositoryBase):
    def __init__(self, app, db):
        super(UserRepository, self).__init__(db)

    def get_by_username(self, username):
        try:
            return self.session().query(User).filter_by(username=username).first()
        except Exception:
            return None
