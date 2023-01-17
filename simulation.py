class SIMULATION:
  def __init__(self):
    simulation = SIMULATION()
    self.world = WORLD()
    self.robot = ROBOT()
    self.physicsClient = p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.setGravity(0,0,-9.8)
