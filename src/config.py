#!/usr/bin/env python
# encoding: utf-8

from handlers import ChatHandler, HomeHandler

__all__ = ['settings', 'routes']

settings = {
    "debug": True,
    "autoreload": True,
    "compiled_template_cache": False,
    "serve_traceback": True
}

routes = [
    (r'/chat/(.*)', ChatHandler),
    (r'/(.*)', HomeHandler, {
        "path": "dist",
        "default_filename": "index.html",
    }),
]

redis_config = {
    "host": "localhost",
    "port": 6379,
    "db": 0
}
