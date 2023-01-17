import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import constants as c
import numpy
import random
import math
class ROBOT:
  def __init__(self):
    self.sensors = {}
    self.motors = {}
    self.robotId = p.loadURDF("body.urdf")
    pyrosim.Prepare_To_Simulate(robotId)
