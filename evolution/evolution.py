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
    
    def __init__(self, nr, lifespan = 30, speed = 2, food = 0):
        self.nr = nr
        self.evolve = random.randint(-3,3)
        self.lifespan = lifespan + self.evolve
        self.old_lifespan = self.lifespan
        self.speed = round(speed - 0.3 *self.evolve)
        if self.speed == 0:
            self.speed = 1 
        self.old_speed = self.speed
        self.food = food
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
                if self.direction == 1 and self.lifespan > 0 and self.x <= 23 and pole.field[self.y][self.x+1] != '-':   #prawo
                    self.x += 1
                    self.lifespan -= 1
                    if pole.field[self.y][self.x] == 1:
                        self.food += 1
                    pole.field[self.y][self.x]='-'

                elif self.direction == 2 and self.lifespan > 0 and self.x >= -24 and pole.field[self.y][self.x-1] != '-':      #lewo
                    self.x -= 1
                    self.lifespan -= 1
                    if pole.field[self.y][self.x] == 1:
                        self.food += 1
                    pole.field[self.y][self.x]='-'

                elif self.direction == 3 and self.lifespan > 0 and self.y >= -49 and pole.field[self.y-1][self.x] != '-':      #góra
                    self.y -= 1
                    self.lifespan -= 1
                    if pole.field[self.y][self.x] == 1:
                        self.food += 1
                    pole.field[self.y][self.x]='-'

                elif self.direction == 4 and self.lifespan > 0 and self.y <= 48 and pole.field[self.y+1][self.x] != '-':      #dół
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
        #print(self.id)
        animals.append(Animal(nr = self.id, lifespan = self.old_lifespan, speed = self.old_speed, food=1))
        print(len(animals))

    def get_stats(self):
        #print('Name: ', self.name, 'Lifespan = ', self.lifespan, 'Speed = ', self.speed)
        return self.name, self.lifespan, self.speed

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
            
    for animal in animals:#tu jest błąd nowy 
        if animal.food == 0:
            animal.die()
        elif animal.food == 1:
            animal.reset()
        elif animal.food > 1:
            animal.multiplicate()
            animal.reset()
    #pprint(pole.field)
    pole.clear()#
    for animal in animals:
        if animal.alive == True:
            statystyki.append([animal.nr,animal.alive,animal.old_lifespan,animal.old_speed, animal.food])
    statystyki.append(['Tura:       ', i])
    for animal in animals:
        animal.food = 0

pprint(statystyki)
print(len(animals))
print(animals[24].alive)







