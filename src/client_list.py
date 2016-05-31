#!/usr/bin/env python
# encoding: utf-8


class ClientList(list):

    def __init__(self, *args, **kwargs):
        super(ClientList, self).__init__(*args, **kwargs)
