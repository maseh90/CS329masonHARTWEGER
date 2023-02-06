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
import os
from pyrosim.neuralNetwork import NEURAL_NETWORK
class ROBOT:
  def __init__(self,solutionID):
    self.robotId = p.loadURDF("body.urdf")
    pyrosim.Prepare_To_Simulate(self.robotId)

    self.Prepare_To_Sense()
    self.Prepare_To_Act()
    self.solutionID = solutionID
    brain_name = "brain" + str(solutionID) + ".nndf"
    self.nn = NEURAL_NETWORK(brain_name)
    #for file in os.listdir("."):
    #  if file.startswith("brain"):
    #    os.system("rm{0} ".format(file))
    os.system("rm "+brain_name)
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
    for neuronName in self.nn.Get_Neuron_Names():
      if self.nn.Is_Motor_Neuron(neuronName):
        jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
        desiredAngle = c.motorJointRange*self.nn.Get_Value_Of(neuronName)
        self.motors[jointName].Set_Value(self.robotId,desiredAngle)
  def Save_Values(self):
    #numpy.save("data/targetAngles1.npy",self.motors["Torso_BackLeg"].motorValues)
    #numpy.save("data/targetAngles2.npy",self.motors["Torso_FrontLeg"].motorValues)
    numpy.save("data/sensorData1.npy",self.sensors["BackLeg"].values)
    numpy.save("data/sensorData2.npy",self.sensors["FrontLeg"].values)
  def Think(self):
    self.nn.Update()
    #self.nn.Print()
  def Get_Fitness(self):
    stateOfLinkZero = p.getLinkState(self.robotId,0)
    positionOfLinkZero = stateOfLinkZero[0]
    xCoordinateOfLinkZero = positionOfLinkZero[0]
    #basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
    #basePosition = basePositionAndOrientation[0]
    #xPosition = basePosition[0]
    open_file = "tmp" + str(self.solutionID) + ".txt"
    f = open(open_file, "w")
    f.write(str(xCoordinateOfLinkZero))
    f.close()
    command_move = "mv " + "tmp" + str(self.solutionID) + ".txt " + "fitness" + str(self.solutionID) + ".txt"
    os.system(command_move)
    #print(positionOfLinkZero)
                                                 
    
