import socketEvents
from socketEvents import Server, Structure
from socketEvents.types import UInt1Type


class Test(Server):
    def __init__(self):

        self.guess = Structure("guess",
                               str=str
                               )
        self.guessed = Structure("guessed",
                                 guess=UInt1Type,
                                 word=str,
                                 who=str
                               )
        self.end = Structure("end",
                             win=bool,
                             winner=str
        )

        Server.__init__(self, self.guess, self.guessed, self.end)

    def go(self):
        self.ip = 'localhost'
        self.start()
        word = "testword"
        letter = []
        win = False
        players = {}
        w = "".join([x if x in letter else "-" for x in word])
        while not win:

            for event in self.events():
                print(event)
                if event.event_name == "join":
                    players[event.player] = 5

                elif event.event_name == "guess":
                    if players[event.player]:
                        if event.str[0] not in word:
                            players[event.player] -= 1
                        letter.append(event.str[0])
                        w = "".join([x if x in letter else "-" for x in word])
                        self.send_to(self.guessed, event.player, guess=players[event.player], word=w,
                                     who=str(event.player))


                        if "-" not in w:
                            self.send_to(win, event.player, win=True, winner=str(event.player))
                            win = False


if __name__ == "__main__":
    c = Test()
    c.go()
