import Message
import ReplyGenerator

class Reply:
    def __init__(self, message):
        originalMessage = message
        reply = ReplyGenerator.GenerateReply(originalMessage, originalMessage.keywords)