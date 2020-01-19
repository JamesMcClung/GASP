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

def begin(height, width):
    global start, win
    start = True
    win  = GraphWin('GASP', width, height)
    
def makeGraphicsObject(colorFill, colorOutline, shape, size, x, y):
    pt = Point(x, y)
    if shape == CIRCLE:
        img = Circle(pt, *size)
    else:
        pass #draw a polygon
    img.setOutline(colorOutline)
    img.setFill(colorFill)
    return img

def updateAll(things):
    if not start:
        print("Error: graphics not started before trying to rendor")
        return
    
    for thing in things:
        thing.gobject.draw(win)
        
def waitForClick():
    win.getMouse()
        
def close():
    win.close()
