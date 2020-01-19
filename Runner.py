#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 20:19:13 2020

@author: Emily
"""

import CreaturesAndThings
import GUI
import time
import foxAndRabbit as population

things = []

GUI.begin()

for i in range(10):
    things.append(population.Rabbit())
    
for i in range(2):
    things.append(population.Fox())
    
GUI.drawAllIn(things)
    
for i in range(1000):
    for thing in things:
        if not thing.exists:
            things.remove(thing)
            thing.gobject.undraw()
        else:
            thing.tick(0,0)
    newThings = []
    for i in range(0,len(things)):
        for j in range(i+1, len(things)):
            if things[i].intersects(things[j]):
                r1 = things[i].meetThing(things[j])
                r2 = things[j].meetThing(things[i])
                if type(r1) == type(r2):
                    None if not r1 else newThings.append(r1)
                else:
                    None if not r1 else newThings.append(r1)
                    None if not r2 else newThings.append(r2)
                    
    GUI.drawAllIn(newThings)
    things += newThings
    
#    GUI.forceUpdate()
    
    time.sleep(.01)
    
GUI.waitForClick()
GUI.close()