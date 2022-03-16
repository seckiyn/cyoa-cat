""" Main window and loop """
import lit
import sys
import pygame

class Col:
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)


SIZE= (500, 500)
WIDTH, HEIGHT = SIZE
FPS = 60

things = pygame.init() # Init the pygame

def main():
    """ Main function """
    screen = pygame.display.set_mode(SIZE) # start screen surface
    clock = pygame.time.Clock() # pygame clock
    running = True
    while running: # Main loop
        clock.tick(FPS) # Pygame clock tick
        for event in pygame.event.get(): # Event loop
            if event.type == pygame.QUIT: # If quit signal get
                sys.exit(1) # Exit the program
            if event.type == pygame.KEYDOWN: # If a key pressed down
                if event.key == pygame.K_ESCAPE: # If esc pressed
                    sys.exit(1) # Exit the program
        # Process events

        # Paint according to events
        screen.fill(Col.blue) # Remove the buffer
        lit.blit_file(screen, "im.png", (0,0),"img")


        # Paint them to screen
        pygame.display.update()

if __name__ == "__main__":
    main()
