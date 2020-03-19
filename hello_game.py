# simple pygame program

# import and initialise the pygame library
import pygame

pygame.init()


#setup the drawing window
screen = pygame.display.set_mode((500,500))


# run until the user asks to quit
running = True
while running:

    # did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # fill the background with white
    screen.fill((255,255,255))

    # draw a solid blue circle in the center
    pygame.draw.circle(screen, (0,0,255), (250,250), 75)

    # flip display
    pygame.display.flip()

# done. time to quit.
pygame.quit()

