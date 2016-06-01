#!/usr/bin/env python
# encoding: utf-8


__all__ = ['Singleton']


class Singleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        #  else:
            #  cls._instances[cls].__init__(*args, **kwargs)

        return cls._instances[cls]

if __name__ == '__main__':
    pass
