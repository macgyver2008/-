import pygame
import random
from datetime import datetime
from datetime import timedelta
SCREEN_WIDTH = 400
SCREEN_HIGHT = 400
BLOCK_SIZE = 20

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE =(0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))


def draw_bg(screen):
    background = pygame.Rect((0, 0), (SCREEN_WIDTH, SCREEN_HIGHT))
    pygame.draw.rect(screen, WHITE, background)

def draw_block(screen, color, position):
    block = pygame.Rect(
        (position[0] * BLOCK_SIZE, position[1] * BLOCK_SIZE),
        (BLOCK_SIZE, BLOCK_SIZE)
    )
    pygame.draw.rect(screen, color, block)
class Offset:
    NONE = [0, 0]
    RIGHT = [1, 0]
    LEFT = [-1, 0]
    UP = [0, -1]
    DOWN = [0, 1]

class Snake:
    def __init__(self, color, position, offset):
        self.color = color
        self.offset = offset

        self. positions =[
            position,
            [position[0], position[1] + 1],
            [position[0], position[1] + 2],
            [position[0], position[1] + 3]

        ]
    def draw(self):
        for position in self.positions:
            draw_block(screen, self.color, position)

    def move(self):
        now_pos = [self.positions[0][0], self.positions[0][1]]
        self.positions[0][0] += self.offset[0]
        self.positions[0][1] += self.offset[1]
        last_pos = now_pos

        for i in range(1, len(self.positions)):
            now_pos = [self.positions[i][0], self.positions[i][1]]
            self.positions[i] = last_pos
            last_pos = now_pos

    def grow(self):
        self.positions.append([self.positions[-1][0], self.positions[-1][1]])

class Apple:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def draw(self):
        draw_block(screen, self.color, self.position)

    def random_move(self):
        self.position = [random.randint(0, 19), random.randint(0, 19)]
class Game:
    def __init__(self):
        self.snake = Snake(GREEN, [9, 9], Offset.NONE)
        self.apple = Apple(RED, [3, 3])

    def draw(self):
        draw_bg(screen)
        self.snake.draw()
        self.apple.draw()
        pygame.display.update()

    def start(self):
        last_movement = datetime.now()
        keydown_flag = False
        while True:
            events = pygame.event.get()
            for event in events:

                if event.type == pygame.QUIT:
                    exit()

                elif event.type == pygame.KEYDOWN and not keydown_flag:

                    if event.key == pygame.K_RIGHT and self.snake.offset != Offset.LEFT:
                        self.snake.offset = Offset.RIGHT
                        keydown_flag = True
                    elif event.key == pygame.K_LEFT and self.snake.offset != Offset.RIGHT:
                        self.snake.offset = Offset.LEFT
                        keydown_flag = True
                    elif event.key == pygame.K_UP and self.snake.offset != Offset.DOWN:
                        self.snake.offset = Offset.UP
                        keydown_flag = True
                    elif event.key == pygame.K_DOWN and self.snake.offset != Offset.UP:
                        self.snake.offset = Offset.DOWN
                        keydown_flag = True

            if self.snake.positions[0] == self.apple.position:
                self.apple.random_move()
                self.snake.grow()


            if timedelta(milliseconds=300) <= datetime.now() - last_movement:
                last_movement = datetime.now()
                keydown_flag = False
                self.snake.move()

            self.draw()


game = Game()
game.start()
