import pygame
import neat
import time
from multiprocessing import Process
import sys
import math


tempFoodImage = pygame.image.load(r'C:\Users\jarvis\PycharmProjects\simplegame\cactus3.png')

foodImage = pygame.transform.scale(tempFoodImage, (20, 20))

tempFoodImage2 = pygame.image.load(r'C:\Users\jarvis\PycharmProjects\simplegame\cactus4.png')

foodImage2 = pygame.transform.scale(tempFoodImage2, (20, 20))

tempAgentImage = pygame.image.load(r'C:\Users\jarvis\PycharmProjects\simplegame\rex.png')

agentImage = pygame.transform.scale(tempAgentImage, (40, 40))

tempCloudImage1 = pygame.image.load(r'C:\Users\jarvis\PycharmProjects\simplegame\cloud1.png')

cloudImage1 = pygame.transform.scale(tempCloudImage1, (50, 30))

tempCloudImage2 = pygame.image.load(r'C:\Users\jarvis\PycharmProjects\simplegame\cloud2.png')

cloudImage2 = pygame.transform.scale(tempCloudImage2, (50, 30))

tempCloudImage3 = pygame.image.load(r'C:\Users\jarvis\PycharmProjects\simplegame\cloud3.png')

cloudImage3 = pygame.transform.scale(tempCloudImage3, (50, 30))


class Food:
    def __init__(self):
        self.p = 450
        self.q = 470
        self.size = 10
        self.alive = True
        self.number = 0
        self.image = foodImage

    def draw(self, screen):
        screen.blit(self.image, dest=(self.p, self.q))

        if self.number % 3 == 0:
            self.image = foodImage2

        else:
            self.image = foodImage
        #pygame.draw.circle(screen, (0, 255, 0), (self.p, self.q), 5)


class Cloud1:
    def __init__(self):
        self.m = 100
        self.n = 250

    def draw(self, screen):
        screen.blit(cloudImage1, dest=(self.m, self.n))


class Cloud2:
    def __init__(self):
        self.m = 300
        self.n = 200

    def draw(self, screen):
        screen.blit(cloudImage2, dest=(self.m, self.n))


class Cloud3:
    def __init__(self):
        self.m = 400
        self.n = 150

    def draw(self, screen):
        screen.blit(cloudImage3, dest=(self.m, self.n))


class Agent:
    def __init__(self):
        self.x = 0
        self.y = 450
        self.alive = True
        self.score = 0
        self.size = 30
        self.image = agentImage
        self.number = 0

    def draw(self, screen):

        screen.blit(self.image, dest=(self.x, self.y))

    def jumpUp(self):
        if self.y == 450:
            self.y = self.y - 25

    def jumpDown(self):
        if self.y < 450:
            self.y += 25

    def duckDown(self):
        if self . y == 450:
            self.y += 25

    def duckUp(self):
        if self.y > 450:
            self.y -= 25


food = Food()
agent = Agent()
cloud1 = Cloud1()
cloud2 = Cloud2()
cloud3 = Cloud3()

pygame.init()
win = pygame.display.set_mode((500, 500))
run = True
vel = 5
cloudVel1 = 0.6
cloudVel2 = 0.5
cloudVel3 = 0.4


def dis(x, y, p, q):
    dist = math.sqrt((x-p)*(x-p) - (y-q)*(y-q))
    return dist


def collision(agent1, food1):
    if agent1.x < food1.p < agent1.x+agent1.size:
        if agent1.y < food1.q < agent1.y + agent1.size:
            return True

"""def agentRun(run1):
    while run1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run1 = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            agent.jump();

        time.sleep(1)
        pygame.display.update()


def gameRun(food1,agent1,run1):
    while run1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run1 = False

        food1.p = food1.p - vel;
        if (food1.p < 0):
            food = Food()
        pygame.time.delay(20)
        food1.draw(win)
        agent1.draw(win)
        pygame.display.update()"""




"""if __name__ == '__main__':
    p1 = Process(target=agentRun(run))

    p2 = Process(target=gameRun(food, agent, run))

    processes = list()
    processes.append(p1)
    processes.append(p2)

    for p in processes:
        p.start()"""
uptime = time.time()
downtime = time.time()
startTime = time.time()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and agent.y == 450:
        uptime = time.time()
        agent.jumpUp()

    if time.time() - uptime>1:
        agent.jumpDown()
        uptime = time.time()

    if keys[pygame.K_DOWN] and agent.y == 450:
        downtime = time.time()
        agent.duckDown()

    if time.time() - downtime > 1:
        agent.duckUp()
        downtime = time.time()

    font = pygame.font.Font('freesansbold.ttf', 32)
    textColor = (255, 0, 0)
    score = math.trunc(time.time()-startTime)
    text_surface = font.render(str(score), True, textColor)

    print(score)
    if collision(agent, food):
        startTime = time.time()
        print("collision happened")
        food = Food()
        cloud1.m = 50
        cloud2.m = 500
        cloud3.m = 200

    food.p = food.p-vel
    cloud1.m = cloud1.m - cloudVel1
    cloud2.m -= cloudVel2
    cloud3.m -= cloudVel3

    if cloud1.m + 50 < 0:
        cloud1.m = 500

    if cloud2.m + 50 < 0:
        cloud2.m = 500

    if cloud3.m + 50 < 0:
        cloud3.m = 500

    if food.p < 0:
        food.p = 500
        food.number += 1
    pygame.time.delay(20)
    win.fill((0, 0, 0))
    win.blit(text_surface, dest=(20, 20))
    food.draw(win)
    agent.draw(win)
    cloud1.draw(win)
    cloud2.draw(win)
    cloud3.draw(win)
    pygame.display.update()



