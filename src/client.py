#!/usr/bin/env python
# encoding: utf-8

from utils import Runnable, ConvertRedisMessage


class Client(Runnable):

    def __init__(self, user_id):
        super(Client, self).__init__()
        self._user_id = user_id
        self._pubsub = None
        self._sender = None

    def getUserId(self):
        return self._user_id

    def setSender(self, sender):
        self._sender = sender

    def subscribe(self, redis, *args):
        self._pubsub = redis.pubsub()
        self._pubsub.subscribe(args)

    def unsubscribe(self):
        self._pubsub.unsubscribe()
        print(self, "unsubscribed and finished")

    def process(self, channel, data):
        if channel == '_kill':
            if data == self._user_id:
                self.unsubscribe()
            return
        try:
            if self._sender:
                self._sender(data)
        except AttributeError:
            pass

    def run(self):
        for item in self._pubsub.listen():
            if self.shouldStop():
                self.unsubscribe()
                break
            msg_type = ConvertRedisMessage(item['type'])
            data = ConvertRedisMessage(item['data'])
            channel = ConvertRedisMessage(item['channel'])
            if msg_type == 'message':
                self.process(channel, data)

    def __eq__(self, o):
        return self._user_id == o._user_id

    def __hash__(self):
        return hash(self._user_id)

if __name__ == '__main__':
    pass
