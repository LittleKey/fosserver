#!/usr/bin/env python
# encoding: utf-8

from tornado.websocket import WebSocketHandler
from tornado.web import StaticFileHandler
from factory import Factory
import uuid


def GetCurrentClient(handler):
    user_id = handler.get_cookie("user")
    if not user_id and not isinstance(handler, WebSocketHandler):
        user_id = str(uuid.uuid4())
        handler.set_cookie("user", user_id)
    return Factory().getClient(user_id)


class ChatHandler(WebSocketHandler):

    def open(self, room_id):
        print("connection opend...")
        self.room_id = room_id
        client = GetCurrentClient(self)
        client.setProxy(write_message=self.write_message)
        room = Factory().getRoom(self.room_id)
        room.addClient(client)
        self.write_message("connected.")

    def on_message(self, message):
        current_user_id = GetCurrentClient(self).getUserId()
        for client in Factory().getRoom(self.room_id).getClients():
            user_id = client.getUserId()
            if user_id != current_user_id:
                client.write_message("%s: %s" % (user_id, message))
        print("received:", message)

    def on_close(self):
        client = GetCurrentClient(self)
        client.setProxy()  # cancel proxy
        room = Factory().getRoom(self.room_id)
        # TODO : remove client from Factory._clients
        room.removeClient(client)
        print("connection closed...")


class HomeHandler(StaticFileHandler):

    # override
    def set_extra_headers(self, path):
        GetCurrentClient(self)

if __name__ == '__main__':
    pass
