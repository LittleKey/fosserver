#!/usr/bin/env python
# encoding: utf-8

from handlers import ChatHandler
from tornado.web import StaticFileHandler

__all__ = ['settings', 'routes']

settings = {
    "debug": True,
    "autoreload": True,
    "compiled_template_cache": False,
    "serve_traceback": True
}

routes = [
    (r'/chat/(.*)', ChatHandler),
    (r'/(.*)', StaticFileHandler, {
        "path": "dist",
        "default_filename": "index.html",
    }),
]
