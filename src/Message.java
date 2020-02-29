package botPackage;

public class Message {
	String msg;
	MessageType type; // gets decided by interpretter [DialogFlow]
	
	public Message(String msg) {
		this.msg = msg;
		this.type = Interpretter.interpret(msg);
	}
}
