import pygame

KEY_UP = 273

# create DC class
class DC(object):
    def __init__(self):
        self.image = pygame.image.load('images/DC-logo.png').convert_alpha()
        self.x = 60
        self.y = 400
        self.dir_y = 5

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def update(self):
        self.y += self.dir_y

# creates Pipe class
class Pipes:
    def __init__(self, x, y, speed):
        self.image = pygame.image.load('images/pipes.png').convert_alpha()
        self.x = x
        self.y = y
        self.speed = speed

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update(self, width):
        self.x += self.speed



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
    pipe_list = [
    Pipes(1000, -400, -10),
    Pipes(1000, 100, -10),
    Pipes(1000,-200, -10),
    Pipes(1000, -300, -10)
]


    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling for keystroke up for DC logo
            if event.type == pygame.KEYDOWN:
                if event.key == KEY_UP:
                    dc_logo.dir_y -= 20
                    dc_logo.image = pygame.image.load('images/DC-logo-tilt.png').convert_alpha()
            if event.type == pygame.KEYUP:
                if event.key == KEY_UP:
                    dc_logo.dir_y = 5
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
        for pipe in pipe_list:
            pipe.update(width)

        # Draw background
        screen.blit(background_image, (0,0))

        # Game display
        dc_logo.draw(screen)
        dc_logo.update()
        for pipe in pipe_list:
            pipe.display(screen)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
