#!/usr/bin/env python
# encoding: utf-8

from redis import ConnectionPool
from six import with_metaclass
from redis_config import local_config
from utils import Singleton
from room import Room
from client import Client


class Factory(with_metaclass(Singleton, object)):

    def __init__(self):
        self._rooms = {}
        self._clients = {}
        self._connectionPool = ConnectionPool(**local_config)

    def getRoom(self, room_id):
        if room_id is None:
            return None
        room = self._rooms.get(room_id)
        if not room:
            room = Room(room_id, self._connectionPool)
            self._rooms[room_id] = room

        return room

    def getClient(self, client_id):
        if client_id is None:
            return None
        client = self._clients.get(client_id)
        if not client:
            client = Client(client_id)
            self._clients[client_id] = client

        return client

    def getRooms(self):
        return self._rooms.values()

    def getClients(self):
        return self._clients.values()

if __name__ == '__main__':
    pass
