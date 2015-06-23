__author__ = 'dhruvmullick'

import pygame, sys
from pygame.locals import *
from variables import *

class Snake:
                                #XS[0] IS THE SNAKE'S HEAD'S X COORDINATE
    xs=[100,120,140,160]        #X COORDINATES OF THE TILES OCCUPIED BY SNAKE
    ys=[100,100,100,100]
    dir = 0 #0, 90, 180, 270

    def changedir(self,dir):
        if(abs(self.dir-dir)==180): #opposite dir
            return
        self.dir=dir

    def grow(self):         #ADD A NEW TILE TO SNAKE'S BODY
        self.xs.append(100) #100 IS A RANDOM VALUE. ON MOVING, WE ASSIGN XS[i]=XS[i-1], SO IT DOESN'T MATTER WHAT VALUE WE APPEND INITIALLY
        self.ys.append(100)

    def move(self):
        for i in range(len(self.xs)-1,0,-1):
            self.xs[i]=self.xs[i-1] #MOVE THE SNAKE
            self.ys[i]=self.ys[i-1]

        if self.dir==0:
            self.xs[0]=self.xs[0]+tile_width    #CREATE A TILE TO THE RIGHT OF THE SNAKE'S HEAD
        elif self.dir==90:
            self.ys[0]=self.ys[0]-tile_width
        elif self.dir==180:
            self.xs[0]=self.xs[0]-tile_width
        elif self.dir==270:
            self.ys[0]=self.ys[0]+tile_width

    def collide(self,x1,y1,x2,y2):
        if abs(x1-x2)<tile_width and abs(y1-y2)<tile_width:
            return True
        else :
            return False

    def eatapple(self,x,y):
        if self.collide(self.xs[0],self.ys[0],x,y):
            return True
        else:
            return False

    def selfcollision(self):
        for i in range(1,len(self.xs)):
            if self.collide(self.xs[0],self.ys[0],self.xs[i],self.ys[i]):
                return True
        return False

    def arenacollision(self):           # CAN CHANGE TO SIMPLE < and > conditons
        if self.collide(self.xs[0],self.ys[0],self.xs[0],0):
            return True
        elif self.collide(self.xs[0],self.ys[0],self.xs[0],arena_height):
            return True
        elif self.collide(self.xs[0],self.ys[0],0,self.ys[0]):
            return True
        elif self.collide(self.xs[0],self.ys[0],arena_width,self.ys[0]):
            return True
        else:
            return False