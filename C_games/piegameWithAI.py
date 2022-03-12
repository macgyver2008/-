import pygame
import random

from datetime import datetime
from datetime import timedelta
from perceptron import *

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
BLOCK_SIZE = 20

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def draw_bg(screen):
    background = pygame.Rect((0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT))
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

        self.nnw = NeuralNetwork(6, 30, 3)
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
    def getDirection(self):
        if self.offset == Offset.UP:
            return [Offset.UP, Offset.LEFT, Offset.RIGHT]
        elif self.offset == Offset.DOWN:
            return [Offset.DOWN, Offset.RIGHT, Offset.LEFT]
        elif self.offset == Offset.LEFT:
            return [Offset.LEFT, Offset.DOWN, Offset.UP]
        else:
            return [Offset.RIGHT, Offset.UP, Offset.DOWN]

    def obstacleSensor(self):
        ob_sensor = [1.0, 1.0, 1.0]
        direction = self.getDirection()

        head = list(self.positions[0])
        for i in range(3):
            for j in range(1, 6):
                if not (20 > head[0] + direction[i][0] * j >= 0
                        and 20 > head[1] + direction[i][1] * j >= 0):
                    ob_sensor[1] -= 0.2
                elif True:
                    pass
        return ob_sensor
    def AppleSensor(self, applePos):
        direction = self.getDirection()


        fbeam = list(self.positions[0])
        while 0 <= fbeam[0] < 20 and 0 <= fbeam[1] < 20:
            fbeam[0] += direction[0][0]
            fbeam[1] += direction[0][1]
            if fbeam == applePos:
                return [1.0, 0.0, 0.0]
            lbeam = list(fbeam)
            while 0 <= lbeam[0] < 20 and 0 <= lbeam[1] < 20:
                if lbeam == applePos:
                    return [0.0, 1.0, 0.0]
                lbeam[0] += direction[1][0]
                lbeam[1] += direction[1][1]
            rbeam = list(fbeam)
            while 0 <= rbeam[0] < 20 and 0 <= rbeam[1] < 20:
                if rbeam == applePos:
                    return [0.0, 0.0, 1.0]
                rbeam[0] += direction[2][0]
                rbeam[1] += direction[2][1]
            pass
        return [0.0, 0.0, 0.0]
    def setOffset(self, output):
        direction = self.getDirection()
        self.offset = direction[np.argmax(output)]




class Apple:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def draw(self):
        draw_block(screen, self.color, self.position)

    def random_move(self, avoid_pos):
        self.position = [random.randint(0, 19), random.randint(0, 19)]
        while self.position in avoid_pos:
            self.position = [random.randint(0, 19), random.randint(0, 19)]


class Game:
    def __init__(self):
        self.snake = Snake(GREEN, [9, 9], Offset.UP)
        self.apple = Apple(RED, [3, 3])
        self.score = 0
        self.timer = 50
    def draw(self):
        draw_bg(screen)
        self.snake.draw()
        self.apple.draw()
        pygame.display.update()
    def crush(self):
        shead = self.snake.positions[0]
        if shead[0] < 0 or shead[0] > 19 or shead[1] < 0 or shead[1] > 19 or shead in self.snake.positions[1:]:
            return True
        return False
    def start(self):
        last_movement = datetime.now()
        keydown_flag = False
        last_input = []
        last_output = []
        eat_list = []
        live_list = []
        time_speed = 1
        train_cnt = 0
        max_score = 0
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
                    elif event.key == pygame.K_w:
                        time_speed = time_speed - 1 if not time_speed == 1 else 1
                    elif event.key == pygame.K_s:
                        time_speed = time_speed + 1 if not time_speed == 30000000 else 30000000




            if self.snake.positions[0] == self.apple.position:
                self.apple.random_move(self.snake.positions)
                self.snake.grow()
                self.timer += 50
                self.score += 1
                output = [0.0, 0.0, 0.0]
                output[np.argmax(last_output)] = 1.0
                eat_list.insert(0, [last_input, output])

            if self.crush() or self.timer == 0:
                if self.score == 0:
                    for i in range(10):
                        output =[0.0, 0.0, 0.0]
                        output[random.randint(0, 2)] = 1.0
                        self.snake.nnw.train(last_input, output, 0.1)
                elif self.crush():
                    for io in live_list:
                        self.snake.nnw.train(io[0], io[1], 0.01)
                for io in eat_list:
                    self.snake.nnw.train(io[0], io[1], 0.02)

                last_output = []
                last_input = []
                live_list = []

                train_cnt += 1
                if max_score < self.score:
                    max_score = self.score
                print(F"{train_cnt}회 학습중 최고점수 {self.score}")
                brain = self.snake.nnw
                self.__init__()
                self.apple.random_move(self.snake.positions)
                self.snake.nnw = brain
            if timedelta(microseconds=time_speed) <= datetime.now() - last_movement:
                self.timer -= 1
                if len(last_input) != 0 and len(last_output) != 0:
                    output = [0.0, 0.0, 0.0]
                    output[np.argmax(last_output)] = 1.0
                    live_list.insert(0, [last_input, output])
                input1 = self.snake.obstacleSensor()
                input2 = self.snake.AppleSensor(self.apple.position)
                last_input = input1 + input2

                last_output = self.snake.nnw.query(last_input)
                self.snake.setOffset(last_output)

                last_movement = datetime.now()
                keydown_flag = False
                self.snake.move()

            self.draw()


game = Game()
game.start()
