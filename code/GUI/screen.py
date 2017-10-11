import pygame

from GUI.button import Button
from GUI.game import Game
from GUI.picker import Picker
from players.minimax_player import MinimaxPlayer
from players.random_player import RandomPlayer

class Screen:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((400, 440))
        self.game = Game(0, 40, 400, 400)

        player_options = [
            ('Human', 0),
            ('Minimax', 1),
            ('Random', 2)
        ]

        self.player1_picker = Picker(5, 5, 150, 30, player_options, 1)
        self.player2_picker = Picker(160, 5, 150, 30, player_options)
        self.go_button = Button(320, 5, 50, 30, 'GO', self.on_go)
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

            self.player1_picker.update(events)
            self.player2_picker.update(events)
            self.go_button.update(events)
            self.game.update(events)

            self.player1_picker.render()
            self.player2_picker.render()
            self.go_button.render()
            self.game.render()

            self.screen.blit(self.game, (self.game.x, self.game.y))
            self.screen.blit(self.player1_picker, (self.player1_picker.x, self.player1_picker.y))
            self.screen.blit(self.player2_picker, (self.player2_picker.x, self.player2_picker.y))
            self.screen.blit(self.go_button, (self.go_button.x, self.go_button.y))

            pygame.display.flip()

    def on_go(self):
        player1 = self.get_player(self.player1_picker.get_value())
        player2 = self.get_player(self.player2_picker.get_value())
        self.game.start_new_game(player1, player2)

    def get_player(self, picker_value):
        if picker_value == 0:
            return 'human'
        if picker_value == 1:
            return MinimaxPlayer()
        if picker_value == 2:
            return RandomPlayer()

if __name__ == '__main__':
    screen = Screen()
    screen.start()