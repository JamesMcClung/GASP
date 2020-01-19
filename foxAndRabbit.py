#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 20:13:12 2020

@author: Emily
"""

from CreaturesAndThings import Creature as framework
import random
from math import cos, sin, pi
import random



class Rabbit(framework):
    def __init__(self, **args):
        super().__init__({"speed": 10, "age": 0}, colorFill = "gray", length = 10, width = 10, size = [5], **args)
        self.dx = 0
        self.dy = 0
        self.angle = 0
        
    def walk(self):
        #probably that it takes a random turn
        turn = random.random() < .1
        maxSpeed = self.traits["speed"]
        
        #if the point is walkable, the thing should move there
        if self.isWalkable(self.x+self.dx, self.y+self.dy):
            self.gobject.move(self.dx, self.dy)
            self.x += self.dx
            self.y += self.dy
        else: 
            turn = True
        
        #if take a random turn, pick a random new angle
        if turn:
            self.angle = random.random() * 2 * pi
        
        #change the angle a bit every time at random
        self.angle += (random.random()-.5)
        self.dx = maxSpeed * cos(self.angle)
        self.dy = maxSpeed * sin(self.angle)
        
    def tick(self, dt, environment):
        self.walk()
        self.traits["age"]+=1
        if self.traits["age"] == 50:
            self.size = [10]
            self.updateGobject()
        super().tick(dt, environment)
        
    def meetThing(self, thing):
        if isinstance(thing, Rabbit):
            if self.traits["age"] > 50 and thing.traits["age"] > 50:
                return Rabbit(x = self.x, y = self.y)
            
        
        
class Fox(framework):
    def __init__(self, **args):
        super().__init__({"speed": 5, "age":0}, colorFill = "orange", length = 20, width = 10, size = [10], **args)
        self.dx = 0
        self.dy = 0
        self.angle = 0
        
    def walk(self):
        #probably that it takes a random turn
        turn = random.random() < .1
        maxSpeed = self.traits["speed"]
        
        #if take a random turn, pick a random new angle
        if turn:
            self.angle = random.random() * 2 * pi
        
        #change the angle a bit every time at random
        self.angle += (random.random()-.5)
        self.dx = maxSpeed * cos(self.angle)
        self.dy = maxSpeed * sin(self.angle)
        
        #if the point is walkable, the thing should move there
        if self.isWalkable(self.x+self.dx, self.y+self.dy):
            self.gobject.move(self.dx, self.dy)
            self.x += self.dx
            self.y += self.dy
        
    def tick(self, dt, environment):
        self.walk()
        self.traits["age"]+=1
        if self.traits["age"] == 100:
            self.size = [15]
            self.updateGobject()
        super().tick(dt, environment)
        
    def meetThing(self, thing):
        if isinstance(thing, Rabbit):
            thing.exists = False
        elif isinstance(thing, Fox):
            if self.traits["age"] > 100 and thing.traits["age"] > 100:
                return Fox(x= self.x, y = self.y)
            