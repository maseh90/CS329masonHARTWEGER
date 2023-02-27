import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
from pyrosim.neuron import NEURON
import random
def Create_World():
  pyrosim.Start_SDF("world.sdf")
  pyrosim.Send_Cube(name="Box1", pos=[3,3,3], size=[1,1,1])
  pyrosim.End()
def Create_Robot():
  pyrosim.Start_URDF("body.urdf")
  pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5], size=[1,1,1])
  pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1,0,1])
  pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5], size=[1,1,1])
  pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2,0,1])
  pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5], size=[1,1,1])
  pyrosim.End()
def Generate_Body_and_Brain():
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
  joint_element_x[0] = 0 + body_element_width[0]/2
  joint_element_z[0] = 1.5
  for i in range(number_body_elements-1):
    body_element_x[i+1] = joint_element[0] + body_element_width[i+1]/2
    if number_body_elements == 1:
      break
    if (i == (number_body_elements - 1)):
      break
    joint_element_x[i+1] = body_element_width[i+1]
  pyrosim.Start_URDF("body.urdf")
  joint_name_list = []
  for i in range(number_body_elements-1):
    pyrosim.Send_Cube(name=names_body_elements[i], pos=[body_element_x[i],body_element_y[i],body_element_z[i]], size=[body_element_width[i],body_element_length[i],body_element_height[i]])
    if (i == (number_body_elements - 1)):
      break
    name_new = names_body_elements[i] + "_" + names_body_elements[i+1]
    joint_name_list.append(name_new)
    pyrosim.Send_Joint(name = name_new , parent= names_body_elements[i] , child = names_body_elements[i+1] , type = "revolute", position = [joint_element_x[i],joint_element_y[i],joint_element_z[i]])
  #pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5], size=[1,1,1])
  #pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1,0,1])
  #pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5], size=[1,1,1])
  #pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2,0,1])
  #pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5], size=[1,1,1])
  pyrosim.End()
  Generate_Brain(joint_name_list,number_body_elements,names_body_elements,body_element_width,body_element_length,body_element_height,touch_sensor_no_sensor)
def Generate_Brain(joint_name_list,number_body_elements,names_body_elements,body_element_width,body_element_length,body_element_height,touch_sensor_no_sensor):
  pyrosim.Start_NeuralNetwork("brain.nndf")
  sensor_name_index = 0
  for i in range(number_body_elements):
    if touch_sensor_no_sensor[i]:
      pyrosim.Send_Sensor_Neuron(name = name_index, linkName = names_body_elements[i])
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
  for key_neuron_sensor in sensor_neurons:
    for key_motor_sensor in motor_neurons:
      pyrosim.Send_Synapse( sourceNeuronName = key_neuron_sensor , targetNeuronName = key_motor_sensor , weight = -1+2*random.random() )
  pyrosim.End()
length = 1
width = 1
height = 1
x = 0
y = 0
z = 0.5
index = 0
Create_World()
Generate_Body_and_Brain()
#Generate_Brain()
