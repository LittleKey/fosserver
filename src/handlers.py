#!/usr/bin/env python
# encoding: utf-8

from tornado.websocket import WebSocketHandler
import client_list

clients = client_list.ClientList()


class ChatHandler(WebSocketHandler):

    def open(self, room_id):
        print("connection opend...")
        self.room_id = room_id
        clients.append(self)
        self.write_message("connected.")

    def on_message(self, message):
        for client in clients:
            client.write_message("%s: %s" % (self.room_id, message))
        print("received:", message)

    def on_close(self):
        clients.remove(self)
        print("connection closed...")

