import pyrosim.pyrosim as pyrosim
import numpy
import os
import random
import time
import constants as c
class SOLUTION:
  def __init__(self,idChosen):
    random.seed(random.randint(1,1000))
    self.body_num_el = random.randint(1,15)
    self.touch_sensor_no_sensor_new = [0]*self.body_num_el
    self.numSensor_Neurons = 0
    self.orientation_with_respect_to_first = [0]*self.body_num_el
    for i in range(self.body_num_el):
      self.orientation_with_respect_to_first[i] = random.randint(1,5)
      self.touch_sensor_no_sensor_new[i] = random.randint(0,1)
      if self.touch_sensor_no_sensor_new[i] == 1:
        self.numSensor_Neurons = self.numSensor_Neurons + 1
    print("ORIENTATIONS OF MAIN LIMBS WITH RESPECT TO EACH OTHER")
    print(self.orientation_with_respect_to_first)
    self.numMotor_Neurons = self.body_num_el - 1
    self.weights = 2 * numpy.random.rand(self.numSensor_Neurons,self.numMotor_Neurons) - 1
    #print(self.weights)
    self.number_limbs = random.randint(1,10)
    self.number_elements_per_limb = [0]*self.number_limbs
    self.location_on_main_body_limb = [0]*self.number_limbs
    self.orientation_on_main_body_limb = [0]*self.number_limbs
    self.limb_dimensions_x = []
    self.limb_dimensions_y = []
    self.limb_dimensions_z = []
    self.limb_positions_x = []
    self.limb_positions_y = []
    self.limb_positions_z = []
    self.orientation_with_respect_to_first_limbs = []
    self.limb_sensors = []
    self.limb_joint_element_x = []
    self.limb_joint_element_y = []
    self.limb_joint_element_z = []
    self.limb_names = []
    for i in range(self.number_limbs):
      self.number_elements_per_limb[i] = random.randint(2,15) # simple number
      self.location_on_main_body_limb[i] = random.randint(0,self.body_num_el-1) # index
      self.orientation_on_main_body_limb[i] = random.randint(1,5) # simple number
      self.limb_dimensions_x.append( [0]*self.number_elements_per_limb[i] )
      self.limb_dimensions_y.append( [0]*self.number_elements_per_limb[i] )
      self.limb_dimensions_z.append( [0]*self.number_elements_per_limb[i] )
      self.limb_positions_x.append( [0]*self.number_elements_per_limb[i] )
      self.limb_positions_y.append( [0]*self.number_elements_per_limb[i] )
      self.limb_positions_z.append( [0]*self.number_elements_per_limb[i] )
      self.limb_joint_element_x.append( [0]*self.number_elements_per_limb[i] )
      self.limb_joint_element_y.append( [0]*self.number_elements_per_limb[i] )
      self.limb_joint_element_z.append( [0]*self.number_elements_per_limb[i] )
      self.limb_names.append( [0]*self.number_elements_per_limb[i] )
      self.orientation_with_respect_to_first_limbs.append( [0]*self.number_elements_per_limb[i] )
      self.limb_sensors.append( [0]*self.number_elements_per_limb[i] )
      for j in range(self.number_elements_per_limb[i] ):
        self.limb_sensors[i][j] = random.randint(0,1)
    print("Number elements per limb")
    print(self.number_elements_per_limb)
    #self.weights = self.weights * 2 - 1
    self.myID = idChosen
    #print(self.weights)
    #def Evaluate(self,directOrGUI):
  def Start_Simulation(self,directOrGUI):
    self.Create_World()
    self.Create_Body_and_Brain()
    #statement = "python3 simulate.py " + directOrGUI + " " + str(self.myID) + " 2&>1 &"
    statement = "python3 simulate.py " + directOrGUI + " " + str(self.myID) + " &"
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
    pyrosim.End()
  def Create_Body_and_Brain(self):
    pyrosim.Start_URDF("body.urdf")
    number_body_elements = self.body_num_el
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
    touch_sensor_no_sensor = self.touch_sensor_no_sensor_new
    for i in range(number_body_elements):
      body_element_width[i] = round(random.uniform(0.5,1.5),2)
      body_element_length[i] = round(random.uniform(0.5,1.5),2)
      body_element_height[i] = round(random.uniform(0.5,1.5),2)
      #touch_sensor_no_sensor[i] = random.randint(0,1)
      names_body_elements[i] = str(i)
    ii = number_body_elements
    for i in range(self.number_limbs):
      self.location_on_main_body_limb[i] = random.randint(0,number_body_elements-1)
      for j in range(self.number_elements_per_limb[i]):
        self.limb_dimensions_x[i][j] = (round(random.uniform(0.5,1.5),2))
        self.limb_dimensions_y[i][j] = (round(random.uniform(0.5,1.5),2))
        self.limb_dimensions_z[i][j] = (round(random.uniform(0.5,1.5),2))
        self.orientation_with_respect_to_first_limbs[i][j] = (random.randint(1,5))
        self.limb_names[i][j] = str(ii)
        ii = ii + 1
      self.orientation_with_respect_to_first_limbs[i][0] = random.randint(1,5)
      self.limb_joint_element_x[i][0] = 0
      self.limb_joint_element_y[i][0] = 0
      self.limb_joint_element_z[i][0] = 0
      self.limb_positions_x[i][0] = 0
      self.limb_positions_y[i][0] = 0
      self.limb_positions_z[i][0] = 0
    print("LOCATION ON MAIN BODY LIMB")
    print(self.location_on_main_body_limb)
    body_element_x[0] = 0
    body_element_z[0] = 15
    self.orientation_with_respect_to_first[0] = 1
    if number_body_elements != 1:
      joint_element_x[0] = 0 + body_element_width[0]/2
      joint_element_z[0] = 15
    for i in range(number_body_elements-1):
      if number_body_elements == 1:
        continue
      if (i >= (number_body_elements-2)):
        continue
      
      if self.orientation_with_respect_to_first[i+1] == 1:
        joint_element_x[i+1] = body_element_width[i+1]
        body_element_x[i+1] = body_element_width[i+1]/2
      elif self.orientation_with_respect_to_first[i+1] == 2:
        if self.orientation_with_respect_to_first[i] == 2:
          joint_element_y[i+1] = body_element_length[i+1]
          body_element_y[i+1] = body_element_length[i+1]/2
        else:
          joint_element_x[i+1] = body_element_width[i]/2
          joint_element_y[i+1] = body_element_length[i]/2
          #body_element_x[i+1] = body_element_width[i+1]/2
          body_element_y[i+1] = body_element_length[i+1]/2
      elif self.orientation_with_respect_to_first[i+1] == 3:
        if self.orientation_with_respect_to_first[i] == 3:
          joint_element_y[i+1] = -body_element_length[i+1]
          body_element_y[i+1] = -body_element_length[i+1]/2
        else:
          joint_element_x[i+1] = body_element_width[i]/2
          joint_element_y[i+1] = -1*body_element_length[i]/2
          #body_element_x[i+1] = body_element_width[i+1]/2
          body_element_y[i+1] = -1*body_element_length[i+1]/2
      elif self.orientation_with_respect_to_first[i+1] == 4:
        if self.orientation_with_respect_to_first[i] == 4:
          joint_element_z[i+1] = body_element_height[i+1]
          body_element_z[i+1] = body_element_height[i+1]/2
        else:
          joint_element_x[i+1] = body_element_width[i]/2
          joint_element_z[i+1] = body_element_height[i]/2
          #body_element_x[i+1] = body_element_width[i+1]/2
          body_element_z[i+1] = body_element_height[i+1]/2
      elif self.orientation_with_respect_to_first[i+1] == 5:
        if self.orientation_with_respect_to_first[i] == 5:
          joint_element_z[i+1] = -body_element_height[i+1]
          body_element_z[i+1] = -body_element_height[i+1]/2
        else:
          joint_element_x[i+1] = body_element_width[i]/2
          joint_element_z[i+1] = -1*body_element_height[i]/2
          #body_element_x[i+1] = body_element_width[i+1]/2
          body_element_z[i+1] = -1*body_element_height[i+1]/2
    for i in range(self.number_limbs):
      for j in range(self.number_elements_per_limb[i]-1):
        if self.number_elements_per_limb[i] == 1:
          continue
        if (i >= (self.number_elements_per_limb[i]-2)):
          continue
        if self.orientation_with_respect_to_first_limbs[i][j+1] == 1:
          self.limb_joint_element_x[i][j+1] = self.limb_dimensions_x[i][j+1]
          self.limb_positions_x[i][j+1] = self.limb_dimensions_x[i][j+1]/2
        elif self.orientation_with_respect_to_first_limbs[i][j+1] == 2:
          if self.orientation_with_respect_to_first_limbs[i][j] == 2:
            self.limb_joint_element_y[i][j+1] = self.limb_dimensions_y[i][j+1]
            self.limb_positions_y[i][j+1] = self.limb_dimensions_y[i][j+1]/2
          else:
            self.limb_joint_element_x[i][j+1] = self.limb_dimensions_x[i][j]/2
            self.limb_joint_element_y[i][j+1] = self.limb_dimensions_y[i][j]/2
            #body_element_x[i+1] = body_element_width[i+1]/2
            self.limb_positions_y[i][j+1] = self.limb_dimensions_y[i][j+1]/2
        elif self.orientation_with_respect_to_first_limbs[i][j+1] == 3:
          if self.orientation_with_respect_to_first_limbs[i][j] == 3:
            self.limb_joint_element_y[i][j+1] = -self.limb_dimensions_y[i][j+1]
            self.limb_positions_y[i][j+1] = -self.limb_dimensions_y[i][j+1]/2
          else:
            self.limb_joint_element_x[i][j+1] = self.limb_dimensions_x[i][j]/2
            self.limb_joint_element_y[i][j+1] = -1*self.limb_dimensions_y[i][j]/2
            #body_element_x[i+1] = body_element_width[i+1]/2
            self.limb_positions_y[i][j+1] = -1*self.limb_dimensions_y[i][j+1]/2
        elif self.orientation_with_respect_to_first_limbs[i][j+1] == 4:
          if self.orientation_with_respect_to_first_limbs[i][j] == 4:
            self.limb_joint_element_z[i][j+1] = self.limb_dimensions_z[i][j+1]
            self.limb_positions_z[i][j+1] = self.limb_dimensions_z[i][j+1]/2
          else:
            self.limb_joint_element_x[i][j+1] = self.limb_dimensions_x[i][j]/2
            self.limb_joint_element_z[i][j+1] = self.limb_dimensions_z[i][j]/2
            #body_element_x[i+1] = body_element_width[i+1]/2
            self.limb_positions_z[i][j+1] = self.limb_dimensions_z[i][j+1]/2
        elif self.orientation_with_respect_to_first_limbs[i][j+1] == 5:
          if self.orientation_with_respect_to_first_limbs[i][j] == 5:
            self.limb_joint_element_z[i][j+1] = -self.limb_dimensions_z[i][j+1]
            self.limb_positions_z[i][j+1] = -self.limb_dimensions_z[i][j+1]/2
          else:
            self.limb_joint_element_x[i][j+1] = self.limb_dimensions_x[i][j]/2
            self.limb_joint_element_z[i][j+1] = -1*self.limb_dimensions_z[i][j]/2
            #body_element_x[i+1] = body_element_width[i+1]/2
            self.limb_positions_z[i][j+1] = -1*self.limb_dimensions_z[i][j+1]/2
   
    
    
    joint_name_list = []
    for i in range(number_body_elements):
      #print(touch_sensor_no_sensor)
      if touch_sensor_no_sensor[i]:
        pyrosim.Send_Cube(name=names_body_elements[i], pos=[body_element_x[i],body_element_y[i],body_element_z[i]], size=[body_element_width[i],body_element_length[i],body_element_height[i]],COLOR_NAME="Green",RED="0.0",GREEN="1.0",BLUE="0.0")
      else:
        pyrosim.Send_Cube(name=names_body_elements[i], pos=[body_element_x[i],body_element_y[i],body_element_z[i]], size=[body_element_width[i],body_element_length[i],body_element_height[i]],COLOR_NAME="Blue",RED="0.0",GREEN="0.0",BLUE="1.0")
      if (number_body_elements == 1):
        break
      if (i >= (number_body_elements - 1)): # add -1
        break
      name_new = names_body_elements[i] + "_" + names_body_elements[i+1]
      joint_name_list.append(name_new)
      pyrosim.Send_Joint(name = name_new , parent= names_body_elements[i] , child = names_body_elements[i+1] , type = "revolute", position = [joint_element_x[i],joint_element_y[i],joint_element_z[i]], jointAxis = "0 0 1")
    print("NAMES BODY ELEMENTS")
    print(names_body_elements)
    joint_name_limb_list = []
    for i in range(self.number_limbs):
      for j in range(self.number_elements_per_limb[i]):
        if self.limb_sensors[i][j]:
          #pass
          pyrosim.Send_Cube(name=self.limb_names[i][j], pos=[self.limb_positions_x[i][j],self.limb_positions_y[i][j],self.limb_positions_z[i][j]], size=[self.limb_dimensions_x[i][j],self.limb_dimensions_y[i][j],self.limb_dimensions_z[i][j]],COLOR_NAME="Green",RED="0.0",GREEN="1.0",BLUE="0.0")
        else:
          #pass
          pyrosim.Send_Cube(name=self.limb_names[i][j], pos=[self.limb_positions_x[i][j],self.limb_positions_y[i][j],self.limb_positions_z[i][j]], size=[self.limb_dimensions_x[i][j],self.limb_dimensions_y[i][j],self.limb_dimensions_z[i][j]],COLOR_NAME="Blue",RED="0.0",GREEN="0.0",BLUE="1.0")
        if (self.number_elements_per_limb[i] == 1):
          break
        if (j >= (self.number_elements_per_limb[i] - 1)): # add -1
          break
        name_new = self.limb_names[i][j] + "_" + self.limb_names[i][j+1]
        joint_name_limb_list.append(name_new)
        if j == 0:
          print("BRANCHING ON")
          print(self.limb_names[i][j])
          print("CONNECTING TO")
          print(names_body_elements[self.location_on_main_body_limb[i]])
          name_link_torso =  names_body_elements[self.location_on_main_body_limb[i]] + "_" + self.limb_names[i][j+1]
          name_link_torso_2 =  self.limb_names[i][j] + "_" + self.limb_names[i][j+1]
          #name_link_torso_second = names_body_elements[0] + "_" + self.limb_names[i][j]
          #pyrosim.Send_Joint(name = name_link_torso_second , parent=names_body_elements[0] , child = self.limb_names[i][j] , type = "revolute", position = [self.limb_joint_element_x[i][j],self.limb_joint_element_y[i][j],self.limb_joint_element_z[i][j]], jointAxis = "0 0 1")
          pyrosim.Send_Joint(name = name_link_torso , parent= names_body_elements[self.location_on_main_body_limb[i]], child = self.limb_names[i][j] , type = "revolute", position = [self.limb_joint_element_x[i][j],self.limb_joint_element_y[i][j],self.limb_joint_element_z[i][j]], jointAxis = "0 0 1")
          pyrosim.Send_Joint(name = name_link_torso_2 , parent= self.limb_names[i][j], child = self.limb_names[i][j+1] , type = "revolute", position = [self.limb_joint_element_x[i][j],self.limb_joint_element_y[i][j],self.limb_joint_element_z[i][j]], jointAxis = "0 0 1")
          #pyrosim.Send_Joint(name = name_new , parent= names_body_elements[self.location_on_main_body_limb[i]] , child = self.limb_names[i][j] , type = "revolute", position = [self.limb_joint_element_x[i][j],self.limb_joint_element_y[i][j],self.limb_joint_element_z[i][j]], jointAxis = "0 0 1")
        else:
          name_link_torso_second = self.limb_names[i][j] + "_" + self.limb_names[i][j+1]
          pyrosim.Send_Joint(name = name_link_torso_second , parent= self.limb_names[i][j] , child = self.limb_names[i][j+1] , type = "revolute", position = [self.limb_joint_element_x[i][j],self.limb_joint_element_y[i][j],self.limb_joint_element_z[i][j]], jointAxis = "0 0 1")
          
          #pyrosim.Send_Joint(name = name_new , parent= self.limb_names[i][j] , child = self.limb_names[i][j+1] , type = "revolute", position = [self.limb_joint_element_x[i][j],self.limb_joint_element_y[i][j],self.limb_joint_element_z[i][j]], jointAxis = "0 0 1")
    #pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5], size=[1,1,1])
    #pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1,0,1])
    #pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5], size=[1,1,1])
    #pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2,0,1])
    #pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5], size=[1,1,1])
    pyrosim.End()
    self.Create_Brain(joint_name_list,number_body_elements,names_body_elements,body_element_width,body_element_length,body_element_height,touch_sensor_no_sensor)
    
  def Create_Brain(self,joint_name_list,number_body_elements,names_body_elements,body_element_width,body_element_length,body_element_height,touch_sensor_no_sensor):
    brain_file = "brain" + str(self.myID) + ".nndf"
    pyrosim.Start_NeuralNetwork(brain_file)
    sensor_name_index = 0
    for i in range(number_body_elements):
      if touch_sensor_no_sensor[i]:
        pyrosim.Send_Sensor_Neuron(name = sensor_name_index, linkName = names_body_elements[i])
        sensor_name_index = sensor_name_index + 1
    motor_name_index = sensor_name_index
    for element_name in joint_name_list:
      pyrosim.Send_Motor_Neuron( name = motor_name_index , jointName = element_name)
      motor_name_index = motor_name_index + 1
    sensor_neurons = list(range(sensor_name_index))
    motor_neurons = list(range(motor_name_index-sensor_name_index))
    for i in range(len(motor_neurons)):
      motor_neurons[i] = motor_neurons[i] + sensor_name_index
    for currentRow in sensor_neurons:
      for currentColumn in motor_neurons:
        pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn, weight = self.weights[currentRow-1][currentColumn-sensor_name_index-1] )
    pyrosim.End()
    
  def Mutate(self):
    if self.numSensor_Neurons-1 == 0 or self.numSensor_Neurons-1 == -1:
      row_chosen = 0
    else:
      row_chosen = random.randint(0,self.numSensor_Neurons-1)
    if self.numMotor_Neurons-1 == 0 or self.numMotor_Neurons-1 == -1:
      col_chosen = 0
    else:
      col_chosen = random.randint(0,self.numMotor_Neurons-1)
    if self.numMotor_Neurons != 0 and self.numSensor_Neurons !=0:
      self.weights[row_chosen][col_chosen] = random.random() * 2 - 1
      
  def Set_ID(self,valueChosen):
    self.myID = valueChosen
