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
    self.valueTimes = numpy.arrange(0,1000,1)
    self.motorValues = self.amplitudeFront * numpy.sin(self.frequencyFront*self.valueTimes + self.phaseOffsetFront)
  def Act(self):
    pass
