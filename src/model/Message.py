#!/usr/bin/env python
# encoding: utf-8

from uuid import uuid4, UUID
from .db_config import (
    db, Required, PrimaryKey
)

Type = {
    "message": 0,
    "notify": 1,
}


class Message(db.Entity):

    mid = PrimaryKey(UUID, default=uuid4, auto=True)
    uid = Required(UUID, nullable=False)
    content = Required(str, nullable=False)
    msg_type = Required(int, nullable=False, default=Type["notify"])
