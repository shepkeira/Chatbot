import ScriptList
import MessageType

class ReplyGenerator:
    otherScripts = ScriptList.ScriptList("OtherScripts.txt")
    questionScripts = ScriptList.ScriptList("QuestionScripts.txt")
    statementScripts = ScriptList.ScriptList("StatementScripts.txt")

    def GenerateReply(self, message, keywords):
        if message.msgType == MessageType.Statement:
            return self.GenerateStatementReply(message, keywords)
        elif message.msgType == MessageType.Question:
            return self.GenerateQuestionReply(message, keywords)
        else:
            return self.GenerateOtherReply(message, keywords)

    def GenerateStatementReply(self, message, keywords):
        return ""
    def GenerateQuestionReply(self, message, keywords):
        return ""
    def GenerateOtherReply(self, message, keywords):
        return ""