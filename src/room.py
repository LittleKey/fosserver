#!/usr/bin/env python
# encoding: utf-8

from redis import Redis
from utils import Thread


class Room(object):

    def __init__(self, room_id, connection_pool):
        self._room_id = room_id
        self._threads = dict()
        self._redis = Redis(connection_pool=connection_pool)

    def addClient(self, client):
        client.subscribe(self._redis, self._room_id, '_kill')
        thread = Thread(client)
        self._threads[client.getUserId()] = thread
        thread.start()

    def removeClient(self, client):
        user_id = client.getUserId()
        thread = self._threads.pop(user_id, None)
        if thread:
            thread.stop()
            self.kill(user_id)

    def kill(self, user_id):
        self._redis.publish('_kill', user_id)

    def publish(self, message):
        self._redis.publish(self._room_id, message)

if __name__ == '__main__':
    pass
