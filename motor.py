import pyrosim.pyrosim as pyrosim
import pybullet as p
import constants as c
import numpy
class MOTOR:
  def __init__(self,jointNameInput):
    self.jointName = jointNameInput
  def Act(self):
    self.Set_Value()
  def Set_Value(self,robotIdInput,desiredAngle):
    #print(desiredAngle)
    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotIdInput,
    jointName = self.jointName,
    controlMode = p.POSITION_CONTROL,
    targetPosition = desiredAngle,
    maxForce = c.maxForce)
