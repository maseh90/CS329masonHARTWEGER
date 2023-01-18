import pyrosim.pyrosim as pyrosim
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
    self.valueTimes = numpy.arange(0,1000,1)
    self.motorValues = self.amplitudeFront * numpy.sin(self.frequencyFront*self.valueTimes + self.phaseOffsetFront)
  def Act(self):
    self.Set_Value()
  def Set_Value(self,robotIdInput,timeStep):
    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotIdInput,
    jointName = self.jointName,
    controlMode = p.POSITION_CONTROL,
    targetPosition = self.motorValues[timeStep],
    maxForce = 150)
