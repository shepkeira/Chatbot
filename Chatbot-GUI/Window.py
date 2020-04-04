import tkinter
from tkinter import *

from main import do_thing

window = tkinter.Tk()
window.resizable(width=True, height=False)
window.title("Azile Chatbot") #displays at the top window bar
scrollbar = Scrollbar(window)
scrollbar.pack(side=RIGHT, fill=Y)
user = StringVar()
bot = StringVar()

num = 0

messages = Text(window, width=120, height=20, yscrollcommand=scrollbar.set, wrap=WORD)
messages.config(borderwidth=5,highlightcolor="LightBlue4",
               background = "LightBlue3", relief=SUNKEN)
scrollbar.config(command=messages.yview())
messages.pack(anchor='nw', expand=1, fill=BOTH)


def Enter_pressed():
    global num
    num = num + 1
    input_get = user.get()
    #print("You: " + input_get)
    messages.insert(END, "You: " + '%s\n' % input_get)
    # label = Label(window, text=input_get)
    bot_get = do_thing(input_get, num)
    #print("Bot: " + bot_get)
    messages.insert(END, "Dr. Azile: " + '%s\n' % bot_get)
    user.set('')
    messages.see(END)
    # label.pack()
    return "break"

def event_enter(key):
    Enter_pressed()


Label(window, text=" user : ").pack(side=LEFT)
Entry(window, textvariable=user, width=10, background="floral white").pack(side=LEFT, anchor='nw', expand=1, fill=BOTH)
frame = Frame(window)  # , width=300, height=300)
Button(window, width=10, text="Send", foreground = "turquoise4", command=Enter_pressed, relief = "raised").pack(side=LEFT)
messages.insert(END, "Dr. Azile: " + '%s\n' % "Say hi to get started")
window.bind("<Return>", event_enter) #here??
frame.pack(anchor='nw', expand=1, fill=BOTH)

window.mainloop()


