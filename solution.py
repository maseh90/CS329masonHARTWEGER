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
    self.Create_Body()
    self.Create_Brain()
    statement = "python3 simulate.py " + directOrGUI + " " + str(self.myID) + " 2&>1 &"
    os.system(statement)
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
    pyrosim.Send_Cube(name="FirstStep", pos=[-52,2,0], size=[10,10,1])
    pyrosim.End()
  def Create_Body(self):
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[0,0,1], size=[1,1,1])
    pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0,-0.5,1], jointAxis = "1 0 0")
    pyrosim.Send_Cube(name="BackLeg", pos=[0,-0.5,0], size=[0.2,1,0.2])
    pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0,0.5,1], jointAxis = "1 0 0")
    pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,0], size=[0.2,1,0.2])
    pyrosim.Send_Joint(name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = [-0.5,0,1], jointAxis = "0 1 0")
    pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5,0,0], size=[1,0.2,0.2])
    pyrosim.Send_Joint(name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = [0.5,0,1], jointAxis = "0 1 0")
    pyrosim.Send_Cube(name="RightLeg", pos=[0.5,0,0], size=[1.0,0.2,0.2])
    pyrosim.Send_Joint(name = "FrontLeg_FrontLowerLeg" , parent= "FrontLeg" , child = "FrontLowerLeg" , type = "revolute", position = [0.0,1.0,0.0], jointAxis = "1 0 0")
    pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0,0,-0.5], size=[0.2,0.2,1.0])
    pyrosim.Send_Joint(name = "BackLeg_BackLowerLeg" , parent= "BackLeg" , child = "BackLowerLeg" , type = "revolute", position = [0.0,-1.0,0.0], jointAxis = "1 0 0")
    pyrosim.Send_Cube(name="BackLowerLeg", pos=[0,0,-0.5], size=[0.2,0.2,1.0])
    pyrosim.Send_Joint(name = "LeftLeg_LeftLowerLeg" , parent= "LeftLeg" , child = "LeftLowerLeg" , type = "revolute", position = [-1.0,0.0,0.0], jointAxis = "0 1 0")
    pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0,0,-0.5], size=[0.2,0.2,1.0])
    pyrosim.Send_Joint(name = "RightLeg_RightLowerLeg" , parent= "RightLeg" , child = "RightLowerLeg" , type = "revolute", position = [1.0,0.0,0.0], jointAxis = "0 1 0")
    pyrosim.Send_Cube(name="RightLowerLeg", pos=[0,0,-0.5], size=[0.2,0.2,1.0])
    # New 45 degree legs
    pyrosim.Send_Joint(name = "Torso_MiddleBackLeg" , parent= "Torso" , child = "MiddleBackLeg" , type = "revolute", position = [0,-0.5,1], jointAxis = "1 0 0")
    pyrosim.Send_Cube(name="MiddleBackLeg", pos=[-0.5,-0.5,0], size=[0.2,1,0.2])
    pyrosim.Send_Joint(name = "Torso_MiddleFrontLeg" , parent= "Torso" , child = "MiddleFrontLeg" , type = "revolute", position = [0,0.5,1], jointAxis = "1 0 0")
    pyrosim.Send_Cube(name="MiddleFrontLeg", pos=[0.5,0.5,0], size=[0.2,1,0.2])
    pyrosim.Send_Joint(name = "Torso_MiddleLeftLeg" , parent= "Torso" , child = "MiddleLeftLeg" , type = "revolute", position = [-0.5,0,1], jointAxis = "0 1 0")
    pyrosim.Send_Cube(name="MiddleLeftLeg", pos=[-0.5,-0.5,0], size=[1,0.2,0.2])
    pyrosim.Send_Joint(name = "Torso_MiddleRightLeg" , parent= "Torso" , child = "MiddleRightLeg" , type = "revolute", position = [0.5,0,1], jointAxis = "0 1 0")
    pyrosim.Send_Cube(name="MiddleRightLeg", pos=[0.5,0.5,0], size=[1.0,0.2,0.2])
    
    pyrosim.Send_Joint(name = "MiddleFrontLeg_MiddleFrontLowerLeg" , parent= "MiddleFrontLeg" , child = "MiddleFrontLowerLeg" , type = "revolute", position = [0.0,1.0,0.0], jointAxis = "1 0 0")
    pyrosim.Send_Cube(name="MiddleFrontLowerLeg", pos=[0.5,0,-0.5], size=[0.2,0.2,1.0])
    pyrosim.Send_Joint(name = "MiddleBackLeg_MiddleBackLowerLeg" , parent= "MiddleBackLeg" , child = "MiddleBackLowerLeg" , type = "revolute", position = [0.0,-1.0,0.0], jointAxis = "1 0 0")
    pyrosim.Send_Cube(name="MiddleBackLowerLeg", pos=[-0.5,0,-0.5], size=[0.2,0.2,1.0])
    pyrosim.Send_Joint(name = "MiddleLeftLeg_MiddleLeftLowerLeg" , parent= "MiddleLeftLeg" , child = "MiddleLeftLowerLeg" , type = "revolute", position = [-1.0,0.0,0.0], jointAxis = "0 1 0")
    pyrosim.Send_Cube(name="MiddleLeftLowerLeg", pos=[0,-0.5,-0.5], size=[0.2,0.2,1.0])
    pyrosim.Send_Joint(name = "MiddleRightLeg_MiddleRightLowerLeg" , parent= "MiddleRightLeg" , child = "MiddleRightLowerLeg" , type = "revolute", position = [1.0,0.0,0.0], jointAxis = "0 1 0")
    pyrosim.Send_Cube(name="MiddleRightLowerLeg", pos=[0,0.5,-0.5], size=[0.2,0.2,1.0])
    pyrosim.End()
    #exit()
  def Create_Brain(self):
    brain_file = "brain" + str(self.myID) + ".nndf"
    pyrosim.Start_NeuralNetwork(brain_file)
    pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "FrontLowerLeg")
    pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLowerLeg")
    pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "LeftLowerLeg")
    pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "RightLowerLeg")
    pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_BackLeg")
    pyrosim.Send_Motor_Neuron( name = 5 , jointName = "Torso_FrontLeg")
    pyrosim.Send_Motor_Neuron( name = 6 , jointName = "Torso_LeftLeg")
    pyrosim.Send_Motor_Neuron( name = 7 , jointName = "Torso_RightLeg")
    pyrosim.Send_Motor_Neuron( name = 8 , jointName = "FrontLeg_FrontLowerLeg")
    pyrosim.Send_Motor_Neuron( name = 9 , jointName = "BackLeg_BackLowerLeg")
    pyrosim.Send_Motor_Neuron( name = 10 , jointName = "LeftLeg_LeftLowerLeg")
    pyrosim.Send_Motor_Neuron( name = 11 , jointName = "RightLeg_RightLowerLeg")
    #pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 3 , weight = -0.75 )
    #pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = -0.75 )
    #pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 4 , weight = 1 )
    #pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 4 , weight = 1 )
    sensor_neurons = list(range(c.numSensorNeurons))
    motor_neurons = list(range(c.numMotorNeurons))
    #for neuronName in self.nn.Get_Neuron_Names():
    for currentRow in sensor_neurons:
      for currentColumn in motor_neurons:
        pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn + c.numSensorNeurons , weight = self.weights[currentRow][currentColumn] )
    pyrosim.End()
    #exit()
  def Mutate(self):
    row_chosen = random.randint(0,c.numSensorNeurons-1)
    col_chosen = random.randint(0,c.numMotorNeurons-1)
    self.weights[row_chosen][col_chosen] = random.random() * 2 - 1
  def Set_ID(self,valueChosen):
    self.myID = valueChosen
