

import pygame
import snakeObject
import random


pygame.init()
pygame.font.init()

winX = 450
winY = 450

window = pygame.display.set_mode((winX, winY))
pygame.display.set_caption("Pysnake")

font = pygame.font.Font("freesansbold.ttf", 20)
text = font.render("Move to start", True, (0, 0, 255))
textRect = text.get_rect()
textRect.center = (winX // 2, winY // 3)

def generatePosition(direction, gridX, gridY): # 0 - x, 1 - y
    openX,openY = [], []
    for i in range(len(gridX)):
        if gridX:
            openX.append(i)
        if gridY:
            openY.append(i)
    newPosition = random.choice(openY) * height
    if direction == 0: 
        newPosition = random.choice(openX) * width

    return newPosition

def mainMenu():
    window.fill((0,0,0))
    window.blit(text, textRect)
    pygame.draw.rect(window,(255,0,0), (x, y, width, height))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        keys = pygame.key.get_pressed()
        if any(keys):
            break;

def paused():
    text = font.render("Space to Resume", True, (255,0,0))
    textRect.center = (winX // 2, winY // 2)
    window.fill((0,0,0))
    window.blit(text,textRect)
    pygame.draw.rect(window,(255,0,0), (x,y,width, height))
    for each in head.body: 
        pygame.draw.rect(window, (255,0,0), (each[0], each[1], width, height))
    pygame.draw.rect(window, (255,208,0), (itemX, itemY, width, height))
    pygame.display.update()

    pygame.time.delay(100)

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            break;

#constants and variables

x = 0 
y = 0 
width = 15
height = 15
speed = 15
head = snakeObject.Snake([x,y], width, height)

#directions

up, down, left, right = 0, 0, 0, speed

#item creation

gridX, gridY = [True] * (winX // width), [True]  * (winY // height)
itemX, itemY = generatePosition(0, gridX, gridY), generatePosition(1, gridX, gridY)

alive = True

#start
mainMenu()

while alive: 
    pygame.time.delay(80)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        up, down, left, right = 0,0,0,0
        up -= speed
    if keys[pygame.K_LEFT]: 
        up, down, left, right = 0,0,0,0
        left -= speed
    if keys[pygame.K_DOWN]: 
        up, down, left, right = 0,0,0,0
        down = speed
    if keys[pygame.K_RIGHT]: 
        up, down, left, right = 0,0,0,0
        right = speed    
    if keys[pygame.K_p]:
        paused()
    
    #moves
    x = (x + left + right) % winX
    y = (y + up + down) % winY

    #currentDirection
    currDirection = -1
    if left + right == 0 and up + down < 0:
        currDirection = 0
    elif left + right == 0 and up + down > 0: 
        currDirection = 1
    elif up + down == 0 and left + right < 0:
        currDirection = 2
    elif up + down == 0 and left + right > 0: 
        currDirection = 3
    
    #snake

    gridX, gridY = [True] * (winX // width), [True] * (winY // height)
    bodyLength = head.getLength() - 1
    snakeX, snakeY = [x // width], [y // height]
    gridX[x // width] = False
    gridY[y // width] = False
    
    for i in range(bodyLength):
        snakeX.append(head.body[i][0] // width)
        snakeY.append(head.body[i][1] // height)
        gridX[head.body[i][0] // width] = False
        gridY[head.body[i][1] // height] = False

    #end game 

    for i in range(bodyLength):
        if abs(x - head.body[i][0]) < width and abs(y - head.body[i][1]) < height:    
            alive = False
    
    if not alive: 
        break; 

    head.updatePos(x,y)

    #eat items

    if abs(x-itemX) < width and abs(y-itemY) < height:
        head.grow(currDirection, winX, winY)
        itemX, itemY = generatePosition(0,gridX,gridY), generatePosition(1,gridX,gridY)
    
    window.fill((0,0,0))

    #item
    pygame.draw.rect(window, (255,208,0), (itemX,itemY, width, height))

    #draw snake

    pygame.draw.rect(window, (255,0,0), (x, y, width, height))
    for each in head.body:
        pygame.draw.rect(window, (255, 0, 0), (each[0], each[1], width, height))
    pygame.display.update()

# end game

text = font.render("You Lost...", True, (0, 0, 255)) 
textRect.center = (winX // 3, winY // 3)
window.fill((0, 0, 0))
window.blit(text, textRect)
window.blit(text, textRect)
for each in head.body:
    pygame.draw.rect(window, (255, 0, 0), (each[0], each[1], width, height))
pygame.draw.rect(window, (255, 208, 0), (itemX, itemY, width, height))
pygame.display.update()


pygame.quit()


