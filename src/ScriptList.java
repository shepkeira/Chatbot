package botPackage;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

// List that holds prewritten scripts we create

public class ScriptList {
	// array list to holds list of scripts
	private ArrayList<Script> scripts = new ArrayList<Script>();
	
	public ScriptList(File file) {
		importScripts(file);
	}

	private void importScripts(File file) { 
		// For Example: file = QuestionScripts.txt 
		// Scanner grabs all the scripts from said text file
		try(Scanner in = new Scanner(file);) {
			// read list of scripts from a test file
			while (in.hasNext()){
				String script = in.nextLine();
				scripts.add(new Script(script));
				}
			
		} catch (FileNotFoundException e) {
			System.out.println("File not found D:");
			e.printStackTrace();
		}
		
	}
	
}
