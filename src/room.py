#!/usr/bin/env python
# encoding: utf-8


class Room(object):

    def __init__(self, room_id):
        self._room_id = room_id
        self._clients = set()

    def addClient(self, client):
        self._clients.add(client)

    def removeClient(self, client):
        if client in self._clients:
            self._clients.remove(client)

    def getClients(self):
        return list(self._clients)

if __name__ == '__main__':
    pass
