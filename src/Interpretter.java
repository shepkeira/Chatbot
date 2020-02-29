package botPackage;

// this is the only class that is connected with DialogFlow

public class Interpretter {
	
	public static MessageType interpret(String msg) {
		/* feeds string to DialogFlow to determine what the user intends
		 * If DialogFlow decides Intention is a Statement -> return MessageType.Statement
		 * else if Question -> return MessageType.Question
		 * else Other
		 */
		return null;
	}
}
