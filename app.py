import pygame
import random
from random import randint

KEY_UP = 273
SPACE = 32


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

# creates win piece class
class WinPiece(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load('images/cloud.png').convert_alpha()
        self.x = 750
        self.y = 400
        self.speed = -10
        self.rect = self.image.get_rect()
        pygame.sprite.Sprite.__init__(self)
        self.rect.x = 750
        self.rect.y = 400

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update(self):
        self.rect.x += self.speed

def main():
    width = 790
    height = 790
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Flappy Crafts')
    clock = pygame.time.Clock()

    # Game initialization (prints background image/pipes/and DC)
    background_image = pygame.image.load('images/background.png').convert_alpha()
    welcome_image = pygame.image.load('images/welcome.png').convert_alpha()
    lost_life = pygame.image.load('images/lost-life.png').convert_alpha()
    game_over = pygame.image.load('images/game-over.png').convert_alpha()
    lives = 3

    main_game = True
    while main_game:
        if lives == 3:
            screen.blit(welcome_image, (0,0))
        elif lives < 3 and lives > 0:
            screen.blit(lost_life, (0,0))
        elif lives == 0:
            screen.blit(game_over, (0,0))

        pygame.display.update()
        playing = False
        for event in pygame.event.get():
                # Event handling for keystroke up for DC logo
                if event.type == pygame.KEYDOWN:
                    if event.key == SPACE:
                        playing = True
                        dg = pygame.sprite.Group()
                        dc_logo = DC()
                        dg.add(dc_logo)
                        pipe_list = []
                        wg = pygame.sprite.Group()
                        end_piece = WinPiece()
                        # wg.add(end_piece)
                        timer_count = 60
                    if lives == 0:
                        if event.key == SPACE:
                            lives = 3
                            playing = False
        while playing:
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
                if event.type == pygame.QUIT:
                    pygame.quit()

                # stops the logo from going off the screen
                if dc_logo.rect.y < 0:
                    dc_logo.rect.y = 0
                if dc_logo.rect.y >= 750:
                    dc_logo.rect.y = 750


            # set timer over
            timer_count -= 1
            if timer_count == 0 and len(pipe_list) < 6:
                rndm_ydn = randint(-300, 0)
                pipe_list.append(PipesDown(750, rndm_ydn, -10))
                pipe_list.append(Pipes(750, (rndm_ydn + 700), -10))
                timer_count = 60
            else:
                wg.add(end_piece)

            # Draw background 
            screen.blit(background_image, (0,0))

            # Game logic
            for pipe in pipe_list:
                pg.add(pipe)


            # collision
            hit = pygame.sprite.spritecollide(dc_logo, pg, False)
            if hit:
                dg.remove(dc_logo)
                lives -= 1
                playing = False
            else:
                for pipe in pipe_list:
                    pipe.update(width)
            pg.draw(screen)


            # Game display
            dc_logo.update()
            dg.draw(screen)
            end_piece.update()
            wg.draw(screen)
            pygame.display.update()


        # quits game if red box clicked
        if event.type == pygame.QUIT:
            main_game = False

    pygame.quit()

if __name__ == '__main__':
    main()
