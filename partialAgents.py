# partialAgent.py
# parsons/15-oct-2017
#
# Version 1
#
# The starting point for CW1.
#
# Intended to work with the PacMan AI projects from:
#
# http://ai.berkeley.edu/
#
# These use a simple API that allow us to control Pacman's interaction with
# the environment adding a layer on top of the AI Berkeley code.
#
# As required by the licensing agreement for the PacMan AI we have:
#
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

# The agent here is was written by Simon Parsons, based on the code in
# pacmanAgents.py

from pacman import Directions
from game import Agent
import api
import random
import game
import util

def DirectionCalculator(obj_loc, my_loc):
            loc_x = [0] * len(obj_loc) # initalise location lists # i miss numpy
            loc_y = [0] * len(obj_loc)
            obj_direction=[]
            for i in range(len(obj_loc)): # Create vectors from pacman to location
                loc_x[i] = obj_loc[i][0] - my_loc[0] # matlab is love
                loc_y[i] = obj_loc[i][1] - my_loc[1] # matlab is life
                if loc_x[i] < 0:
                    obj_direction.append(Directions.WEST) # Define North south etc.
                if loc_y[i] > 0:
                    obj_direction.append(Directions.NORTH)
                if loc_y[i] < 0:
                    obj_direction.append(Directions.SOUTH)
                if loc_x[i] > 0:
                    obj_direction.append(Directions.EAST)
            obj_direction = list(set(obj_direction))
            return obj_direction

class PartialAgent(Agent):

    # Constructor: this gets run when we first invoke pacman.py
    def __init__(self):
        print "Starting up!"
        name = "Pacman"
        self.last = Directions.STOP
        #ghost_loc_init = api.ghosts(state)

    # This is what gets run in between multiple games
    def final(self, state):
        print "Looks like I just died!"

    # For now I just move randomly
    def getAction(self, state):

        legal = api.legalActions(state)
        fod = api.food(state)
        my_loc = api.whereAmI(state)
        ghost_loc = api.ghosts(state)
        #food_direction = DirectionCalculator(fod, my_loc)
        #ghost_direction = DirectionCalculator(ghost_loc, my_loc)

        # remove stop
        if Directions.STOP in legal: # Get the actions we can try, and remove "STOP" if that is one of them.
            legal.remove(Directions.STOP)
        if ghost_loc:
            ghost_direction = DirectionCalculator(ghost_loc,my_loc) #get ghost locations
            for i in ghost_direction:
                if i in legal:
                    legal.remove(i) #remove ghost direction from legal
            moves = list(legal)
            if len(legal) ==0:
                return Directions.STOP # if no more legal, give up
        else:
            if len(legal) >1:
                if Directions.REVERSE[self.last] in legal: # remove opposite direction
                    legal.remove(Directions.REVERSE[self.last])
            #print 'legal 3: ',legal
            if fod:
                food_direction = DirectionCalculator(fod, my_loc)
                legal = set(legal)
                food_direction = set(food_direction)
                moves = list(food_direction)
            else:
                moves = list(legal)
        pick = random.choice(moves)
        self.last = pick # remember what direction we are now moving towards'''
        return pick
