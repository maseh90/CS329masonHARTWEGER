import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy
import random
import math
import constants as c
import sys
from simulation import SIMULATION

simulation = SIMULATION("DIRECT")
simulation.Run()
simulation.Get_Fitness()

#physicsClient = p.connect(p.GUI)
#p.setAdditionalSearchPath(pybullet_data.getDataPath())
#p.setGravity(0,0,-9.8)
#planeId = p.loadURDF("plane.urdf")
#robotId = p.loadURDF("body.urdf")
#p.loadSDF("world.sdf")
#pyrosim.Prepare_To_Simulate(robotId)
#backLegSensorValues = numpy.zeros(1000)
#frontLegSensorValues = numpy.zeros(1000)
#targetAnglesFront = numpy.pi/4*numpy.sin(numpy.linspace(0, 2*numpy.pi, 1000))
#targetAnglesBack = numpy.pi/4*numpy.sin(numpy.linspace(0, 2*numpy.pi, 1000))
#for i in range(1000):
#  targetAnglesFront[i] = c.amplitudeFront * math.sin(c.frequencyFront * i + c.phaseOffsetFront)
#  targetAnglesBack[i] = c.amplitudeBack * math.sin(c.frequencyBack * i + c.phaseOffsetBack)
#  time.sleep(1/60)
#  p.stepSimulation()
#  if pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg") is not None:
#    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#  if pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg") is not None:
#    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
#  pyrosim.Set_Motor_For_Joint(
#  bodyIndex = robotId,
#  jointName = "Torso_BackLeg",
#  controlMode = p.POSITION_CONTROL,
#  targetPosition = targetAnglesBack[i], # random.random()-0.5)*math.pi/4.0,
#  maxForce = 150)
#  pyrosim.Set_Motor_For_Joint(
#  bodyIndex = robotId,
#  jointName = "Torso_FrontLeg",
#  controlMode = p.POSITION_CONTROL,
#  targetPosition = targetAnglesFront[i], # random.random()-0.5)*math.pi/4.0,
#  maxForce = 150)
#numpy.save("data/targetAngles.npy",targetAngles)
#numpy.save("data/backLegSensorValues.npy",backLegSensorValues)
#numpy.save("data/frontLegSensorValues.npy",frontLegSensorValues)
#p.disconnect()
