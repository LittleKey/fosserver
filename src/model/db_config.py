#!/usr/bin/env python
# encoding: utf-8

from pony import orm

__all__ = ['db', 'CreateModel']

db = orm.Database()
orm.sql_debug(True)


def CreateModel(name=':memory:'):
    db.bind('sqlite', name, create_db=True)
    db.generate_mapping(create_tables=True)
