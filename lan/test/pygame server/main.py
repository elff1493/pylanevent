from socketEvents import Server, Structure, PGTYPE
import socketEvents
import pygame


pygame.init()
socketEvents.init_pyevents() 
# initialize sound - uncomment if you're using sound
# pygame.mixer.init()
# create the game window and set the title
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My Game")
# start the clock
clock = pygame.time.Clock()

e = Structure("test", text=str)
server = Server(e, use_pygame=True)
server.ip = "localhost"
server.start()

# set the 'running' variable to False to end the game
running = True
# start the game loop
while running:
    # keep the loop running at the right speed
    clock.tick(60)
    #server.add_event(text="tt")
    # Game loop part 1: Events #####
    for event in pygame.event.get():
        # this one checks for the window being closed
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.USEREVENT:
            print(event, "user")
        elif event.type == PGTYPE.EVENT:
            print(event)
        elif event.type == PGTYPE.JOIN:
            print(event, "joined")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            server.send_to(e, server.conns[0], text="hi")
            print(server.conns)



        # add any other events here (keys, mouse, etc.)

    # Game loop part 2: Updates #####

    # Game loop part 3: Draw #####
    screen.fill((0, 0, 0))
    # after drawing, flip the display
    pygame.display.flip()

# close the window
pygame.quit()