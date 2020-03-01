package botPackage;

public class Script {
	String script; // Script is a string with blanks to be filled in by keywords
		// Example Script: "Why do @Pronoun @Verb @Excess"
		// @ symbol is an entity that needs to be filled in from keyword list
		// ALTERNATIVELY, we can replace the @Pronoun with a number that indicates the equivalent
		//  - Example: "Why do 1 2 0", where 1 indicates @Pronoun, 2 = @Verb, 0 = @Excess
	public Script(String script) {
		this.script = script;
	}
		
}
