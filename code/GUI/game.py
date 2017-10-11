import time

import pygame

from functions import result


class Game(pygame.Surface):

    player_moving = 0
    wait = None
    started = False
    players = ()

    def __init__(self, x, y, width, height):
        super().__init__((width, height))

        self.width = width
        self.height = height
        self.x = x
        self.y = y

        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

        self.cell_size = min(self.width / len(self.board[0]), self.height / len(self.board))

    def start_new_game(self, player1, player2):
        self.started = True
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                self.board[y][x] = 0

        self.players = (
            player1,
            player2
        )

    def update(self, events):
        if not self.started or result(self.board) != -1:
            return

        if self.wait and time.time() < self.wait:
            return

        move = (-1, -1)
        if self.players[self.player_moving] == 'human':
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mx = event.pos[0] - self.x
                        my = event.pos[1] - self.y
                        cs = self.cell_size
                        for y in range(len(self.board)):
                            for x in range(len(self.board)):
                                if my > y * cs and my < (y + 1) * cs \
                                    and mx > x * cs and mx < (x + 1) * cs:
                                    move = (x, y)
        else:
            if self.wait is None:
                self.wait = time.time() + 0.5
                return
            move = self.players[self.player_moving].get_move()

        if self.valid_move(move):
            self.board[move[1]][move[0]] = self.player_moving + 1
            next_player = (self.player_moving + 1) % 2
            if self.players[next_player] != 'human':
                self.players[next_player].opponent_move(move[0], move[1])
            self.player_moving = next_player

        self.wait = None

    def render(self):
        self.fill((255, 255, 255))

        for x in range(1, len(self.board[0])):
            pygame.draw.line(self, (0, 0, 0), (x * self.cell_size, 0), (x * self.cell_size, self.height))

        for y in range(1, len(self.board)):
            pygame.draw.line(self, (0, 0, 0), (0, y * self.cell_size), (self.width, y * self.cell_size))

        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                if self.board[y][x] != 0:
                    line_width = 8
                    pad = self.cell_size * 0.1
                    x0 = x * self.cell_size + pad
                    x1 = (x + 1) * self.cell_size - pad
                    y0 = y * self.cell_size + pad
                    y1 = (y + 1) * self.cell_size - pad

                    if self.board[y][x] == 1:
                        pygame.draw.line(self, (0, 0, 0), (x0, y0), (x1, y1), line_width)
                        pygame.draw.line(self, (0, 0, 0), (x0, y1), (x1, y0), line_width)
                    elif self.board[y][x] == 2:
                        pygame.draw.ellipse(self, (0, 0, 0), pygame.Rect(x0, y0, x1 - x0, y1 - y0), line_width)

        res = result(self.board)
        if res != -1 or not self.started:
            s = pygame.Surface((self.width, self.height))
            s.set_alpha(128)
            s.fill((0, 0, 0))
            self.blit(s, (0, 0))

            font = pygame.font.SysFont(None, 40)
            label = None
            if res == 0:
                label = font.render('Draw!', True, (255, 255, 255))
            elif res == 1:
                label = font.render('Player 1 wins!', True, (255, 255, 255))
            elif res == 2:
                label = font.render('Player 2 wins!', True, (255, 255, 255))

            if label:
                x = (self.width / 2) - (label.get_width() / 2)
                y = (self.height / 2) - (label.get_height() / 2)
                self.blit(label, (x, y))

    def valid_move(self, move):
        if len(move) != 2:
            return False

        if move[0] < 0 or move[0] > len(self.board) - 1 or move[1] < 0 or move[1] > len(self.board) - 1:
            return False

        if self.board[move[1]][move[0]]:
            return False

        return True