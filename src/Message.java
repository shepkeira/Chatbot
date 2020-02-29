package botPackage;

public class Message {
	String msg;
	MessageType type; // gets decided by interpretter [DialogFlow]
	// may need to be broken up into their DialogFlow entities (verbs and pronouns)
	String[] keywords; 
	
	public Message(String msg) {
		this.msg = msg;
		this.type = Interpretter.interpretType(msg);
		this.keywords = Interpretter.getKeywords(msg);
	}
}
