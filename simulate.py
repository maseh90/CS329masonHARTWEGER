import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(100)
#print(backLegSensorValues)
#exit()
for i in range(100):
  time.sleep(1/60)
  p.stepSimulation()
  #print(pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg"))
  if pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg") is not None:
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
p.disconnect()
print(backLegSensorValues)
