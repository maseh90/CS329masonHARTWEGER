import pybullet as p
import pybullet_data
import time
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
for i in range(999):
  time.sleep(1/60)
  p.stepSimulation()
  backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
  print(i)
p.disconnect()
