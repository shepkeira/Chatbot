import Interpreter
import MessageType

class Message:
    msg = ""
    keywords = []
    msgType = MessageType.Other

    def __init__(self, msg):
        msg = msg
        Interpreter.process(self)