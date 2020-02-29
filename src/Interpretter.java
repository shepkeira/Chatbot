package botPackage;

// this is the only class that is connected with DialogFlow

public class Interpretter {
	
	public static MessageType interpretType(String msg) {
		/* feeds string to DialogFlow to determine what the user intends
		 * If DialogFlow decides Intention is a Statement -> return MessageType.Statement
		 * else if Question -> return MessageType.Question
		 * else Other
		 */
		return null;
	}

	public static String[] getKeywords(String msg) {
		// returns a list of the Key Entities of a sentence (Pronounds and Verbs)
		
		/* EXAMPLE
		 * Input: "I feel like running away"
		 * 	 - Keywords: I [@Pronoun], feel [@Verb] 
		 * 			+ these keywords get identified by DialogFlow
		 * 			+ if feasable, then we can store "like running away" to be used in possible response
		 * 
		 */
		return null;
		
		/* END GOAL OF OBTAINING THESE KEY WORDS
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
	}
	
	public static boolean checkForX (String msg, String x) {
		// here we could check if the string x is present in the message
		
		return msg.contains(x); // x could be phrases that indicate self harm
	}
}
