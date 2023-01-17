import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import constants as c
import numpy
import random
import math
class SIMULATION:
  def __init__(self):
    self.world = WORLD()
    self.robot = ROBOT()
    self.physicsClient = p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.setGravity(0,0,-9.8)
