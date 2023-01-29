import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import constants as c
import numpy
import random
import math
from world import WORLD
from robot import ROBOT
class SIMULATION:
  def __init__(self):
    self.physicsClient = p.connect(p.DIRECT)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.setGravity(0,0,c.gravity)
    self.world = WORLD()
    self.robot = ROBOT()
  def Run(self):
    for i in range(c.simulationSteps):
      time.sleep(c.sleepTime)
      self.robot.Sense(i)
      self.robot.Think()
      self.robot.Act(i)
      p.stepSimulation()
    self.robot.Save_Values()
  def __del__(self):
    p.disconnect()
  def Get_Fitness(self):
    self.robot.Get_Fitness()
