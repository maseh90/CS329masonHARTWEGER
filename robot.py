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
from pyrosim.neuralNetwork import NEURAL_NETWORK
class ROBOT:
  def __init__(self):
    self.robotId = p.loadURDF("body.urdf")
    pyrosim.Prepare_To_Simulate(self.robotId)
    self.nn = NEURAL_NETWORK("brain.nndf")
    self.Prepare_To_Sense()
    self.Prepare_To_Act()
  def Prepare_To_Sense(self):
    self.sensors = {}
    for linkName in pyrosim.linkNamesToIndices:
      self.sensors[linkName] = SENSOR(linkName,numpy.zeros(c.simulationSteps))
      #print(self.sensors[linkName].values)
  def Sense(self,t):
    for linkName in pyrosim.linkNamesToIndices:
      self.sensors[linkName].values[t] = self.sensors[linkName].Get_Value()
      #print(self.sensors[linkName].values)
  def Prepare_To_Act(self):
    self.motors = {}
    for jointName in pyrosim.jointNamesToIndices:
      self.motors[jointName] = MOTOR(jointName)
  def Act(self,t):
    for jointName in pyrosim.jointNamesToIndices:
      self.motors[jointName].Set_Value(self.robotId,t)
  def Save_Values(self):
    numpy.save("data/targetAngles1.npy",self.motors["Torso_BackLeg"].motorValues)
    numpy.save("data/targetAngles2.npy",self.motors["Torso_FrontLeg"].motorValues)
    numpy.save("data/sensorData1.npy",self.sensors["BackLeg"].values)
    numpy.save("data/sensorData2.npy",self.sensors["FrontLeg"].values)
  def Think(self):
    self.nn.Print()
                                                 
    
