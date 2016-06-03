#!/usr/bin/env python
# encoding: utf-8

from uuid import uuid4, UUID
from .db_config import (
    db, Required, PrimaryKey, Optional
)


class Room(db.Entity):

    rid = PrimaryKey(UUID, default=uuid4, auto=True)
    name = Required(str, unique=True, nullable=False)
    story = Optional(str, nullable=True)
