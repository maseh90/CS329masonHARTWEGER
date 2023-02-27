import pyrosim.pyrosim as pyrosim
import constants as c
import copy
import os
from solution import SOLUTION
import math

import matplotlib
import matplotlib.pyplot as plt

class PARALLEL_HILL_CLIMBER:
  def __init__(self):
    os.system("rm brain*.nndf")
    os.system("rm fitness*.nndf")
    self.parents = {}
    self.fitness_scores_gens = []
    self.nextAvailableID = 0
    for key_parent in range(c.populationSize):
      self.parents[key_parent] = SOLUTION(self.nextAvailableID)
      self.nextAvailableID = self.nextAvailableID + 1
    #print(self.parents)
    #self.parent.Evaluate("DIRECT")
  def Evolve(self):
    self.Evaluate(self.parents)
    #self.parent.Evaluate("GUI")
    for currentGeneration in range(c.numberOfGenerations):
      print("GENERATION #: ",currentGeneration)
      self.Evolve_For_One_Generation()
      fitness_comp = 10000
      for key_parent in self.parents:
        if self.parents[key_parent].fitness < fitness_comp:
          fitness_comp = self.parents[key_parent].fitness
      self.fitness_scores_gens.append(fitness_comp)
    #self.parent.Evaluate("GUI")
  def Evolve_For_One_Generation(self):
    self.Spawn()
    self.Mutate()
    #self.child.Evaluate("DIRECT")
    self.Evaluate(self.children)
    self.Print()
    #print("\n\nPARENT FITNESS: ",self.parent.fitness," CHILD FITNESS: ",self.child.fitness,"\n")
    #exit()
    self.Select()
  def Print(self):
    print("\n")
    print("PARENT FITNESS")
    for key_parent in self.parents:
      print(self.parents[key_parent].fitness)
    print("CHILDREN FITNESS")
    for key_child in self.children:
      print(self.children[key_child].fitness)
    print("\n")
  def Spawn(self):
    self.children = {}
    i = 0
    for key_parent in self.parents:
      self.children[i] = copy.deepcopy(self.parents[key_parent])
      self.children[i].Set_ID(self.nextAvailableID)
      self.nextAvailableID = self.nextAvailableID + 1
      i = i + 1
    #print(self.children)
    #self.child = copy.deepcopy(self.parent)
    #self.child.Set_ID(self.nextAvailableID)
    #self.nextAvailableID = self.nextAvailableID + 1
  def Mutate(self):
    #print("PARENT")
    #print(self.parent.weights)
    for key_child in self.children:
      self.children[key_child].Mutate()
    #print("CHILD")
    #print(self.child.weights)
    #exit()
  def Evaluate(self,solutions):
    for key in solutions:
      solutions[key].Start_Simulation("DIRECT")
    for key in solutions:
      solutions[key].Wait_For_Simulation_To_End()
  def Select(self):
    i = 0
    for key_parent in self.parents:
      if math.isnan(self.parents[key_parent].fitness) and not math.isnan(self.children[i]):
        self.parents[key_parent] = self.children[i]
        self.parents[key_parent].fitness = 1000
      elif (self.parents[key_parent].fitness > self.children[i].fitness):
        self.parents[key_parent] = self.children[i]
      i = i + 1
    #if (self.parent.fitness > self.child.fitness):
    #  self.parent = self.child
    #print("CHILD FITNESS:")
    #print(self.child.fitness)
    #print("PARENT FITNESS:")
    #print(self.parent.fitness)
    #exit()
  def Show_Best(self):
    fitness_comp = 10000
    for key_parent in self.parents:
      
      if self.parents[key_parent].fitness < fitness_comp:
        fitness_comp = self.parents[key_parent].fitness
        best_parent = self.parents[key_parent]
    print(fitness_comp)
    index_list = list(range(0,len(self.fitness_scores_gens)))
    plt.plot(index_list,self.fitness_scores_gens)
    plt.xlabel("Generation #")
    plt.ylabel("Fitness Score")
    plt.savefig("FITNESS_PLOT.png")
    best_parent.Start_Simulation("GUI")
    
