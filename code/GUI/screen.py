import pygame
from GUI.game import Game

class Screen:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((400, 450))
        self.game = Game(0, 50, 400, 400)
        self.clock = pygame.time.Clock()

    def start(self):
        self.running = True
        self.run()

    def stop(self):
        self.running = False

    def run(self):
        while self.running:
            self.clock.tick(30)

            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    self.stop()

            self.game.update(events)

            self.game.render()

            self.screen.blit(self.game, (self.game.x, self.game.y))


            pygame.display.flip()

if __name__ == '__main__':
    screen = Screen()
    screen.start()