# coding: utf-8

from blinker import signal


msg_signal = signal('msg_signal')  # same signal...


class FromHttpToSocketio(object):

    def __init__(self, name):
        self.name = name

    def send(self):
        msg_signal = signal('msg_signal')
        msg_signal.send(self)  # I can get msg use self.msg from socketio register function:)

    def __repr__(self):
        return '<FromHttpToSocketio Message: %r>' % self.name
