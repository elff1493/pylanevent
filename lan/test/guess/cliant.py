import main2
from socketEvents import *
from socketEvents.types import *
#from main2 import *
from threading import Thread

def send():
    while True:
        inp = input("guess")
        if inp:
            conn.send(guess, str=inp)

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

    conn = client(guess, guessed, end)
    conn.start()

    print("start game")
    print()

    Thread(target=send).start()

    while True:
        for event in conn.events():
            if event.event_name == "guessed":
                print("player {} has {} guess left, word is now {}".format(event.who, event.guess, event.word))
            else:
                print(event)




    #cliant