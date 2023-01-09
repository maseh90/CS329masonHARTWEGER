import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("world.sdf")
length = 1
width = 1
height = 1
x = 0
y = 0
z = 1
index = 0
pyrosim.Send_Cube(name="Box1", pos=[x,y,z], size=[length,width,height])
pyrosim.End()
