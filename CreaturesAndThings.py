#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 14:08:56 2020

@author: Emily
"""
from cnst import *
import GUI

class Thing():
    def __init__(self, **args):
        #kwargs x, y, th, crossable, shape, length, width
        self.x = args.get("x", 0)
        self.y = args.get("y", 0)
        self.th = args.get("th", 0)
        self.length = args.get("length", 20)
        self.width = args.get("width", 20)
        self.size = args.get("size", [20])
        self.crossable = args.get("crossable", False)
        self.colorFill = args.get("colorFill", RED)
        self.colorOutline = args.get("colorOutline", BLUE)
        self.shape = args.get("shape", CIRCLE)
        self.gobject = GUI.makeGraphicsObject(self.colorFill, self.colorOutline, self.shape, self.size, self.x, self.y)
        self.exists = True
            
    def intersects(self, thing):
        pass

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
            
    def tick(self, dt, environment):
        super().tick(dt, environment)
   
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
