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
backLegSensorValues = numpy.zeros(10000)
print(backLegSensorValues)
#exit()
for i in range(10000):
  time.sleep(1/60)
  p.stepSimulation()
  print(pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg"))
  #if backLegSensorValues[i] is not None:
  backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
  #print(i)
print(backLegSensorValues)
p.disconnect()
