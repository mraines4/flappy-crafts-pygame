import pygame

KEY_UP = 273

# create DC class
class DC(object):
    def __init__(self):
        self.image = pygame.image.load('images/DC-logo.png').convert_alpha()
        self.x = 60
        self.y = 400
        self.dir_y = 10

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def update(self):
        self.y += self.dir_y

# creates Pipe class
class Pipes(object):
    def __init__(self):
        self.image = pygame.image.load('images/pipes.png').convert_alpha()
        self.x = 1000
        self.y = 0
        self.dir_x = -10

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def update(self):
        self.x += self.dir_x

pipe_list = [
    # Pipes(-400),
    # Pipes(100),
    # Pipes(-200),
    # Pipes(-300)
]


def main():
    width = 750
    height = 750

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Flappy Crafts')
    clock = pygame.time.Clock()

    # Game initialization (prints background image/pipes/and DC)
    background_image = pygame.image.load('images/background.png').convert_alpha()
    # pipes = pygame.image.load('images/pipes.png').convert_alpha()
    dc_logo = DC()
    # for pipe in pipe_list:
    #     moving_pipe = Pipes()
    moving_pipe = Pipes()

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling for keystroke up for DC logo
            if event.type == pygame.KEYDOWN:
                if event.key == KEY_UP:
                    dc_logo.dir_y -= 40
                    dc_logo.image = pygame.image.load('images/DC-logo-tilt.png').convert_alpha()
            if event.type == pygame.KEYUP:
                if event.key == KEY_UP:
                    dc_logo.dir_y = 10
                    dc_logo.image = pygame.image.load('images/DC-logo.png').convert_alpha()

            # stops the logo from going off the screen
            if dc_logo.y < 0:
                dc_logo.y = 0
            if dc_logo.y >= 750:
                dc_logo.y = 750

            # quits game if red box clicked
            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic

        # Draw background
        screen.blit(background_image, (0,0))

        # Game display
        dc_logo.draw(screen)
        dc_logo.update()
        moving_pipe.draw(screen)
        moving_pipe.update()

        # dc_logo.handle_keys()
        # screen.blit(pipes, (0,-400)),
        # screen.blit(pipes, (100,-100)),
        # screen.blit(pipes, (200,-200)),
        # screen.blit(pipes, (300,-300))
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
