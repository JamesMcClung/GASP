#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 20:13:12 2020

@author: Emily
"""

from CreaturesAndThings import Creature as framework
import random


class Rabbit(framework):
    def __init__(self):
        super().__init__({"speed": 10}, colorFill = "brown", length = 10, width = 10, size = [10])
        
    def walk(self):
        dx = random.randint(-1,1)*self.traits["speed"]
        dy = random.randint(-1, 1)*self.traits["speed"]
        self.gobject.move(dx, dy)
        
    def tick(self, dt, environment):
        self.walk()
        super().tick(dt, environment)
        
        
class Fox(framework):
    def __init__(self):
        super().__init__({"speed": 5}, colorFill = "brown", length = 20, width = 10, size = [20])
        
    def walk(self):
        dx = random.randint(-1,1)*self.traits["speed"]
        dy = random.randint(-1, 1)*self.traits["speed"]
        self.gobject.move(dx, dy)
        
    def tick(self, dt, environment):
        self.walk()
        super().tick(dt, environment)