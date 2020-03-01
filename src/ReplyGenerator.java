package botPackage;

import java.io.File;

// Methods to create a reply that continues basic basic conversation

/*
 *  REASON FOR NOT USING DIALOGFLOW TO DIRECTLY GENERATE REPLIES: 
 *  We are not using DialogFlow to directly generate replies because dialog flow is
 *  designed to be an interpretter with usually hardcoded non-flexible replies. 
 *  Meaning DialogFlow is not made to create conversation 
 *  but rather to determine what a user has said
 *  and pick out the details we want from that information. 
 *  
 *  In short, we are using DialogFlow to tell us what method to run
 *  and what keywords to put into our scripts. 
 */

public class ReplyGenerator {
	
	// scripts the bot will be used to help generate replies
	final private static ScriptList otherScripts = new ScriptList(new File("OtherScripts.txt"));
	final private static ScriptList questionScripts = new ScriptList(new File("QuestionScripts.txt"));
	final private static ScriptList statementScripts = new ScriptList(new File("StatementScripts.txt"));
		// note that none of these scripts have been written yet.
		// we also need to decide on how we want to write them so we can develop methods to use them
	
	
	public static String GenerateReply (Message message, String[] keywords) {
		// keywords will likely need to be broken into two arrays: Verbs and Pronouns
		// and, ideally, we take the excess and use it in a way that echos properly
		//  - Note that this echo is what makes the conversation much more believable
		switch(message.type) {
			default: 
				return GenerateOtherReply(message, keywords);
			case Statement: 
				return GenerateStatementReply(message, keywords);
			case Question: 
				return GenerateQuestionReply(message, keywords);
		}
	}

	// Used in cases where the Bot can't decipher what the user is saying
	//  - My thought is we keep a list of questions to ask the user when this happens
	// 		+ possibly make a memory class like the one in ELIZA
	private static String GenerateOtherReply(Message message, String[] keywords) {
		return null;
	}

	// Used when the user asks the bot a question
	private static String GenerateQuestionReply(Message message, String[] keywords) {
		// TODO Auto-generated method stub
		return null;
	}

	// Used when the user makes a statement that follows the form: @Pronoun @Verb @Excess
	private static String GenerateStatementReply(Message message, String[] keywords) {
		// TODO Auto-generated method stub
		return null;
	}
}
