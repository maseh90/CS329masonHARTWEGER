import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("boxes.sdf")
length = 1
width = 1
height = 1
x = 0
y = 0
z = 1
index = 0
name_new = "Box"
for i in range(5):
  for ii in range(5):
    for iii in range(10):
      name_new = name_new + str(index)
      pyrosim.Send_Cube(name=name_new, pos=[x+i,y+ii,z+iii], size=[length*0.9**iii,width*0.9**iii,height*0.9**iii])
pyrosim.End()
