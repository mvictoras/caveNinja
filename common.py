from omega import *
from cyclops import *
from omegaToolkit import *
from euclid import *
from math import *
import random

itemModel = {}
players = ['Andrew', 'Joshua', 'Antwan']
#players = ['Andrew']
items = {}
gameItems = []
'''
items['Andrew'] = ['Chair', 'Table', 'Sword']
items['Joshua'] = ['banana']
items['Antwan'] = ['SpaceShip', 'Sword']
'''

items['Andrew'] = ['banana']
items['Joshua'] = ['banana']
items['Antwan'] = ['banana']

def getRandomPosition(y, radius):
  x = random.randint(0, radius) * (random.randint(0, 1) * 2 -  1)
  z = sqrt(pow(radius,2) - pow(x,2)) * (random.randint(0, 1) * 2 - 1)
  return Vector3(x, y, z)

def loadModel(player, name):
  '''  
  key = (player, name)
  itemModel[key] = ModelInfo()
  itemModel[key].name = name
  itemModel[key].path = "models/" + player + "/" + name + ".fbx"
  itemModel[key].size = 1.0
  getSceneManager().loadModel(itemModel[key])
  '''
  for i in range(0,2):
      key = (player, str(i))
      itemModel[key] = ModelInfo()
      itemModel[key].name = str('banana_half%i'%(i + 1))
      #itemModel[key].path = "models/" + player + "/" + 'banana'+ '/' + 'banana_half'+ str(i) + ".fbx"
      itemModel[key].path = "models/" + player + "/" + 'banana'+ '/' + 'banana_half'+ str(i + 1) + ".obj"
      itemModel[key].size = 1.0
      getSceneManager().loadModel(itemModel[key])

def loadModels():
  for player in players:
    for item in items[player]:
      loadModel(player, item)

def createRandomItem(playerName, height, radius):
  index = random.randint(0, len(items[playerName]) - 1)
  halves = []
  
  '''
  item = StaticObject.create(items[playerName][index])
  item.setPosition( getRandomPosition( height, radius ))
  item.setEffect("textured")
  '''
    
  randPos = getRandomPosition( height, radius )
    
  for i in range(0,2):
    tempName = str('banana_half%i'%(i + 1))
    print 'TEMPNAME     ',tempName
    item = StaticObject.create(tempName)
    item.setPosition(randPos)
    item.setEffect("textured")
  #test hit zone:
    #item.setBoundingBoxVisible(True)
    
    halves.append(item)
  #print item.getPosition()

  return halves