#!/usr/bin/python3
#Classes for side project with Gabe
#Authors:
#   Ariel Lima <ariel.lima@gordon.edu>
#   ...

#imports needed
from random import randint

###########
##classes##
###########

#global variables for now
chanceOfDodge = 20

#class Player
#class Player:

#class Animal
class Animal:
    """
        This is the main animal class of the mini-game, all other animal classes come from this one
    """
    def __init__(self):#constructor
        #animal level
        self.level = 0
        #agility attributes
        self.speed = 5
        #damage attributes
        self.strength = 5
        #health attributes
        self.health = 500
        self.defense = 5
        self.defenseFactor = 5
        self.equipment = {"helmet" : "",
                          "chest plate": ""} #add or remove based on animal

    def warCry(self):
        #Simple method that returns an animals warcry as string
        return ""
    def getLevel(self):
        #Simple method that returns a animals level
        return(self.level)

    def printAnimalStat(self):
        #print animal stats
        print("level: "         + str(self.level)           + '\n'+
              "speed: "         + str(self.speed)           + '\n'+
              "strength: "      + str(self.strength)        + '\n'+
              "health: "        + str(self.health)          + '\n'+
              "defense: "       + str(self.defense)         + '\n'+
              "defenseFactor : "+ str(self.defenseFactor)   + '\n'+
              "equipment : "    + str(self.equipment)
              )
        
    def attackDamage(self):
        #Simple method that returns the total damage this animal will do
        return(randint(1, self.strength)*randint(1, self.speed))#'*' is times, 3*4=12

    def curHealth(self):
        #Return the current health point of an animal
        return(self.health)    

    def damagePad(self):
        #Simple method that will be run uppon receiving damage, helps negate some of the damage comming in
        return(randint(1, self.defense)+randint(1, self.defenseFactor))#Gabe, randint(x, y) gives us a random number in between those two points

    def takeDamage(self, damage):
        #Simple method that deals damage to self
        damageT = damage - self.damagePad()
        if(damageT > 0):
            self.health -= damage
        else:
            self.health -= 1
    
    def attack(self, attackDamage, defendingAnimal):
        #Input damage being delt at defending animal object
        if(defendingAnimal.doesDodge()==False):
            defendingAnimal.takeDamage(attackDamage)
    
    def doesDodge(self):
        #Returns whether an attack has been succesfully dodged or not
        if(randint(0, chanceOfDodge) <= self.speed):
            return True
        return False

#class Reptile
#Inherits from class Animal
class Reptile(Animal):
    """
    This is the default reptile class, all reptiles inherit from this class
    """
    def __init__(self): #constructor
        #inherit from parent class
        super(Reptile, self).__init__()
        #agility attributes
        self.speed = 2
        #health attributes
        self.defense = 7
        self.defenseFactor = 7

#class Mammal
#Inherits from class Animal
class Mammal(Animal):
    """
    This is the default mammal class, all mammals inherit from this class
    """
    def __init__(self): #constructor
        #inherit from parent class
        super(Mammal, self).__init__()
        #agility attributes
        self.speed = 7
        #damage attributes
        self.strength = 7
        #health attributes
        self.defense = 3
        self.defenseFactor = 4

#class Bird
#Inherits from Animal
class Bird(Animal):
    """
    This is the default bird class, all birds inherit from this class
    """
    def __init__(self): #contstructor
        #inherit from parent class
        super(Bird, self).__init__()
        #agility attributes 
        self.speed = 10
        #damage attribute 
        self.strength = 2
        #health attributes 
        self.health = 400
        self.defense = 3
        self.defenseFactor = 2

#class Fiction
#Inherits from Animal 
class Fiction(Animal):
    """
    This is the default Fiction class, all Fictional animals inherit from this class
    """
    def __init__(self): #constructor
        super(Fiction, self).__init__()
        #This class stays as is
"""
TODO - Gabe:

Create these classes in this file:

class Reptile(Animal): <- the Animal inside the parenthesis means we are inheriting from the Animal class, if you read you know what it means. If you didn't, go read it.
    {...}
class Mammal(Animal):
    {...}
class Bird(Animal):
    {...}
class Fiction(Animal):
    {...}
START THESE BY TONIGHT, use the default one I made to help you.
                        add your name to the authors(replace the '...') when you work on it.

**********************************************************
**MAKE SURE TO ADJUST CLASS VARIABLES FOR EACH SUB-CLASS**
**********************************************************

"""
