package botPackage;

// This Class sends back our reply to the user

public class Reply {
	Message originalMessage;
	String reply;
	
	public Reply(Message message) {
		this.originalMessage = message;
		this.reply = ReplyGenerator.GenerateReply(this.originalMessage,
				this.originalMessage.keywords);
	}
}
