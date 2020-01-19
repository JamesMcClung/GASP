#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 14:08:56 2020

@author: Emily
"""

class Thing():
    def __init__(self, x = 0, y = 0, th = 0, crossable  = True):
        if x and y: 
            self.x = x
            self.y = y
            self.th = th
            self.length
            self.width
            self.crossable = crossable
            
    def intersects(self, thing):
        pass

class Tickable(Thing):
    
    def __init__(self, x = None, y = None, th = None, crossable = True):
        super.__init__(x = x, y = y, th = th, crossable = crossable)
        self.environment = None
        self.time = 0
    
    def tick(self, dt, env):
        self.environment = env
        self.time = dt
        

class Creature(Tickable):
    
    def __init__(self, traits, x = 0, y = 0, crossable  = True):
        super.__init__(x = x, y = y, crossable = crossable)
        self.traits = [self.reproductionRate, self.mutationRate, self.energy] + traits
   
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
    

     
class exampleCreature(Creature):
    pass
