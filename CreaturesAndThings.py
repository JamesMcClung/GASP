#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 14:08:56 2020

@author: Emily
"""
from cnst import *
import GUI
import random

class Thing():
    def __init__(self, **args):
        #kwargs x, y, th, crossable, shape, length, width
        self.th = args.get("th", 0)
        self.length = args.get("length", 20)
        self.width = args.get("width", 20)
        self.size = args.get("size", [20])
        self.crossable = args.get("crossable", False)
        self.colorFill = args.get("colorFill", 'red')
        self.colorOutline = args.get("colorOutline", 'blue')
        self.shape = args.get("shape", CIRCLE)
        self.exists = True
        self.x = args.get("x", random.randint(0,WINWIDTH))
        self.y = args.get("y", random.randint(0,WINHEIGHT))
        
        self.gobject = GUI.makeGraphicsObject(self.colorFill, self.colorOutline, self.shape, self.size, self.x, self.y)
            
    def intersects(self, thing):
        return abs(thing.x-self.x) < 5 and abs(thing.y-self.y) < 5
    
    def updateGobject(self):
        self.gobject.undraw()
        self.gobject = GUI.makeGraphicsObject(self.colorFill, self.colorOutline, self.shape, self.size, self.x, self.y)
        GUI.drawAllIn([self])

class Tickable(Thing):
    
    def __init__(self, **args):
        super().__init__(**args)
        self.environment = None
        self.time = 0
    
    def tick(self, dt, env):
        self.environment = env
        self.time = dt
        

class Creature(Tickable):
    
    def __init__(self, traits, **args):
        #Kwargs traits
        super().__init__(**args)
        self.reproductionRate = .5
        self.mutationRate = .05
        self.energy = 10
        self.traits = {"reproductionRate":self.reproductionRate, "mutationRate":self.mutationRate, "energy":self.energy}
        for key, val in traits.items():
            self.traits[key] = val
            
    def start(self):
        pass
    
    def tick(self, dt, environment):
        super().tick(dt, environment)
        
    def end(self):
        pass
   
    def meetThing(self, other):
        pass
       
    def reproduce(self):
        pass
    
    def swim(self):
        pass
    
    def burrow(self):
        pass
    
    def walk(self):
        pass
    
    def getWorld(self):
        return self.environment
    
    def isWalkable(self, x, y):
        return x >= 0 and x <= WINWIDTH and y >= 0 and y <= WINHEIGHT
     
class exampleCreature(Creature):
    pass
