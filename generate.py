import pyrosim.pyrosim as pyrosim
def Create_World():
  pyrosim.Start_SDF("world.sdf")
  pyrosim.Send_Cube(name="Box1", pos=[3,3,3], size=[1,1,1])
  pyrosim.End()
def Create_Robot():
  pyrosim.Start_URDF("body.urdf")
  pyrosim.Send_Cube(name="Link0", pos=[0,0,0.5], size=[1,1,1])
  pyrosim.Send_Joint(name = "Link0_Link1" , parent= "Link0" , child = "Link1" , type = "revolute", position = [0,0,1])
  pyrosim.Send_Cube(name="Link1", pos=[0,0,0.5], size=[1,1,1])
  pyrosim.End()
length = 1
width = 1
height = 1
x = 0
y = 0
z = 0.5
index = 0
Create_World()
Create_Robot()
