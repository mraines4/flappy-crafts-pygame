import pygame

class DC(object):
    def __init__(self):
        self.image = pygame.image.load('images/DC-logo.png').convert_alpha()
        self.x = 60
        self.y = 400
        self.dir_y = 10

    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 40
        if key[pygame.K_UP]:
            self.y -= dist
            self.image = pygame.image.load('images/DC-logo-tilt.png').convert_alpha()

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

def main():
    width = 800
    height = 800

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Flappy Crafts')
    clock = pygame.time.Clock()

    # Game initialization
    background_image = pygame.image.load('images/background.png').convert_alpha()
    pipes = pygame.image.load('images/pipes.png').convert_alpha()
    dc_logo = DC()

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling
            if dc_logo.y < 0:
                dc_logo.y = 0
            if dc_logo.y >= 800:
                dc_logo.y = 800

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic
        dc_logo.y += dc_logo.dir_y

        # Draw background
        screen.blit(background_image, (0,0))

        # Game display
        dc_logo.draw(screen)
        dc_logo.handle_keys()
        screen.blit(pipes, (0,-400)),
        screen.blit(pipes, (100,-100)),
        screen.blit(pipes, (200,-200)),
        screen.blit(pipes, (300,-300))
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
