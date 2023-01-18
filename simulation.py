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
    self.physicsClient = p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.setGravity(0,0,c.gravity)
    self.world = WORLD()
    self.robot = ROBOT()
  def Run(self):
    for i in range(c.simulationSteps):
      time.sleep(c.sleepTime)
      self.robot.Sense(i)
      self.robot.Act(i)
      p.stepSimulation()
      """
      targetAnglesFront[i] = c.amplitudeFront * math.sin(c.frequencyFront * i + c.phaseOffsetFront)
      targetAnglesBack[i] = c.amplitudeBack * math.sin(c.frequencyBack * i + c.phaseOffsetBack)
      if pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg") is not None:
        backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
      if pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg") is not None:
        frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
      pyrosim.Set_Motor_For_Joint(
      bodyIndex = robotId,
      jointName = "Torso_BackLeg",
      controlMode = p.POSITION_CONTROL,
      targetPosition = targetAnglesBack[i], # random.random()-0.5)*math.pi/4.0,
      maxForce = 150)
      pyrosim.Set_Motor_For_Joint(
      bodyIndex = robotId,
      jointName = "Torso_FrontLeg",
      controlMode = p.POSITION_CONTROL,
      targetPosition = targetAnglesFront[i], # random.random()-0.5)*math.pi/4.0,
      maxForce = 150)
      """
      #print(i)
  def __del__(self):
    p.disconnect()
