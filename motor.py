import pyrosim.pyrosim as pyrosim
import pybullet as p
import constants as c
import numpy
class MOTOR:
  def __init__(self,jointNameInput):
    self.jointName = jointNameInput
    self.Prepare_to_Act()
  def Prepare_to_Act(self):
    self.amplitude = c.amplitude
    self.frequency = c.frequency
    self.offset = c.offset
    self.valueTimes = numpy.arange(0,c.simulationSteps,1)
    if self.jointName == "Torso_BackLeg":
      self.motorValues = self.amplitude * numpy.sin(self.frequency/2*self.valueTimes + self.offset)
    if self.jointName == "Torso_FrontLeg":
      self.motorValues = self.amplitude * numpy.sin(self.frequency*self.valueTimes + self.offset)
  def Act(self):
    self.Set_Value()
  def Set_Value(self,robotIdInput,desiredAngle):
    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotIdInput,
    jointName = self.jointName,
    controlMode = p.POSITION_CONTROL,
    targetPosition = desiredAngle,
    maxForce = c.maxForce)
