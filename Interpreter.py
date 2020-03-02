class Interpreter:
    def process(self, message):
        if self.checkForX(message.msg, "PHRASE/WORD TO CHECK FOR"):
            print("yes") #delete later
            #do ____ instead of generating a reply from a script
            # -exampe of when to do this would be messages regarding serious topics
            # + could be used for greetings as well :)
        # if ToneBot identifies Tone: Message.reply = ToneBots reply
        
        
            
        message.msgType = Interpreter.interpreterType(message.msg);
        message.keywords = self.getKeywords(message.msg);

    def getKeywords(self, msg):
        #retuns a list of the Key Entities of a sentence (Pronouns and Verbs)
        return ["key", "words"]

    def checkForX (self, msg, x):
        #here we could check if the string x is present in the message

        return msg.contains(x)

