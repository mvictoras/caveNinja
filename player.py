from item import *
from common import *

global bananas

class Player:

  items = []

  def __init__(self, nmbItems, objHeight, objStartingRadius, totalItems, timestep, name, score):
    self.nmbItems = nmbItems
    self.objStartingRadius = objStartingRadius
    self.objHeight = objHeight
    self.name = name
    self.totalItems = totalItems
    self.timestep = timestep
    self.dt = 0
    self.items = []
    self.score = 0

    #for item in xrange(nmbItems):
    #  newItem = Item(" ", 0.5, objHeight, objStartingRadius, name)
    #  self.items.append( newItem )
    #  gameItems.append( newItem )

    #bananas = gameItems[0].halves



  #def update(self, t, dt):
    #self.dt += dt
    #if (self.dt > self.timestep) and (len(self.items) < self.totalItems) :
    #  for item in xrange(self.nmbItems):
    #    newItem = Item(getSceneManager(), " ", 0.5, self.objHeight, self.objStartingRadius, self.name)
    #    self.items.append( newItem )
    #    gameItems.append( newItem )

    #  self.dt = 0

  def setWandId(self, wandId):
      self.wandId = wandId





