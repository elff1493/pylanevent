import main2
from main2 import *
from threading import Thread

def send():
    while True:

        inp = input("guess")
        if inp:
            c.send(guess, str=inp)

if __name__ == "__main__":
    guess = Structure("guess",
                           str=str
                           )

    guessed = Structure("guessed",
                             guess=UInt1Type,
                             word=str,
                             who=str
                             )
    end = Structure("end",
                         win=bool,
                         winner=str
                         )

    c = client(guess, guessed, end)
    c.start()
    print("s")
    Thread(target=send).start()
    while True:
        for event in c.events():
            if event.event_name == "guessed":
                print("player {} has {} guess left, word is now {}".format(event.who, event.guess, event.word))




    #cliant