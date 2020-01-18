class Environment:
    def __init__(self):
        self.things = []
        self.tickables = []
        self.time = 0
    
    def tick(self, dt: float):
        """Ticks every tickable, then handles collisions.\n
        dt: how much time to elapse (a small float)"""
        self.time += dt
        for tickable in tickables:
            tickable.tick(dt, self)
        
        # handle collisions by checking if every pair of things intersects
        for i, thing1 in enumerate(things):
            for thing2 in things[i+1:]
            if thing1.intersects(thing2):
                self.collide(thing1, thing2)
    
    def collide(self, thing1, thing2):
        # faster thing gets to interact first
        pass
    


    def addThing(self, thing):
        """Adds the specified thing to the world."""
        self.things.append(thing)
        if isinstance(thing, Tickable):
            self.tickables.append(thing)