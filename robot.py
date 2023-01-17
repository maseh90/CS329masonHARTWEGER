import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import constants as c
import numpy
import random
import math
from sensor import SENSOR
class ROBOT:
  def __init__(self,timeSteps):
    self.motors = {}
    self.robotId = p.loadURDF("body.urdf")
    self.numberTimeSteps = timeSteps
    pyrosim.Prepare_To_Simulate(self.robotId)
    self.Prepare_To_Sense()
  def Prepare_To_Sense(self):
    self.sensors = {}
    for linkName in pyrosim.linkNamesToIndices:
      self.sensors[linkName] = SENSOR(linkName,numpy.zeros(self.numberTimeSteps))
      print(self.sensors[linkName].values)
  def Sense(self,t):
    for linkName in pyrosim.linkNamesToIndices:
      self.sensors[linkName].values[t] = self.sensors[linkName].Get_Value()
      print(self.sensors[linkName].values)
  def Prepare_To_Act(self):
    pass
