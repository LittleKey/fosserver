#!/usr/bin/env python
# encoding: utf-8

from uuid import uuid4, UUID
from .db_config import (
    db, Required, PrimaryKey, Optional
)


class User(db.Entity):

    uid = PrimaryKey(UUID, default=uuid4)
    email = Required(str, unique=True, nullable=False)
    name = Required(str, unique=True, nullable=False)
    password = Required(str, unique=True, nullable=False)
    avatar = Optional(str, nullable=True)
