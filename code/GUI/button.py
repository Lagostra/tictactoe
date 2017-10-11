import pygame

class Button(pygame.Surface):

    def __init__(self, x, y, width, height, text, callback):
        super().__init__((width, height))

        self.x = x
        self.y = y
        self.text = text
        self.callback = callback

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] > self.x and event.pos[0] < self.x + self.get_width() \
                    and event.pos[1] > self.y and event.pos[1] < self.y + self.get_height():
                    self.callback()

    def render(self):
        self.fill((255, 255, 255))

        font = pygame.font.SysFont(None, self.get_height())
        label = font.render(self.text, True, (0, 0, 0))
        self.blit(label, ((self.get_width() - label.get_width()) / 2, 5))