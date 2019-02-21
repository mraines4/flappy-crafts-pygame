import pygame
import random
from random import randint

KEY_UP = 273


# pg = pygame.sprite.Group()
dg = pygame.sprite.Group()

# create DC class
class DC(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load('images/DC-logo.png').convert_alpha()
        self.x = 60
        self.y = 400
        self.dir_y = 10
        self.rect = self.image.get_rect()
        pygame.sprite.Sprite.__init__(self)
        self.rect.x = 60
        self.rect.y  = 400

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update(self):
        self.rect.y += self.dir_y

# creates Pipe class
class Pipes(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        self.image = pygame.image.load('images/up-pipe.png').convert_alpha()
        self.x = x
        self.y = y
        self.speed = speed
        self.rect = self.image.get_rect()
        pygame.sprite.Sprite.__init__(self)
        self.rect.x = x
        self.rect.y = y

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update(self, width):
        self.rect.x += self.speed

class PipesDown(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        self.image = pygame.image.load('images/down-pipe.png').convert_alpha()
        self.x = x
        self.y = y
        self.speed = speed
        self.rect = self.image.get_rect()
        pygame.sprite.Sprite.__init__(self)
        self.rect.x = x
        self.rect.y = y

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update(self, width):
        self.rect.x += self.speed


def main():
    width = 750
    height = 750
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Flappy Crafts')
    clock = pygame.time.Clock()

    # Game initialization (prints background image/pipes/and DC)
    background_image = pygame.image.load('images/background.png').convert_alpha()
    dc_logo = DC()
    dg.add(dc_logo)
    pipe_list = []
    timer_count = 60
    # for each in pipe_list:
    #     pg.add(each)


    stop_game = False
    while not stop_game:
        pg = pygame.sprite.Group()
        for event in pygame.event.get():
            # Event handling for keystroke up for DC logo
            if event.type == pygame.KEYDOWN:
                if event.key == KEY_UP:
                    dc_logo.dir_y -= 20
                    dc_logo.image = pygame.image.load('images/DC-logo-tilt.png').convert_alpha()
            if event.type == pygame.KEYUP:
                if event.key == KEY_UP:
                    dc_logo.dir_y = 10
                    dc_logo.image = pygame.image.load('images/DC-logo.png').convert_alpha()

            # stops the logo from going off the screen
            if dc_logo.rect.y < 0:
                dc_logo.rect.y = 0
            if dc_logo.rect.y >= 750:
                dc_logo.rect.y = 750

            # quits game if red box clicked
            if event.type == pygame.QUIT:
                stop_game = True

        # set timer over
        timer_count -= 1
        if timer_count == 0 and len(pipe_list) < 40:
            rndm_ydn = randint(-400, 0)
            pipe_list.append(PipesDown(750, rndm_ydn, -10))
            pipe_list.append(Pipes(750, (rndm_ydn + 700), -10))
            timer_count = 60


        # Game logic
        for pipe in pipe_list:
            pipe.update(width)
            pg.add(pipe)

        # collision
        hit = pygame.sprite.spritecollide(dc_logo, pg, False)
        if hit:
            # print("hit")
            dg.remove(dc_logo)

        # Draw background
        screen.blit(background_image, (0,0))

        # Game display
        # dc_logo.display(screen)
        dc_logo.update()
        dg.draw(screen)
        # for pipe in pipe_list:
        #     pipe.display(screen)
        pg.draw(screen)
        pygame.display.update()
    

    pygame.quit()

if __name__ == '__main__':
    main()
