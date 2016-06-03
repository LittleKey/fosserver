#!/usr/bin/env python

from tornado.ioloop import IOLoop
from tornado.web import Application
from config import settings, routes
import model


def main():
    application = Application(routes, **settings)
    application.listen(8000)
    model.CreateModel('test.db')
    IOLoop.instance().start()

if __name__ == "__main__":
    main()
