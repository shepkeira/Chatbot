import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

class Main {
    static List<String> GREETINGS = new ArrayList<String>() {{
        add("hello");
        add("hi");
    } };

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.print("You: ");
        String myString = input.next();

        String response = check_for_greeting(myString);
        if (!response.equals("")) {
            System.out.println("Dr.Azile: " + response);
        } else {
            System.out.println("Dr.Azile: I'm sorry but I don't understand");
        }


    }

    private static String check_for_greeting(String myString) {
        String respond = "";
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
 */