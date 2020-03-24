# sky dodge game

# import the pygame library
import pygame
import os

# import pygame locals for easier access to key coordiantes
from pygame.locals import(
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

# define size
WIDTH = 800
HEIGHT = 500

# loop speed
FPS = 30

# define colours
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
LIGHTBLUE = (100,100,255)
DARKRED = (100,0,0)

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')



# initialise pygame
pygame.init()

pygame.display.set_caption('DL game')

class Player(pygame.sprite.Sprite):
    ''' class for sprite '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((50, 50))
        #self.image.fill(DARKRED)
        imageName = ['marsRocket_01.jpg', 'retro_aircraft_01.png']
        self.image = pygame.image.load(os.path.join(img_folder, imageName[1])).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.x_speed = 5
        self.y_speed = 0

    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed


        if self.rect.bottom > HEIGHT - 50:
            self.y_speed = -3
        if self.rect.top < 50:
            self.y_speed = 1
        if self.rect.left > WIDTH:
            self.rect.right = 0
            



#setup the drawing window
screen = pygame.display.set_mode((WIDTH,HEIGHT))

clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# run until the user asks to quit
running = True
while running:

    # keep loop running at correct speed
    clock.tick(FPS)

    # events in pygame
    for event in pygame.event.get():
        # user clicks close window
        if event.type == pygame.QUIT:
            running = False
        # key is pressed
        if event.type == pygame.KEYDOWN:
            # down arrow pressed
            if event.key == pygame.K_DOWN:
                player.y_speed += 1
            # up arrow pressed
            if event.key == pygame.K_UP:
                player.y_speed -= 1
            # left arrow pressed
            if event.key == pygame.K_LEFT:
                player.x_speed -= 1
            # right arrow pressed
            if event.key == pygame.K_RIGHT:
                player.x_speed += 1


    # update
    all_sprites.update()

    # draw / render
    screen.fill(LIGHTBLUE) # fill background light blue
    all_sprites.draw(screen)

    # flip display
    pygame.display.flip()

# done. time to quit.
pygame.quit()

