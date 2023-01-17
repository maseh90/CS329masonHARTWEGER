class WORLD:
  def __init__(self):
    world = WORLD()
  def Prepare_To_Simulate(self):
    physicsClient = p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.setGravity(0,0,-9.8)
    planeId = p.loadURDF("plane.urdf")
    p.loadSDF("world.sdf")
