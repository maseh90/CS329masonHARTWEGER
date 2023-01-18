import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import constants as c
import numpy
import random
import math
from sensor import SENSOR
from motor import MOTOR
class ROBOT:
  def __init__(self):
    self.robotId = p.loadURDF("body.urdf")
    pyrosim.Prepare_To_Simulate(self.robotId)
    self.Prepare_To_Sense()
    self.Prepare_To_Act()
  def Prepare_To_Sense(self):
    self.sensors = {}
    for linkName in pyrosim.linkNamesToIndices:
      self.sensors[linkName] = SENSOR(linkName,numpy.zeros(c.simulationSteps))
      print(self.sensors[linkName].values)
  def Sense(self,t):
    for linkName in pyrosim.linkNamesToIndices:
      self.sensors[linkName].values[t] = self.sensors[linkName].Get_Value()
      print(self.sensors[linkName].values)
  def Prepare_To_Act(self):
    self.motors = {}
    for jointName in pyrosim.jointNamesToIndices:
      self.motors[jointName] = MOTOR(jointName)
  def Act(self,t):
    for jointName in pyrosim.jointNamesToIndices:
      self.motors[jointName].Set_Value(self.robotId,t)
