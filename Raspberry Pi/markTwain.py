'''
"I must have a prodigious amount of mind;
it takes me as much as a week, sometimes, to make it up!""

- Mark Twain
'''
import pygame as p
import sys
import math
size = (720,420)
window = p.display.set_mode(size)

def eventhandle():
    for event in p.event.get():
		if event.type == p.QUIT:
			sys.exit()

def main():
    delay = 1000
    window = p.display.set_mode(size)
    mytrack = Track()

    while True:
        eventhandle()
        mytrack.draw()

        p.display.flip()
        p.time.wait(delay)

#used to keep track of position
class Pos(object):
    def __init__(self, pos):
        self.pos = pos

#The track the car drives on
class Track(object):
    def __init__(self):
        self.surface = p.Surface(size)
        self.surface.fill((0,0,0))
        p.draw.rect(self.surface,(255,0,0),(0,0,size[0],size[1]),10)
        p.draw.rect(self.surface,(255,0,0),(160,160,400,100))
    def draw(self):
        window.blit(self.surface,(0,0))

class Car(object):
    posX = 0
    posY = 1
    def __init__(self,pos):
        #force floats as pos
        self.pos = map(float,pos)
        self.compass = Compass(self)
        #currently always faces upwards
        self.prevPos = (pos[posX],pos[posY]-1)

    def getData(self,pos):
        pass

    def goto(self,newPos):
        self.pos = newPos

    def pos():
        doc = "The pos property."
        def fget(self):
            return self._pos
        def fset(self, value):
            self.prevPos = self.pos
            self._pos = value
        def fdel(self):
            del self._pos
        return locals()
    pos = property(**pos())

class Compass(object):
    def __init__(self,car):
        #create fictive pos based on car pos
        self.car = car
    def getData(self):
        a_x,a_y = self.car.pos
        b_x,b_y = self.car.prevPos
        #vektor b->a
        c_x,c_y = a_x-b_x, b_x-b_y
        #angle between vectors
        cosV=c_x/(c_x**2+c_y**2)
        


if __name__ == "__main__":
    main()
