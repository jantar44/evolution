#Evolution
"""
Created on %(03.05.2020)s
@author: %(Jan)s
"""
#imports
from pprint import pprint
from itertools import count
import random
import numpy as np

class Field:
    """
    This is a class for creating and operating on field and food distribution.

    Attributes:
        field (list): Matrix 2D representing field 25x50.
    """
    field = np.zeros((50, 25), dtype=int)

    @classmethod
    def food(cls):
        """
        Class function for Field class.
        Function is populting field with 1 representing food.

        Parameters:
           None
        """

        for _i in range(80):
            empty = True
            while empty:
                x_cor = random.randint(1, 24)
                y_cor = random.randint(0, 49)
                if POLE.field[y_cor, x_cor] != 1:
                    POLE.field[y_cor, x_cor] = 1
                    empty = False
                else:
                    pass
    @classmethod
    def clear(cls):
        """
        Class function for Field class.
        Function is clearing field by inserting everywhere 0.

        Parameters:
           None
        """
        POLE.field = np.zeros((50, 25), dtype=int)

class Animal:
    """
    This is a class for creating "Animals".

    Attributes:
        _ids (iter): itertools
        id_animal (int): individual number representing instance.
        lifespan (int): value representing amount of movements overall.
        old_lifespan (int): initial lifespan
        speed (int): value representing amount of movements in the round.
        old_speed (int): initial speed
        food (int): value representing number of points collected.
        evolve (int): value between <-3,3> representing variations in speed and lifespan.
        alive (boolean): state of animal.
        coordiates (list): list containing coordination points x_cor, y_cor, y_pop.
        x_cor (int): x coordinate of animal.
        y_cor (int): y coordinate of animal.
        y_pop (int): starting y coordinate.
    """

    _ids = count(1)

    def __init__(self, lifespan=30, speed=2, food=0):
        """
        The constructor for Animal class.

        Parameters:
            id_animal (int): individual number representing instance.
            lifespan (int): value representing amount of movements overall.
            old_lifespan (int): initial lifespan
            speed (int): value representing amount of movements in the round.
            old_speed (int): initial speed
            food (int): value representing number of points collected.
            evolve (int): value between <-3,3> representing variations in speed and lifespan.
            alive (boolean): state of animal.
            coordiates (list): list containing coordination points x_cor, y_cor, y_pop.
            x_cor (int): x coordinate of animal.
            y_cor (int): y coordinate of animal.
            y_pop (int): starting y coordinate.
        """
        self.id_animal = next(self._ids)
        self.evolve = random.randint(-3, 3)
        self.lifespan = lifespan + self.evolve
        self.old_lifespan = self.lifespan
        self.speed = round(speed - 0.3 *self.evolve)
        if self.speed == 0:
            self.speed = 1
        self.old_speed = self.speed
        self.food = food
        self.alive = True
        self.coordiates = [self.populate()]

    def populate(self):
        """
        Method of the Animal class populating field with instance of Animal class.

        Parameters:
            x_cor (int): x coordinate of animal set to 0.
            y_cor (int): y coordinate of animal randomly chosen on empty place.
            y_pop (int): starting y coordinate.
            empty (boolean): variable used to check if field is empty.
        """
        self.x_cor = 0
        empty = False
        while not empty:
            y_pop = random.randint(0, 49)
            if POLE.field[y_pop, 0] == 0:
                self.y_cor = y_pop
                self.y_pop = y_pop
                POLE.field[y_pop, 0] = 3
                empty = True
        return self.x_cor, self.y_cor, self.y_pop

    def move(self):
        """
        Method of the Animal class moving the animal.

        Parameters:
            x_cor (int): x coordinate of animal set to 0.
            y_cor (int): y coordinate of animal randomly chosen on empty place.
            y_pop (int): starting y coordinate.
            direction (int): random number <1,4> representing direction.
            empty (boolean): variable used to check if field is empty.
            lifespan (int): value representing amount of movements overall.

        """

        if self.alive is True:
            for _i in range(0, self.speed):
                self.direction = random.randint(1, 4)

                if self.direction == 1 and self.lifespan > 0 \
                and self.x_cor <= 23 and POLE.field[self.y_cor, self.x_cor+1] != 2:#prawo
                    self.x_cor += 1
                    self.lifespan -= 1
                    if POLE.field[self.y_cor, self.x_cor] == 1:
                        self.food += 1
                    POLE.field[self.y_cor, self.x_cor] = 2

                elif self.direction == 2 and self.lifespan > 0 and \
                self.x_cor >= -24 and POLE.field[self.y_cor, self.x_cor-1] != 2: #lewo
                    self.x_cor -= 1
                    self.lifespan -= 1
                    if POLE.field[self.y_cor, self.x_cor] == 1:
                        self.food += 1
                    POLE.field[self.y_cor, self.x_cor] = 2

                elif self.direction == 3 and self.lifespan > 0 and \
                self.y_cor >= -49 and POLE.field[self.y_cor-1, self.x_cor] != 2:  #góra
                    self.y_cor -= 1
                    self.lifespan -= 1
                    if POLE.field[self.y_cor, self.x_cor] == 1:
                        self.food += 1
                    POLE.field[self.y_cor, self.x_cor] = 2

                elif self.direction == 4 and self.lifespan > 0 and \
                self.y_cor <= 48 and POLE.field[self.y_cor+1, self.x_cor] != 2:    #dół
                    self.y_cor -= 1
                    self.lifespan -= 1
                    if POLE.field[self.y_cor, self.x_cor] == 1:
                        self.food += 1
                    POLE.field[self.y_cor, self.x_cor] = 2

                else:
                    break

    def die(self):
        """
        Method of the Animal class killing animal.

        Parameters:
            alive (boolean): variable is set to False.
        """

        self.alive = False

    def reset(self):
        """
        Method of the Animal class reseting atributes of animal.

        Parameters:
            lifespan (int): Parameter is set to initial value.
            speed (int):  Parameter is set to initial value.
            x_cor (int):  Parameter is set to initial value.
            y_cor (int):  Parameter is set to initial value.
        """

        self.lifespan = self.old_lifespan
        self.speed = self.old_speed
        self.x_cor = 0
        self.y_cor = self.y_pop

    def multiplicate(self):
        """
        Method of the Animal class creating multiplication of instance.

        Parameters:
            lifespan (int): value representing amount of movements overall.
            speed (int): value representing amount of movements in the round.
            food (int):  Parameter is set to 1.
        """

        ANIMALS.append(Animal(lifespan=self.old_lifespan, \
                              speed=self.old_speed, food=1))

    def check_food(self):
        """
        Method of the Animal class checking results of a round.

        Parameters:
            food (int): value representing number of points collected.
        """

        if self.food == 0:
            Animal.die(self)
        elif self.food == 1:
            Animal.reset(self)
        elif self.food > 1:
            Animal.multiplicate(self)
            Animal.reset(self)

def get_statistics():
    """
    Method returning basic statistics.
    """

    STATISTICS.append(['Tura:       ', i+1])
    for animal in ANIMALS:
        if animal.alive is True:# or animal.alive is False:
            STATISTICS.append([animal.id_animal, animal.alive, animal.old_lifespan, \
                               animal.old_speed, animal.food])
    return STATISTICS

if __name__ == "__main__":
    POLE = Field()
    ANIMALS = [Animal() for x in range(1, 11)]
    STATISTICS = []
    for i in range(70):
        print(i)
        POLE.food()#rozrzut jedzenia
        for j in range(40):   #do poprawy
            for animal in ANIMALS:
                animal.move()   #ruch

        for animal in ANIMALS:
            animal.check_food()

        POLE.clear()

        STATISTICS = get_statistics()
        for animal in ANIMALS:
            animal.food = 0

    pprint(STATISTICS)
