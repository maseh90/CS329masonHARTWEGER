import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("boxes.sdf")
length = 1
width = 1
height = 1
x = 0
y = 0
z = 0
index = 0
pyrosim.Send_Cube(name="Box1", pos=[x+i,y+ii,z+iii], size=[length*0.9**iii,width*0.9**iii,height*0.9**iii])
pyrosim.End()
