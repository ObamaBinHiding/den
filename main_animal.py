#!/usr/bin/python3
#Classes for side project with Gabe
#Authors:
#   Ariel Lima <ariel.lima@gordon.edu>
#   ...

#imports needed
from random import randint

#classes
class Animal:
    """
        This is the main animal class of the mini-game, all other animal classes come from this one
    """
    def __init__(self):
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

    def printAnimalStat(self):
        #print animal stats
        print("speed: "         + str(self.speed)           + '\n'+
              "attack: "        + str(self.attack)          + '\n'+
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
        defendingAnimal.takeDamage(attackDamage)
    

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
