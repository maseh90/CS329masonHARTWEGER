import pyrosim.pyrosim as pyrosim
import constants as c
class MOTOR:
  def __init__(self,jointNameInput):
    self.jointName = jointNameInput
    self.Prepare_to_Act()
  def Prepare_to_Act(self):
    self.amplitude = c.amplitude
    self.frequency = c.frequency
    self.offset = c.offset
