package botPackage;

// this is the only class that is directly connected to DialogFlow

/* INTERPRETTER CLASS IS FOR OBTAINING INFORMATION
 *	- this would help the following interaction
 *
 * Input: String msg
 * 		+ EX: "I feel like running away"
 *  - keywords identified
 *  - keywords transformed ("I" -> "you")
 *  - keywords get slotted into a script 
 *  	+ EX: "Why do ___[@Pronoun] ______[@Verb] _____[excess]"
 *  - transformed keywords get slotted into script
 *  	+ EX: "Why do you feel like running away"
 *  Output: String reply
 *  	+ EX: "Why do you feel like running away"
 */

public class Interpretter {
	
	public static void process(Message message) {
		
		if (checkForX(message.msg, "PHRASE/ WORD TO CHECK FOR")) {
			// do ______ instead of generating a reply from a script
			// 	 - example of when to do this would be messages regarding serious topics
			// 		+ could be used for greetings as well :)
		}
		
		message.type = Interpretter.interpretType(message.msg);
		message.keywords = Interpretter.getKeywords(message.msg);
		
	}
	
	private static MessageType interpretType(String msg) {
		/* feeds string to DialogFlow to determine what the user intends
		 * 		If DialogFlow decides Intention is a Statement -> return MessageType.Statement
		 * 		else if Question -> return MessageType.Question
		 * 		else return Other
		 */
		return null;
	}

	private static String[] getKeywords(String msg) {
		// returns a list of the Key Entities of a sentence (Pronounds and Verbs)
		
		/* EXAMPLE
		 * Input: "I feel like running away"
		 * 	 - Keywords: I [@Pronoun], feel [@Verb] 
		 * 			+ these keywords get identified by DialogFlow
		 * 			+ if feasable, then we can store "like running away" to be used in possible response
		 * 
		 */
		return null;
		
	}
	
	private static boolean checkForX (String msg, String x) {
		// here we could check if the string x is present in the message
		
		return msg.contains(x); // x could be phrases that indicate self harm
	}

}
