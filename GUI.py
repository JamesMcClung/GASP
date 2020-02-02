#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 17:54:41 2020

@author: Emily
"""
from graphics import *
from cnst import *
import CreaturesAndThings as t

start = False

def begin():
    global start, win
    start = True
    win  = GraphWin('GASP', WINWIDTH, WINHEIGHT)
    
def makeGraphicsObject(colorFill, colorOutline, shape, size, x, y):
    if not start:
        print("Error: graphics not started before trying to rendor")
        return
    pt = Point(x, y)
    if shape == CIRCLE:
        img = Circle(pt, *size)
    else:
        pass #draw a polygon
    img.setOutline(colorOutline)
    img.setFill(colorFill)
    return img

def forceUpdate():
    update()
    
def drawAllIn(things):
    for thing in things:
        thing.gobject.draw(win)

def waitForClick():
    win.getMouse()
    
def checkClick():
    win.checkMouse()
        
def close():
    win.close()
