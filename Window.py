from tkinter import *

from main import do_thing

window = Tk()
scrollbar = Scrollbar(window)
scrollbar.pack(side=RIGHT, fill=Y)
user = StringVar()
bot = StringVar()

num = 0

messages = Text(window, width=50, height=20, yscrollcommand=scrollbar.set)
scrollbar.config(command=messages.yview())
messages.pack()


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


Label(window, text=" user : ").pack(side=LEFT)
Entry(window, textvariable=user, width=35).pack(side=LEFT)
frame = Frame(window)  # , width=300, height=300)
Button(window, text="speak", command=Enter_pressed).pack(side=LEFT)
messages.insert(END, "Dr. Azile: " + '%s\n' % "Say hi to get started")
#input_field.bind("<Return>", Enter_pressed) #here??
frame.pack()

window.mainloop()


