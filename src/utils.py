#!/usr/bin/env python
# encoding: utf-8

import threading


__all__ = ['Singleton', 'Thread', 'Runnable', 'ConvertRedisMessage']


class Singleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        #  else:
            #  cls._instances[cls].__init__(*args, **kwargs)

        return cls._instances[cls]


class Thread(threading.Thread):

    def __init__(self, runnable):
        super(Thread, self).__init__()
        self._runnable = runnable
        self._shouldStop = False

    def start(self):
        if isinstance(self._runnable, Runnable):
            self._runnable.shouldStop = self.shouldStop
            super(Thread, self).start()

    def run(self):
        self._runnable.run()

    def stop(self):
        self._shouldStop = True

    def shouldStop(self):
        return self._shouldStop

    def __eq__(self, o):
        return self._runnable == o._runnanle

    def __hash__(self):
        return hash('Thread') + super(Thread, self).__hash__()


class Runnable(object):

    def run(self):
        return NotImplemented

    def shouldStop(self):
        # implement in Thread
        return NotImplemented

    def __hash__(self):
        return NotImplemented


def ConvertRedisMessage(msg):
    if msg is None:
        return None
    if isinstance(msg, int):
        return str(msg)
    elif isinstance(msg, str):
        return msg
    return msg.decode('utf-8')

if __name__ == '__main__':
    pass
