# This script can be executed to run the program.

import CreaturesAndThings
import GUI
import time
import foxAndRabbit as population
import traceback

things = []

GUI.begin()

#make things
for i in range(10):
    things.append(population.Rabbit())
    
for i in range(2):
    things.append(population.Fox())
    
#handles making things happen
#starts things
for thing in things:
    thing.start()

#closes window if something goes wrong
try:
    #draws initial positions
    GUI.drawAllIn(things)

    while(True):
        #ticks things
        for thing in things:
            if not thing.exists:
                things.remove(thing)
                thing.gobject.undraw()
            else:
                thing.tick(0,0)
        
        #meets things
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
        
        #draws and adds new things
        GUI.drawAllIn(newThings)
        things += newThings
        
        #this doesn't work
        click = GUI.checkClick()
        if click:
            break
        
except Exception as e: 
    #print all errors
    traceback.print_exc()
    print(e)

GUI.close()