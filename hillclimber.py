import pyrosim.pyrosim as pyrosim
import constants as c
import copy
from solution import SOLUTION
class HILL_CLIMBER:
  def __init__(self):
    self.parent = SOLUTION()
    self.parent.Evaluate("DIRECT")
  def Evolve(self):
    for currentGeneration in range(c.numberOfGenerations):
      self.Evolve_For_One_Generation()
  def Evolve_For_One_Generation(self):
    self.Spawn()
    self.Mutate()
    self.child.Evaluate("DIRECT")
    print("\n\nPARENT FITNESS: ",self.parent.fitness," CHILD FITNESS: ",self.child.fitness,"\n")
    #exit()
    self.Select()
  def Spawn(self):
    self.child = copy.deepcopy(self.parent)
  def Mutate(self):
    #print("PARENT")
    #print(self.parent.weights)
    self.child.Mutate()
    #print("CHILD")
    #print(self.child.weights)
    #exit()
  def Evaluate(self):
    pass
  def Select(self):
    if (self.parent.fitness < self.child.fitness):
      self.parent = self.child
    #print("CHILD FITNESS:")
    #print(self.child.fitness)
    #print("PARENT FITNESS:")
    #print(self.parent.fitness)
    #exit()
  def Show_Best(self):
    self.parent.Evaluate("GUI")
