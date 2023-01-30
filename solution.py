import pyrosim.pyrosim as pyrosim
import numpy
import os
import random
import time
import constants as c
class SOLUTION:
  def __init__(self,idChosen):
    self.weights = numpy.random.rand(3,2)
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
    pyrosim.End()
  def Create_Body(self):
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[0,0,1], size=[1,1,1])
    pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0,-0.5,1], jointAxis = "0 1 0")
    pyrosim.Send_Cube(name="BackLeg", pos=[0,-0.5,0], size=[0.2,1,0.2])
    pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0,0.5,1], jointAxis = "0 1 0")
    pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,0], size=[0.2,1,0.2])
    pyrosim.End()
    #exit()
  def Create_Brain(self):
    brain_file = "brain" + str(self.myID) + ".nndf"
    pyrosim.Start_NeuralNetwork(brain_file)
    pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
    pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
    pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
    pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
    pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")
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
