import pyrosim.pyrosim as pyrosim

from solution import SOLUTION
class HILL_CLIMBER:
  def __init__(self):
    self.parent = SOLUTION()
    self.parent.Evaluate()
  def Evolve(self):
    pass
