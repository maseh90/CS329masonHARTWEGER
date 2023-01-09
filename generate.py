import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("world.sdf")
length = 1
width = 0
height = 0
x = 0
y = 0
z = 1
index = 0
pyrosim.Send_Cube(name="Box1", pos=[x,y,z], size=[length,width,height])
pyrosim.End()
