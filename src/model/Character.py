#!/usr/bin/env python
# encoding: utf-8

from uuid import uuid4, UUID
from .db_config import (
    db, Required, PrimaryKey, Optional
)


class Character(db.Entity):

    cid = PrimaryKey(UUID, default=uuid4, auto=True)
    name = Required(str, nullable=False)
    uid = Required(UUID, nullable=True)
    rid = Required(UUID, nullable=False)
    intro = Optional(str, nullable=True)
