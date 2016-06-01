#!/usr/bin/env python
# encoding: utf-8


class Client(object):

    def __init__(self, user_id, **kwargs):
        self._user_id = user_id
        self._proxy = kwargs

    def getUserId(self):
        return self._user_id

    def setProxy(self, **kwargs):
        self._proxy = kwargs

    def __getattr__(self, name):
        proxy_func = self._proxy.get(name)
        if proxy_func:
            return proxy_func
        return super(Client, self).__getattribute__(name)

    def __eq__(self, o):
        return self._user_id == o._user_id

    def __hash__(self):
        return hash(self._user_id)

if __name__ == '__main__':
    pass
