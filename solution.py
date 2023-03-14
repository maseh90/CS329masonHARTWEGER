import pyrosim.pyrosim as pyrosim
import numpy
import os
import random
import time
import constants as c
class SOLUTION:
  def __init__(self,idChosen):
    self.fitness = 0
    self.fitness_call_number = 0
    random.seed(random.randint(1,1000))
    self.body_num_el = random.randint(1,10)
    self.touch_sensor_no_sensor_new = [0]*self.body_num_el
    self.numSensor_Neurons = 0
    self.orientation_with_respect_to_first = [0]*self.body_num_el
    for i in range(self.body_num_el):
      self.orientation_with_respect_to_first[i] = random.randint(2,5)
      self.touch_sensor_no_sensor_new[i] = random.randint(0,1)
      if self.touch_sensor_no_sensor_new[i] == 1:
        self.numSensor_Neurons = self.numSensor_Neurons + 1
    #print("ORIENTATIONS OF MAIN LIMBS WITH RESPECT TO EACH OTHER")
    #print(self.orientation_with_respect_to_first)
    self.numMotor_Neurons = self.body_num_el - 1
    self.weights = 2 * numpy.random.rand(self.numSensor_Neurons,self.numMotor_Neurons) - 1
    self.simulation_start = False
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
    self.joint_name_limb_list = []
    self.limb_weights = []
    self.numSensorNeurons = [0]*self.number_limbs
    self.numMotorNeurons = [0]*self.number_limbs
    for i in range(self.number_limbs):
      self.number_elements_per_limb[i] = random.randint(2,10) # simple number
      self.location_on_main_body_limb[i] = random.randint(0,self.body_num_el-1) # index
      self.orientation_on_main_body_limb[i] = random.randint(2,5) # simple number
      self.limb_dimensions_x.append( [0]*self.number_elements_per_limb[i] )
      self.limb_dimensions_y.append( [0]*self.number_elements_per_limb[i] )
      self.limb_dimensions_z.append( [0]*self.number_elements_per_limb[i] )
      self.limb_positions_x.append( [0]*self.number_elements_per_limb[i] )
      self.limb_positions_y.append( [0]*self.number_elements_per_limb[i] )
      self.limb_positions_z.append( [0]*self.number_elements_per_limb[i] )
      self.limb_joint_element_x.append( [0]*self.number_elements_per_limb[i] )
      self.limb_joint_element_y.append( [0]*self.number_elements_per_limb[i] )
      self.limb_joint_element_z.append( [0]*self.number_elements_per_limb[i] )
      self.joint_name_limb_list.append( [0]*self.number_elements_per_limb[i] )
      self.limb_names.append( [0]*self.number_elements_per_limb[i] )
      self.orientation_with_respect_to_first_limbs.append( [0]*self.number_elements_per_limb[i] )
      self.limb_sensors.append( [0]*self.number_elements_per_limb[i] )
      for j in range(self.number_elements_per_limb[i] ):
        self.limb_sensors[i][j] = random.randint(0,1)
      self.limb_weights.append([])
      self.numMotorNeurons[i] = self.number_elements_per_limb[i]-1
      self.numSensorNeurons[i] = sum(self.limb_sensors[i])
    #print("Number elements per limb")
    #print(self.number_elements_per_limb)
    #self.weights = self.weights * 2 - 1
    self.myID = idChosen
    #print(self.weights)
    #def Evaluate(self,directOrGUI):
  def Start_Simulation(self,directOrGUI):
    self.Create_World()
    if not self.simulation_start:
      self.Create_Body_and_Brain()
      self.simulation_start = True
    if self.simulation_start:
      self.Create_New_Updated_Brain_and_Body()
    if self.fitness_call_number == 2:
      self.fitness_update = self.fitness
    elif self.fitness_call_number > 2:
      pass
    else:
      self.fitness_update = 0
    #statement = "python3 simulate.py " + directOrGUI + " " + str(self.myID) + " 2&>1 &"
    self.fitness_call_number = self.fitness_call_number + 1
    statement = "python3 simulate.py " + directOrGUI + " " + str(self.myID) + " " + str(self.fitness_call_number) + " " + str(self.fitness_update) + " &"
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
    body_file = "body" + str(self.myID) + ".urdf"
    pyrosim.Start_URDF(body_file)
    self.number_body_elements = self.body_num_el
    self.names_body_elements = ["0"]*self.number_body_elements
    self.body_element_width = [0]*self.number_body_elements
    self.body_element_length = [0]*self.number_body_elements
    self.body_element_height = [0]*self.number_body_elements
    self.body_element_x = [0]*self.number_body_elements # this will change, build in +x directiomn
    self.body_element_y = [0]*self.number_body_elements
    self.body_element_z = [0]*self.number_body_elements
    self.joint_element_x = [0]*(self.number_body_elements-1) # this will change, build in +x directiomn
    self.joint_element_y = [0]*(self.number_body_elements-1)
    self.joint_element_z = [0]*(self.number_body_elements-1)
    self.touch_sensor_no_sensor = self.touch_sensor_no_sensor_new
    for i in range(self.number_body_elements):
      self.body_element_width[i] = round(random.uniform(0.1,0.5),3)
      self.body_element_length[i] = round(random.uniform(0.1,0.5),3)
      self.body_element_height[i] = round(random.uniform(0.1,0.5),3)
      #touch_sensor_no_sensor[i] = random.randint(0,1)
      self.names_body_elements[i] = str(i)
    ii = self.number_body_elements
    for i in range(self.number_limbs):
      self.location_on_main_body_limb[i] = random.randint(0,self.number_body_elements-1)
      for j in range(self.number_elements_per_limb[i]):
        self.limb_dimensions_x[i][j] = (round(random.uniform(0.1,0.5),3))
        self.limb_dimensions_y[i][j] = (round(random.uniform(0.1,0.5),3))
        self.limb_dimensions_z[i][j] = (round(random.uniform(0.1,0.5),3))
        self.orientation_with_respect_to_first_limbs[i][j] = (random.randint(2,5))
        self.limb_names[i][j] = str(ii)
        ii = ii + 1
      self.orientation_with_respect_to_first_limbs[i][0] = random.randint(1,5)
      #self.limb_joint_element_x[i][0] = 0
      #self.limb_joint_element_y[i][0] = 0
      #self.limb_joint_element_z[i][0] = 0
      #self.limb_positions_x[i][0] = 0
      #self.limb_positions_y[i][0] = 0
      #self.limb_positions_z[i][0] = 0
    #print("LOCATION ON MAIN BODY LIMB")
    #print(self.location_on_main_body_limb)
    self.body_element_x[0] = 0
    self.body_element_z[0] = 3
    self.orientation_with_respect_to_first[0] = 1
    if self.number_body_elements != 1:
      self.joint_element_x[0] = 0 + self.body_element_width[0]/2
      self.joint_element_z[0] = 3
    for i in range(self.number_body_elements-1):
      if self.number_body_elements == 1:
        continue
      if (i >= (self.number_body_elements-2)):
        continue
      
      if self.orientation_with_respect_to_first[i+1] == 1:
        self.joint_element_x[i+1] = self.body_element_width[i+1]/2
        self.body_element_x[i+1] = self.body_element_width[i+1]/2
      elif self.orientation_with_respect_to_first[i+1] == 2:
        if self.orientation_with_respect_to_first[i] == 2:
          self.joint_element_y[i+1] = self.body_element_length[i+1]/2
          self.body_element_y[i+1] = self.body_element_length[i+1]/2
        else:
          self.joint_element_x[i+1] = self.body_element_width[i]/2
          self.joint_element_y[i+1] = self.body_element_length[i]/2
          #body_element_x[i+1] = body_element_width[i+1]/2
          self.body_element_y[i+1] = self.body_element_length[i+1]/2
      elif self.orientation_with_respect_to_first[i+1] == 3:
        if self.orientation_with_respect_to_first[i] == 3:
          self.joint_element_y[i+1] = -self.body_element_length[i+1]/2
          self.body_element_y[i+1] = -self.body_element_length[i+1]/2
        else:
          self.joint_element_x[i+1] = self.body_element_width[i]/2
          self.joint_element_y[i+1] = -1*self.body_element_length[i]/2
          #body_element_x[i+1] = body_element_width[i+1]/2
          self.body_element_y[i+1] = -1*self.body_element_length[i+1]/2
      elif self.orientation_with_respect_to_first[i+1] == 4:
        if self.orientation_with_respect_to_first[i] == 4:
          self.joint_element_z[i+1] = self.body_element_height[i+1]/2
          self.body_element_z[i+1] = self.body_element_height[i+1]/2
        else:
          self.joint_element_x[i+1] = self.body_element_width[i]/2
          self.joint_element_z[i+1] = self.body_element_height[i]/2
          #body_element_x[i+1] = body_element_width[i+1]/2
          self.body_element_z[i+1] = self.body_element_height[i+1]/2
      elif self.orientation_with_respect_to_first[i+1] == 5:
        if self.orientation_with_respect_to_first[i] == 5:
          self.joint_element_z[i+1] = -self.body_element_height[i+1]/2
          self.body_element_z[i+1] = -self.body_element_height[i+1]/2
        else:
          self.joint_element_x[i+1] = self.body_element_width[i]/2
          self.joint_element_z[i+1] = -1*self.body_element_height[i]/2
          #body_element_x[i+1] = body_element_width[i+1]/2
          self.body_element_z[i+1] = -1*self.body_element_height[i+1]/2
    for i in range(self.number_limbs):
      for j in range(self.number_elements_per_limb[i]-1):
        if self.number_elements_per_limb[i] == 1:
          continue
        if (i >= (self.number_elements_per_limb[i]-2)):
          continue
        if self.orientation_with_respect_to_first_limbs[i][j+1] == 1:
          self.limb_joint_element_x[i][j+1] = self.limb_dimensions_x[i][j+1]/2
          self.limb_positions_x[i][j+1] = self.limb_dimensions_x[i][j+1]/2
        elif self.orientation_with_respect_to_first_limbs[i][j+1] == 2:
          if self.orientation_with_respect_to_first_limbs[i][j] == 2:
            self.limb_joint_element_y[i][j+1] = self.limb_dimensions_y[i][j+1]/2
            self.limb_positions_y[i][j+1] = self.limb_dimensions_y[i][j+1]/2
          else:
            self.limb_joint_element_x[i][j+1] = self.limb_dimensions_x[i][j]/2
            self.limb_joint_element_y[i][j+1] = self.limb_dimensions_y[i][j]/2
            #body_element_x[i+1] = body_element_width[i+1]/2
            self.limb_positions_y[i][j+1] = self.limb_dimensions_y[i][j+1]/2
        elif self.orientation_with_respect_to_first_limbs[i][j+1] == 3:
          if self.orientation_with_respect_to_first_limbs[i][j] == 3:
            self.limb_joint_element_y[i][j+1] = -self.limb_dimensions_y[i][j+1]/2
            self.limb_positions_y[i][j+1] = -self.limb_dimensions_y[i][j+1]/2
          else:
            self.limb_joint_element_x[i][j+1] = self.limb_dimensions_x[i][j]/2
            self.limb_joint_element_y[i][j+1] = -1*self.limb_dimensions_y[i][j]/2
            #body_element_x[i+1] = body_element_width[i+1]/2
            self.limb_positions_y[i][j+1] = -1*self.limb_dimensions_y[i][j+1]/2
        elif self.orientation_with_respect_to_first_limbs[i][j+1] == 4:
          if self.orientation_with_respect_to_first_limbs[i][j] == 4:
            self.limb_joint_element_z[i][j+1] = self.limb_dimensions_z[i][j+1]/2
            self.limb_positions_z[i][j+1] = self.limb_dimensions_z[i][j+1]/2
          else:
            self.limb_joint_element_x[i][j+1] = self.limb_dimensions_x[i][j]/2
            self.limb_joint_element_z[i][j+1] = self.limb_dimensions_z[i][j]/2
            #body_element_x[i+1] = body_element_width[i+1]/2
            self.limb_positions_z[i][j+1] = self.limb_dimensions_z[i][j+1]/2
        elif self.orientation_with_respect_to_first_limbs[i][j+1] == 5:
          if self.orientation_with_respect_to_first_limbs[i][j] == 5:
            self.limb_joint_element_z[i][j+1] = -self.limb_dimensions_z[i][j+1]/2
            self.limb_positions_z[i][j+1] = -self.limb_dimensions_z[i][j+1]/2
          else:
            self.limb_joint_element_x[i][j+1] = self.limb_dimensions_x[i][j]/2
            self.limb_joint_element_z[i][j+1] = -1*self.limb_dimensions_z[i][j]/2
            #body_element_x[i+1] = body_element_width[i+1]/2
            self.limb_positions_z[i][j+1] = -1*self.limb_dimensions_z[i][j+1]/2
   
    
    
    self.joint_name_list = []
    for i in range(self.number_body_elements):
      #print(touch_sensor_no_sensor)
      if self.touch_sensor_no_sensor[i]:
        pyrosim.Send_Cube(name=self.names_body_elements[i], pos=[self.body_element_x[i],self.body_element_y[i],self.body_element_z[i]], size=[self.body_element_width[i],self.body_element_length[i],self.body_element_height[i]],COLOR_NAME="Green",RED="0.0",GREEN="1.0",BLUE="0.0")
      else:
        pyrosim.Send_Cube(name=self.names_body_elements[i], pos=[self.body_element_x[i],self.body_element_y[i],self.body_element_z[i]], size=[self.body_element_width[i],self.body_element_length[i],self.body_element_height[i]],COLOR_NAME="Blue",RED="0.0",GREEN="0.0",BLUE="1.0")
      if (self.number_body_elements == 1):
        break
      if (i >= (self.number_body_elements - 1)): # add -1
        break
      name_new = self.names_body_elements[i] + "_" + self.names_body_elements[i+1]
      self.joint_name_list.append(name_new)
      pyrosim.Send_Joint(name = name_new , parent= self.names_body_elements[i] , child = self.names_body_elements[i+1] , type = "revolute", position = [self.joint_element_x[i],self.joint_element_y[i],self.joint_element_z[i]], jointAxis = "0 0 1")
    #print("NAMES BODY ELEMENTS")
    #print(names_body_elements)
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
        
        if j == 0:
          #print("BRANCHING ON")
          #print(self.limb_names[i][j])
          #print("CONNECTING TO")
          #print(names_body_elements[self.location_on_main_body_limb[i]])
          name_link_torso =  self.names_body_elements[self.location_on_main_body_limb[i]] + "_" + self.limb_names[i][j]
          name_link_torso_2 =  self.limb_names[i][j] + "_" + self.limb_names[i][j+1]
          self.joint_name_limb_list[i][j] = name_link_torso
          self.joint_name_limb_list[i][j+1] = name_link_torso_2
          #name_link_torso_second = names_body_elements[0] + "_" + self.limb_names[i][j]
          #pyrosim.Send_Joint(name = name_link_torso_second , parent=names_body_elements[0] , child = self.limb_names[i][j] , type = "revolute", position = [self.limb_joint_element_x[i][j],self.limb_joint_element_y[i][j],self.limb_joint_element_z[i][j]], jointAxis = "0 0 1")
          pyrosim.Send_Joint(name = name_link_torso , parent= self.names_body_elements[self.location_on_main_body_limb[i]], child = self.limb_names[i][j] , type = "revolute", position = [self.limb_joint_element_x[i][j],self.limb_joint_element_y[i][j],self.limb_joint_element_z[i][j]], jointAxis = "0 0 1")
          pyrosim.Send_Joint(name = name_link_torso_2 , parent= self.limb_names[i][j], child = self.limb_names[i][j+1] , type = "revolute", position = [self.limb_joint_element_x[i][j],self.limb_joint_element_y[i][j],self.limb_joint_element_z[i][j]], jointAxis = "0 0 1")
          #pyrosim.Send_Joint(name = name_new , parent= names_body_elements[self.location_on_main_body_limb[i]] , child = self.limb_names[i][j] , type = "revolute", position = [self.limb_joint_element_x[i][j],self.limb_joint_element_y[i][j],self.limb_joint_element_z[i][j]], jointAxis = "0 0 1")
        else:
          name_new = self.limb_names[i][j] + "_" + self.limb_names[i][j+1]
          name_link_torso_second = self.limb_names[i][j] + "_" + self.limb_names[i][j+1]
          self.joint_name_limb_list[i][j+1] = name_link_torso_second
          pyrosim.Send_Joint(name = name_link_torso_second , parent= self.limb_names[i][j] , child = self.limb_names[i][j+1] , type = "revolute", position = [self.limb_joint_element_x[i][j],self.limb_joint_element_y[i][j],self.limb_joint_element_z[i][j]], jointAxis = "0 0 1")
    pyrosim.End()
    self.Create_Brain()
    
  def Create_Brain(self):
    
    brain_file = "brain" + str(self.myID) + ".nndf"
    #print("creating brain")
    pyrosim.Start_NeuralNetwork(brain_file)
    sensor_name_index = 0
    for i in range(self.number_body_elements):
      if self.touch_sensor_no_sensor[i]:
        pyrosim.Send_Sensor_Neuron(name = sensor_name_index, linkName = self.names_body_elements[i])
        sensor_name_index = sensor_name_index + 1
    motor_name_index = sensor_name_index
    for element_name in self.joint_name_list:
      pyrosim.Send_Motor_Neuron( name = motor_name_index , jointName = element_name)
      motor_name_index = motor_name_index + 1
    sensor_neurons = list(range(sensor_name_index))
    motor_neurons = list(range(motor_name_index-sensor_name_index))
    for i in range(len(motor_neurons)):
      motor_neurons[i] = motor_neurons[i] + sensor_name_index
    for currentRow in sensor_neurons:
      for currentColumn in motor_neurons:
        pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn, weight = self.weights[currentRow-1][currentColumn-sensor_name_index-1] )
        
    sensor_name_index_limbs = 0
    motor_name_index_limbs = 0
    
    for i in range(self.number_limbs):
      #print(self.joint_name_limb_list[i])
      for j in range(self.number_elements_per_limb[i]):
        if self.limb_sensors[i][j]:
          pyrosim.Send_Sensor_Neuron(name = sensor_name_index_limbs, linkName = self.limb_names[i][j])
          sensor_name_index_limbs = sensor_name_index_limbs + 1
      motor_name_index_limbs = sensor_name_index_limbs
      for element_name in self.joint_name_limb_list[i]:
        if element_name != 0:
          pyrosim.Send_Motor_Neuron( name = motor_name_index_limbs , jointName = element_name)
          motor_name_index_limbs = motor_name_index_limbs + 1
      sensor_neurons_limbs = list(range(sensor_name_index_limbs))
      motor_neurons_limbs = list(range(motor_name_index_limbs-sensor_name_index_limbs))
      for k in range(len(motor_neurons_limbs)):
        motor_neurons_limbs[k] = motor_neurons_limbs[k] + sensor_name_index_limbs
      for l in range(len(sensor_neurons_limbs)):
        self.limb_weights[i].append([])
      for currentRow in sensor_neurons_limbs:
        for currentColumn in motor_neurons_limbs:
          self.limb_weights[i][currentRow].append( 2*random.random() - 1 )
          pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn, weight = self.limb_weights[i][currentRow][currentColumn-sensor_name_index_limbs-1] )
      sensor_name_index_limbs = 0
      motor_name_index_limbs = 0
    pyrosim.End()
    
  def Mutate(self):
    #body
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
      
    #limbs
    for i in range(self.number_limbs):
      if self.numSensorNeurons[i]-1 == 0 or self.numSensorNeurons[i]-1 == -1:
        row_chosen = 0
      else:
        row_chosen = random.randint(0,self.numSensorNeurons[i]-1)
      if self.numMotorNeurons[i]-1 == 0 or self.numMotorNeurons[i]-1 == -1:
        col_chosen = 0
      else:
        col_chosen = random.randint(0,self.numMotorNeurons[i]-1)
      if self.numMotorNeurons[i] != 0 and self.numSensorNeurons[i] !=0:
        self.limb_weights[i][row_chosen][col_chosen] = random.random() * 2 - 1
    for i in range(self.number_limbs):
      if self.numSensorNeurons[i]-1 == 0 or self.numSensorNeurons[i]-1 == -1:
        row_chosen = 0
      else:
        row_chosen = random.randint(0,self.numSensorNeurons[i]-1)
      if self.numMotorNeurons[i]-1 == 0 or self.numMotorNeurons[i]-1 == -1:
        col_chosen = 0
      else:
        col_chosen = random.randint(0,self.numMotorNeurons[i]-1)
      if self.numMotorNeurons[i] != 0 and self.numSensorNeurons[i] !=0:
        self.limb_weights[i][row_chosen][col_chosen] = random.random() * 2 - 1
    for i in range(self.number_limbs):
      if self.numSensorNeurons[i]-1 == 0 or self.numSensorNeurons[i]-1 == -1:
        row_chosen = 0
      else:
        row_chosen = random.randint(0,self.numSensorNeurons[i]-1)
      if self.numMotorNeurons[i]-1 == 0 or self.numMotorNeurons[i]-1 == -1:
        col_chosen = 0
      else:
        col_chosen = random.randint(0,self.numMotorNeurons[i]-1)
      if self.numMotorNeurons[i] != 0 and self.numSensorNeurons[i] !=0:
        self.limb_weights[i][row_chosen][col_chosen] = random.random() * 2 - 1
    
    # remove limb element possibly
    limb_selected = random.randint(0,self.number_limbs-1)
    remove_limb_binary = random.random()
    if remove_limb_binary > 0.5:
      if self.number_elements_per_limb[limb_selected] == 1:
        if len(self.limb_names[limb_selected]) != 0:
          self.limb_names[limb_selected].pop()
        if len(self.joint_name_limb_list[limb_selected]) != 0:
          self.joint_name_limb_list[limb_selected].pop()
      self.number_elements_per_limb[limb_selected] = self.number_elements_per_limb[limb_selected] - 1
      if len(self.joint_name_limb_list[limb_selected]) != 0:
        self.joint_name_limb_list[limb_selected].pop()
      if len(self.joint_name_limb_list[limb_selected]) == 1:
          self.joint_name_limb_list[limb_selected].pop()
          self.number_elements_per_limb[limb_selected] = self.number_elements_per_limb[limb_selected] - 1
      if len(self.limb_names[limb_selected]) != 0:
        self.limb_names[limb_selected].pop()
      #self.Create_New_Updated_Brain_and_Body()

    #resize limb #1
    i = random.randint(0,self.number_limbs-1)
    if self.number_elements_per_limb[i]-1 > 0:
      j = random.randint(0,self.number_elements_per_limb[i]-1)
      resize_limb_binary = random.random()
      if resize_limb_binary > 0.50:
        if self.number_elements_per_limb[i] == 1:
          if len(self.limb_names[i]) != 0:
            self.limb_dimensions_x[i][j]=(round(random.uniform(0.1,0.5),3))
            self.limb_dimensions_y[i][j]=(round(random.uniform(0.1,0.5),3))
            self.limb_dimensions_z[i][j]=(round(random.uniform(0.1,0.5),3))
            #self.limb_names[limb_selected].pop()
          if len(self.joint_name_limb_list[i]) != 0:
            self.limb_dimensions_x[i][j]=(round(random.uniform(0.1,0.5),3))
            self.limb_dimensions_y[i][j]=(round(random.uniform(0.1,0.5),3))
            self.limb_dimensions_z[i][j]=(round(random.uniform(0.1,0.5),3))
      '''
          #self.joint_name_limb_list[limb_selected].pop()
      #self.number_elements_per_limb[limb_selected] = self.number_elements_per_limb[limb_selected] - 1
      if len(self.joint_name_limb_list[limb_selected]) != 0:
        #self.joint_name_limb_list[limb_selected].pop()
      if len(self.joint_name_limb_list[limb_selected]) == 1:
          #self.joint_name_limb_list[limb_selected].pop()
          #self.number_elements_per_limb[limb_selected] = self.number_elements_per_limb[limb_selected] - 1
      if len(self.limb_names[limb_selected]) != 0:
        #self.limb_names[limb_selected].pop()
      '''
      
    #resize limb #2
    i = random.randint(0,self.number_limbs-1)
    if self.number_elements_per_limb[i]-1 > 0:
      j = random.randint(0,self.number_elements_per_limb[i]-1)
      resize_limb_binary = random.random()
      if resize_limb_binary > 0.50:
        if self.number_elements_per_limb[i] == 1:
          if len(self.limb_names[i]) != 0:
            self.limb_dimensions_x[i][j]=(round(random.uniform(0.1,0.5),3))
            self.limb_dimensions_y[i][j]=(round(random.uniform(0.1,0.5),3))
            self.limb_dimensions_z[i][j]=(round(random.uniform(0.1,0.5),3))
            #self.limb_names[limb_selected].pop()
          if len(self.joint_name_limb_list[i]) != 0:
            self.limb_dimensions_x[i][j]=(round(random.uniform(0.1,0.5),3))
            self.limb_dimensions_y[i][j]=(round(random.uniform(0.1,0.5),3))
            self.limb_dimensions_z[i][j]=(round(random.uniform(0.1,0.5),3))
      
    # add limb element possibly
      
  def Create_New_Updated_Brain_and_Body(self):
    body_file = "body" + str(self.myID) + ".urdf"
    pyrosim.Start_URDF(body_file)
    for i in range(self.number_body_elements):
      if self.touch_sensor_no_sensor[i]:
        pyrosim.Send_Cube(name=self.names_body_elements[i], pos=[self.body_element_x[i],self.body_element_y[i],self.body_element_z[i]], size=[self.body_element_width[i],self.body_element_length[i],self.body_element_height[i]],COLOR_NAME="Green",RED="0.0",GREEN="1.0",BLUE="0.0")
      else:
        pyrosim.Send_Cube(name=self.names_body_elements[i], pos=[self.body_element_x[i],self.body_element_y[i],self.body_element_z[i]], size=[self.body_element_width[i],self.body_element_length[i],self.body_element_height[i]],COLOR_NAME="Blue",RED="0.0",GREEN="0.0",BLUE="1.0")
      if (self.number_body_elements == 1):
        break
      if (i >= (self.number_body_elements - 1)): # add -1
        break
      pyrosim.Send_Joint(name = self.joint_name_list[i] , parent= self.names_body_elements[i] , child = self.names_body_elements[i+1] , type = "revolute", position = [self.joint_element_x[i],self.joint_element_y[i],self.joint_element_z[i]], jointAxis = "0 0 1")
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
        
        if j == 0:
          #print(self.names_body_elements[self.location_on_main_body_limb[i]],"and",self.limb_names[i][j])
          pyrosim.Send_Joint(name = self.joint_name_limb_list[i][j] , parent= self.names_body_elements[self.location_on_main_body_limb[i]], child = self.limb_names[i][j] , type = "revolute", position = [self.limb_joint_element_x[i][j],self.limb_joint_element_y[i][j],self.limb_joint_element_z[i][j]], jointAxis = "0 0 1")
          #print(self.limb_names[i][j],"and",self.limb_names[i][j+1])
          pyrosim.Send_Joint(name = self.joint_name_limb_list[i][j+1] , parent= self.limb_names[i][j], child = self.limb_names[i][j+1] , type = "revolute", position = [self.limb_joint_element_x[i][j],self.limb_joint_element_y[i][j],self.limb_joint_element_z[i][j]], jointAxis = "0 0 1")
        else:
          #print(self.limb_names[i][j],"and",self.limb_names[i][j+1])
          pyrosim.Send_Joint(name = self.joint_name_limb_list[i][j+1] , parent= self.limb_names[i][j] , child = self.limb_names[i][j+1] , type = "revolute", position = [self.limb_joint_element_x[i][j],self.limb_joint_element_y[i][j],self.limb_joint_element_z[i][j]], jointAxis = "0 0 1")
    pyrosim.End()
    
    
    brain_file = "brain" + str(self.myID) + ".nndf"
    print("creating brain")
    pyrosim.Start_NeuralNetwork(brain_file)
    sensor_name_index = 0
    for i in range(self.number_body_elements):
      if self.touch_sensor_no_sensor[i]:
        pyrosim.Send_Sensor_Neuron(name = sensor_name_index, linkName = self.names_body_elements[i])
        sensor_name_index = sensor_name_index + 1
    motor_name_index = sensor_name_index
    for element_name in self.joint_name_list:
      pyrosim.Send_Motor_Neuron( name = motor_name_index , jointName = element_name)
      motor_name_index = motor_name_index + 1
    sensor_neurons = list(range(sensor_name_index))
    motor_neurons = list(range(motor_name_index-sensor_name_index))
    for i in range(len(motor_neurons)):
      motor_neurons[i] = motor_neurons[i] + sensor_name_index
    for currentRow in sensor_neurons:
      for currentColumn in motor_neurons:
        pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn, weight = self.weights[currentRow-1][currentColumn-sensor_name_index-1] )
        
    sensor_name_index_limbs = 0
    motor_name_index_limbs = 0
    for i in range(self.number_limbs):
      #print(self.joint_name_limb_list[i])
      for j in range(self.number_elements_per_limb[i]):
        if self.limb_sensors[i][j]:
          pyrosim.Send_Sensor_Neuron(name = sensor_name_index_limbs, linkName = self.limb_names[i][j])
          sensor_name_index_limbs = sensor_name_index_limbs + 1
      motor_name_index_limbs = sensor_name_index_limbs
      for element_name in self.joint_name_limb_list[i]:
        if element_name != 0:
          pyrosim.Send_Motor_Neuron( name = motor_name_index_limbs , jointName = element_name)
          motor_name_index_limbs = motor_name_index_limbs + 1
      sensor_neurons_limbs = list(range(sensor_name_index_limbs))
      motor_neurons_limbs = list(range(motor_name_index_limbs-sensor_name_index_limbs))
      for k in range(len(motor_neurons_limbs)):
        motor_neurons_limbs[k] = motor_neurons_limbs[k] + sensor_name_index_limbs
      for currentRow in sensor_neurons_limbs:
        for currentColumn in motor_neurons_limbs:
          pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn, weight = self.limb_weights[i][currentRow][currentColumn-sensor_name_index_limbs-1] )
      sensor_name_index_limbs = 0
      motor_name_index_limbs = 0
    pyrosim.End()
      
  def Set_ID(self,valueChosen):
    self.myID = valueChosen
