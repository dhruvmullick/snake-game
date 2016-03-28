__author__ = 'dhruvmullick'
import pygame,sys,random
from pygame.locals import *
from variables import *
from snakeclass import *

pygame.init()

clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Snake')


def exitgame(score):
    gameDisplay.fill(white)
    largeText=pygame.font.SysFont("cambria",50)
    TextSurf, TextRect = text_objects("Your Final Score is "+str(score),largeText)
    TextRect.center = ((display_width/2,display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()
    pygame.mixer.music.stop()

    pygame.time.wait(1000)
    pygame.quit()
    sys.exit()

def text_objects(text, font):           #USED TO SIMPLIFY CREATING TEXT FIELDS
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def button(msg,x,y,w,h,ic,ac,action=None):  #BUTTON ON THE INTRO SCREEN

    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()

    print(click)

    if(x<mouse[0]<x+w and y<mouse[1]<y+h):
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))    #AC IS THE ACTIVE COLOUR OF THE BUTTON

        if(click[0]==1 and action!=None):
            action()

    else :
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))  #IC - INACTIVE COLOUR OF THE BUTTON

    smallText = pygame.font.SysFont("calibri",20)
    textSurf, textRect = text_objects(msg,smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)


def mainmenu():
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                exitgame()
        gameDisplay.fill(white)
        largeText=pygame.font.SysFont("cambria",100)
        TextSurf, TextRect = text_objects("Snake Game!",largeText)
        TextRect.center = ((display_width/2,display_height/2))
        gameDisplay.blit(TextSurf,TextRect)

        button("Play the game!",150,450,100,50,green,bright_green,startgame)
        button("Quit",400,450,100,50,red,bright_red,exitgame)

        pygame.display.update()

def startgame():

    gameDisplay.fill(bright_green)
    mysnake = Snake()   #SNAKE OBJECT
    score=0
    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.play(-1)

    mousex=random.randint(0,arena_width) #X COORDINATE OF MOUSE
    mousey=random.randint(0,arena_height)   #Y COORDINATE OF MOUSE

    mouse=pygame.image.load('mouse.png')

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                exitgame()
            elif event.type==KEYDOWN:
                if event.key==K_RIGHT:
                    mysnake.changedir(0)    #DIRECTIONS ARE IN TERMS OF DEGREES. 0 FOR RIGHT. 90 FOR UP. 180 FOR LEFT.
                elif event.key==K_UP:
                    mysnake.changedir(90)
                elif event.key==K_LEFT:
                    mysnake.changedir(180)
                elif event.key==K_DOWN:
                    mysnake.changedir(270)

        gameDisplay.fill(bright_green)

        gameDisplay.blit(mouse,(mousex,mousey))

        for i in range(len(mysnake.xs)):
            pt=pygame.Surface((tile_width,tile_width))
            pt.fill(brown)
            gameDisplay.blit(pt,(mysnake.xs[i],mysnake.ys[i]))  #XS AND YS REPRESENT THE X AND Y COORDINATES OF THE DIFFERENT TILES IN THE SNAKE BODY
                                    #WE DISPLAY EVERY TILE IN THE SNAKE BODY
        if mysnake.arenacollision():    #CHECK FOR ARENA COLLISION
            exitgame(score)

        if mysnake.selfcollision():     #CHECK FOR COLLISION WITH SELF
            exitgame(score)

        if mysnake.eatapple(mousex,mousey):     #IF IT HAS COLLIDED WITH A MOUSE
            mysnake.grow()      #INCREASE SNAKE SIZE
            mousex = random.randint(50,arena_width-50)  #ASSIGN NEW POSITION TO MOUSE
            mousey = random.randint(50,arena_height-50)
            score+=len(mysnake.xs)*5

        mysnake.move()      #MOVE THE SNAKE
        scoreText=pygame.font.SysFont("calibri",20)
        scoreSurf, scoreRect = text_objects("Your Score is : "+ str(score),scoreText)
        scoreRect.center = ((arena_width/2,50))
        gameDisplay.blit(scoreSurf,scoreRect)


        pygame.display.update()

        clock.tick(10)


mainmenu()