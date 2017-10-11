import pygame

class Picker(pygame.Surface):

    BUTTON_WIDTH = 20

    def __init__(self, x, y, width, height, options, selection=0):
        super().__init__((width, height))
        self.x = x
        self.y = y
        self.options = options
        self.selected_option = selection

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[1] > self.y and event.pos[1] < self.y + self.get_height():
                    if event.pos[0] > self.x + self.get_width() - self.BUTTON_WIDTH * 2 \
                        and event.pos[0] < self.x + self.get_width() - self.BUTTON_WIDTH:
                        self.selected_option = (self.selected_option - 1) % len(self.options)
                    elif event.pos[0] > self.x + self.get_width() - self.BUTTON_WIDTH \
                        and event.pos[0] < self.x + self.get_width():
                        self.selected_option = (self.selected_option + 1) % len(self.options)

    def render(self):
        self.fill((255, 255, 255))
        #pygame.draw.rect(self, pygame.Rect(2, 2, self.get_width() - 4, self.get_height() - 4), 1)

        text = self.options[self.selected_option][0]
        font = pygame.font.SysFont(None, self.get_height())
        label = font.render(text, True, (0, 0, 0))
        self.blit(label, (5, 5))

        pygame.draw.line(self, (0, 0, 0), (self.get_width() - 2 * self.BUTTON_WIDTH, 0),
                         (self.get_width() - 2 * self.BUTTON_WIDTH, self.get_height()))
        pygame.draw.line(self, (0, 0, 0), (self.get_width() - self.BUTTON_WIDTH, 0),
                         (self.get_width() - self.BUTTON_WIDTH, self.get_height()))

        x0 = self.get_width() - 2 * self.BUTTON_WIDTH + 3
        x1 = self.get_width() - self.BUTTON_WIDTH - 3
        y0 = 2
        y1 = self.get_height() / 2
        y2 = self.get_height() - 2
        pygame.draw.polygon(self, (0, 0, 0), ((x1, y0), (x0, y1), (x1, y2)))
        pygame.draw.polygon(self, (0, 0, 0), ((x0 + self.BUTTON_WIDTH, y0), (x1 + self.BUTTON_WIDTH, y1),
                                              (x0 + self.BUTTON_WIDTH, y2)))

    def get_value(self):
        return self.options[self.selected_option][1]