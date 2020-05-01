#Evolution

#imports 
from pprint import pprint
from itertools import count
import random

class Field():
    field = [[0 for i in range(25)] for j in range(50)]    #creating matrix 25x50
    
    def food(self):                                         #rozkładaie "jedzenia"
        global field
        for i in range(80):
            empty = True
            while empty:
                x = random.randint(0,49)
                y = random.randint(1,24)
                if pole.field[x][y] != 1:
                    pole.field[x][y] = 1
                    empty = False
                else:
                    pass
    def clear(self):
        global field
        pole.field = [[0 for i in range(25)] for j in range(50)]

class Animal():
    
    _ids = count(10)
    
    def __init__(self, nr, lifespan = 30, speed = 2):
        self.nr = nr
        self.evolve = random.randint(-3,3)
        self.lifespan = lifespan + self.evolve
        self.old_lifespan = self.lifespan
        self.speed = round(speed - 0.3 *self.evolve)
        if self.speed == 0:
            self.speed = 1 
        self.old_speed = self.speed
        self.food = 0
        self.x = 0
        self.alive = True
        populated = True
        while populated:
            y_pop = random.randint(0,49)
            if pole.field[y_pop][0] == 0:
                self.y = y_pop
                self.y_pop = y_pop
                pole.field[y_pop][0] = 'o'
                populated = False
    
    def move(self):
        if self.alive == True:
            for i in range(0,self.speed):
                self.direction = random.randint(1,4)
                if self.direction == 1 and self.lifespan > 0 and self.x <= 23:   #prawo
                    self.x += 1
                    self.lifespan -= 1
                    if pole.field[self.y][self.x] == 1:
                        self.food += 1
                    pole.field[self.y][self.x]='-'

                elif self.direction == 2 and self.lifespan > 0 and self.x >= -24:      #lewo
                    self.x -= 1
                    self.lifespan -= 1
                    if pole.field[self.y][self.x] == 1:
                        self.food += 1
                    pole.field[self.y][self.x]='-'

                elif self.direction == 3 and self.lifespan > 0 and self.y >= -49:      #góra
                    self.y -= 1
                    self.lifespan -= 1
                    if pole.field[self.y][self.x] == 1:
                        self.food += 1
                    pole.field[self.y][self.x]='-'

                elif self.direction == 4 and self.lifespan > 0 and self.y <= 48:      #dół
                    self.y -= 1
                    self.lifespan -= 1
                    if pole.field[self.y][self.x] == 1:
                        self.food += 1
                    pole.field[self.y][self.x]='-'
          
    def die(self):
        self.alive = False
        
    def reset(self):
        self.lifespan = self.old_lifespan
        self.x = 0
        self.y = self.y_pop

    def multiplicate(self):
        self.id = next(self._ids)
        animals.append(Animal(nr = self.id, lifespan = self.old_lifespan, speed = self.old_speed))

    def get_stats(self):
        #print('Name: ', self.name, 'Lifespan = ', self.lifespan, 'Speed = ', self.speed)
        return self.name, self.lifespan, self.speed

#class Gameplay():
    
#    def __init__(self):
pole = Field()
animals = [Animal(x) for x in range(1,11)]    

statystyki = []
for i in range(10):
    print('tura:', i)
    pole.food()#rozrzut jedzenia
    for j in range(50):   #do poprawy
        for animal in animals:
            animal.move()   #ruch
            #print(animal.nr,'ruszyl')
            
    for animal in animals:
        
        if animal.food == 0:
            animal.die()
        elif animal.food == 1:
            animal.reset()
        elif animal.food > 1:
            animal.multiplicate()
            animal.reset()
    
    pole.clear()#
    for animal in animals:
        if animal.alive == True:
            statystyki.append([animal.nr,animal.alive,animal.old_lifespan,animal.old_speed, animal.food])
    statystyki.append(['Tura:       ', i])
    for animal in animals:
        animal.food = 0

pprint(statystyki)


#rozrzut jedzenia
#populacja
#pętla:
#	ruch_mały x lifespan
#	sprawdzenie:
#		2 multip
#		1 nic
#		0 smierc
#	aktuaizacja zwierzat


#for animal




#for i in range(50):   # do poprawy
#    for animal in animals:
#        animal.move()
        
#    def inner_play(self):
#        pass
#animals[4].multiplicate(4)        
#game = Gameplay()        
#print(animals[20])


# =============================================================================
# print(pole.field)
# pole.food()
# pprint(pole.field)
#     
#     
#     
#     
#     """ This class represents an instance of the game. If we need to
#         reset the game we'd just need to create a new instance of this
#         class. """
#     
#     
#     
# =============================================================================
    
    
    
    
    
    
    
