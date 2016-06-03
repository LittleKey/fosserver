#!/usr/bin/env python
# encoding: utf-8

from pony.orm import (
    Database, sql_debug, db_session,
    PrimaryKey, Required, Optional
)

__all__ = [
    'db', 'CreateModel', 'PrimaryKey', 'Required', 'Optional', 'db_session'
]

db = Database()
sql_debug(True)


def CreateModel(name=':memory:'):
    db.bind('sqlite', name, create_db=True)
    db.generate_mapping(create_tables=True)
