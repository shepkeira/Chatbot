import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

class Main {
    static List<String> GREETINGS = new ArrayList<String>() {{
        add("hello");
        add("hi");
    } };

    static List<String> FARWELLS = new ArrayList<String>() {{
        add("bye");
        add("goodbye");
        add("farwall");
    } };

    static List<String> WARNINGS = new ArrayList<String>() {{
        add("suicide");
        add("harm myself");
        add("self harm");
        add("kill myself");
    } };
    static Scanner input = new Scanner(System.in);

    public static void main(String[] args) {
        boolean done = false;

        System.out.println("Hello, my name is Dr. Azile, I am here to help with your psychological needs. " );
        System.out.println("Please know that I am not a real person; I am a chat bot, created by some amazing people to help you. ");
        System.out.println("If you need a real person or I feel you need someone real I can give you resources like a helpline number.");

        while(!done) {
            System.out.print("You: ");
            String myString = input.nextLine();

            String response_greeting = check_for_greeting(myString);
            String response_harm = check_for_get_help(myString);
            String response_bye = check_for_get_farwell(myString);
            if (!response_harm.equals("")) {
                helplines(response_harm);
            } else if (!response_greeting.equals("")) {
                System.out.println("Dr.Azile: " + response_greeting);
            } else if (!response_bye.equals("")) {
                System.out.println("Dr.Azile: " + response_bye);
                done = true;
            } else {
                System.out.println("Dr.Azile: I'm sorry but I don't understand");
            }
        }


    }

    private static String check_for_get_farwell(String myString) {
        String respond = "";
        myString = myString.toLowerCase();
        for(int i = 0; i < FARWELLS.size(); i++) {
            if(myString.contains(FARWELLS.get(i))) {
                int rand = generateRandomIntIntRange(0, FARWELLS.size() - 1);
                respond = FARWELLS.get(rand);
            }
        }

        return respond;
    }

    private static void helplines(String response_harm) {
        System.out.println("Dr. Azile: " + response_harm);
        System.out.println("If your life is in danger or you know someone’s life is in danger DIAL EMERGENCY NOW (often 911 in your area)  DO NOT HESITATE!");
        System.out.println("Or go to your nearest hospital.");
        System.out.println("If you are between the ages of 5 and 20");
        System.out.println("Kids help phone number: 1-800-668-6868");
        System.out.println("If you would like kids help phone also have online chat if you would prefer");
        System.out.println("Crisis Text Line: text HOME to 686868 in Canada");
        System.out.println("Hope for Wellness help line gives free national telephone crisis intervention and counselling support for First Nations and Inuit.");
        System.out.println("Hope for Wellness: 855-242-3310");
        System.out.println("For a list of international hot lines visit https://ibpf.org/resource/list-international-suicide-hotlines");

    }

    private static String check_for_get_help(String myString) {
        String respond = "";
        myString = myString.toLowerCase();
        for(int i = 0; i < WARNINGS.size(); i++) {
            if(myString.contains(WARNINGS.get(i))) {
                respond = "Here are some help lines I think you should contact";
            }
        }

        return respond;
    }

    private static String check_for_greeting(String myString) {
        String respond = "";
        myString = myString.toLowerCase();
        for(int i = 0; i < GREETINGS.size(); i++) {
            if(myString.contains(GREETINGS.get(i))) {
                int rand = generateRandomIntIntRange(0, GREETINGS.size() - 1);
                respond = GREETINGS.get(rand);
            }
        }

        return respond;
    }

    public static int generateRandomIntIntRange(int min, int max) {
        Random r = new Random();
        return r.nextInt((max - min) + 1) + min;
    }
}

/*
# Sentences we'll respond with if the user greeted us
GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up",)

GREETING_RESPONSES = ["'sup bro", "hey", "*nods*", "hey you get my snap?"]

def check_for_greeting(sentence):
    """If any of the words in the user's input was a greeting, return a greeting response"""
    for word in sentence.words:
        if word.lower() in GREETING_KEYWORDS:
            return random.choice(GREETING_RESPONSES)
            
        	On-boarding complete
 */