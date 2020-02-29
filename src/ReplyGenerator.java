package botPackage;

// Methods to create a reply that continues basic basic conversation

// REASON FOR NOT USING DIALOGFLOW TO GENERATE REPLIES: We are not using DialogFlow to
// generate replies because dialog flow is designed to be an interpretter 
// with usually hardcoded non-flexible replies. Meaning DialogFlow is not
// made to create conversation but rather determine what a user has said
// and pick out the details we want from that information. 
// In essence, we are using DialogFlow to determine what has been said and what the 
// information we are looking for is in what the user sent. 

public class ReplyGenerator {
	
	public static Reply GenerateReply (Message message) {
		switch(message.type) {
			default: 
				return GenerateOtherReply(message);
			case Statement: 
				return GenerateStatementReply(message);
			case Question: 
				return GenerateQuestionReply(message);
		}
	}

	private static Reply GenerateOtherReply(Message message) {
		// TODO Auto-generated method stub
		return null;
	}

	private static Reply GenerateQuestionReply(Message message) {
		// TODO Auto-generated method stub
		return null;
	}

	private static Reply GenerateStatementReply(Message message) {
		// TODO Auto-generated method stub
		return null;
	}
}
