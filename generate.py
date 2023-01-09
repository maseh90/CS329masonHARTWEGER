import pyrosim.pyrosim as pyrosim
def Create_World():
  pyrosim.Start_SDF("world.sdf")
  pyrosim.Send_Cube(name="Box1", pos=[0,0,0.5], size=[1,1,1])
  pyrosim.End()
length = 1
width = 1
height = 1
x = 0
y = 0
z = 0.5
index = 0
Create_World()

