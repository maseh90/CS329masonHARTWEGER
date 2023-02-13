import pyrosim.pyrosim as pyrosim
import numpy
import os
import random
import time
import constants as c
class SOLUTION:
  def __init__(self,idChosen):
    self.weights = 2 * numpy.random.rand(c.numSensorNeurons,c.numMotorNeurons) - 1
    #print(self.weights)
    self.weights = self.weights * 2 - 1
    self.myID = idChosen
    #print(self.weights)
    #def Evaluate(self,directOrGUI):
  def Start_Simulation(self,directOrGUI):
    self.Create_World()
    self.Create_Body_and_Brain()
    statement = "python3 simulate.py " + directOrGUI + " " + str(self.myID) + " 2&>1 &"
    #statement = "python3 simulate.py " + directOrGUI + " " + str(self.myID) + " &"
    os.system(statement)
    #pyrosim.End()
  def Wait_For_Simulation_To_End(self):
    open_file = "fitness" + str(self.myID) + ".txt"
    while not os.path.exists(open_file):
      time.sleep(0.01)
    f = open(open_file, "r")
    self.fitness = float(f.read())
    f.close()
    command_remove = "rm " + open_file
    os.system(command_remove)
    #print(self.fitness)
  def Create_World(self):
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box1", pos=[3,3,3], size=[1,1,1])
    pyrosim.Send_Cube(name="FirstStep", pos=[-52.5,2,0.125], size=[100,100,0.25],mass=1000.0)
    pyrosim.Send_Cube(name="SecondStep", pos=[-53.5,2,0.375], size=[100,100,0.25],mass=1000.0)
    pyrosim.Send_Cube(name="ThirdStep", pos=[-54.5,2,0.625], size=[100,100,0.25],mass=1000.0)
    pyrosim.Send_Cube(name="FourthStep", pos=[-55.5,2,0.875], size=[100,100,0.25],mass=1000.0)
    pyrosim.Send_Cube(name="FifthStep", pos=[-56.5,2,1.125], size=[100,100,0.25],mass=1000.0)
    pyrosim.Send_Cube(name="SixthStep", pos=[-57.5,2,1.375], size=[100,100,0.25],mass=1000.0)
    pyrosim.Send_Cube(name="SeventhStep", pos=[-58.5,2,1.625], size=[100,100,0.25],mass=1000.0)
    pyrosim.Send_Cube(name="EighthStep", pos=[-59.5,2,1.875], size=[100,100,0.25],mass=1000.0)
    pyrosim.Send_Cube(name="NinthStep", pos=[-60.5,2,2.125], size=[100,100,0.25],mass=1000.0)
    pyrosim.Send_Cube(name="TenthStep", pos=[-61.5,2,2.375], size=[100,100,0.25],mass=1000.0)
    pyrosim.Send_Cube(name="EleventhStep", pos=[-62.5,2,2.625], size=[100,100,0.25],mass=1000.0)
    pyrosim.End()
  def Create_Body_and_Brain(self):
    number_body_elements = random.randint(1,10)
    names_body_elements = ["0"]*number_body_elements
    body_element_width = [0]*number_body_elements
    body_element_length = [0]*number_body_elements
    body_element_height = [0]*number_body_elements
    body_element_x = [0]*number_body_elements # this will change, build in +x directiomn
    body_element_y = [0]*number_body_elements
    body_element_z = [0]*number_body_elements
    joint_element_x = [0]*(number_body_elements-1) # this will change, build in +x directiomn
    joint_element_y = [0]*(number_body_elements-1)
    joint_element_z = [0]*(number_body_elements-1)
    touch_sensor_no_sensor = [0]*number_body_elements
    for i in range(number_body_elements):
      body_element_width[i] = round(random.uniform(0,3),2)
      body_element_length[i] = round(random.uniform(0,3),2)
      body_element_height[i] = round(random.uniform(0,3),2)
      touch_sensor_no_sensor[i] = random.randint(0,1)
      names_body_elements[i] = str(i)
    body_element_x[0] = 0
    body_element_z[0] = 1.5
    if number_body_elements != 1:
      joint_element_x[0] = 0 + body_element_width[0]/2
      joint_element_z[0] = 1.5
    for i in range(number_body_elements-1):
      body_element_x[i+1] = joint_element_x[0] + body_element_width[i+1]/2
      if number_body_elements == 1:
        continue
      if (i >= (number_body_elements-2)):
        continue
      joint_element_x[i+1] = body_element_width[i+1]
    pyrosim.Start_URDF("body.urdf")
    joint_name_list = []
    for i in range(number_body_elements-1):
      pyrosim.Send_Cube(name=names_body_elements[i], pos=[body_element_x[i],body_element_y[i],body_element_z[i]], size=[body_element_width[i],body_element_length[i],body_element_height[i]])
      if (i == (number_body_elements - 1)):
        break
      name_new = names_body_elements[i] + "_" + names_body_elements[i+1]
      joint_name_list.append(name_new)
      pyrosim.Send_Joint(name = name_new , parent= names_body_elements[i] , child = names_body_elements[i+1] , type = "revolute", position = [joint_element_x[i],joint_element_y[i],joint_element_z[i]], jointAxis = "1 0 0")
    #pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5], size=[1,1,1])
    #pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1,0,1])
    #pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5], size=[1,1,1])
    #pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2,0,1])
    #pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5], size=[1,1,1])
    pyrosim.End()
    self.Create_Brain(joint_name_list,number_body_elements,names_body_elements,body_element_width,body_element_length,body_element_height,touch_sensor_no_sensor)
  def Create_Brain(self,joint_name_list,number_body_elements,names_body_elements,body_element_width,body_element_length,body_element_height,touch_sensor_no_sensor):
    brain_file = "brain" + str(self.myID) + ".nndf"
    pyrosim.Start_NeuralNetwork("brain.nndf")
    sensor_name_index = 0
    for i in range(number_body_elements):
      if touch_sensor_no_sensor[i]:
        pyrosim.Send_Sensor_Neuron(name = sensor_name_index, linkName = names_body_elements[i])
        sensor_name_index = sensor_name_index + 1
    motor_name_index = sensor_name_index
    for element_name in joint_name_list:
      pyrosim.Send_Motor_Neuron( name = motor_name_index , jointName = element_name)
      motor_name_index = motor_name_index + 1
    #pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
    #pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
    #pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
    #pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
    #pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")
    #pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 3 , weight = -0.75 )
    #pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = -0.75 )
    #pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 4 , weight = 1 )
    #pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 4 , weight = 1 )
    sensor_neurons = list(range(sensor_name_index-1))
    motor_neurons = list(range(motor_name_index-sensor_name_index))
    for i in range(len(motor_neurons)):
      motor_neurons[i] = motor_neurons[i] + sensor_name_index
    #for neuronName in self.nn.Get_Neuron_Names():
    for currentRow in sensor_neurons:
      for currentColumn in motor_neurons:
        pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn, weight = self.weights[currentRow][currentColumn-sensor_name_index] )
    pyrosim.End()
    #exit()
  def Mutate(self):
    row_chosen = random.randint(0,c.numSensorNeurons-1)
    col_chosen = random.randint(0,c.numMotorNeurons-1)
    self.weights[row_chosen][col_chosen] = random.random() * 2 - 1
  def Set_ID(self,valueChosen):
    self.myID = valueChosen
