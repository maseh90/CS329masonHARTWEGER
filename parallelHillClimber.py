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
    for i in range(c.populationSize):
      self.fitness_scores_gens.append([])
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
      if math.isnan(self.parents[key_parent].fitness) and not math.isnan(self.children[i].fitness):
        self.parents[key_parent] = self.children[i]
        self.parents[key_parent].fitness = 1000
      elif (self.parents[key_parent].fitness < self.children[i].fitness):
        self.parents[key_parent] = self.children[i]
      fitness_comp = self.parents[key_parent].fitness
      self.fitness_scores_gens[i].append(fitness_comp)  
      i = i + 1
      #fitness_comp = 10000
      #for key_parent in self.parents:
      #  if self.parents[key_parent].fitness < fitness_comp:
      #    fitness_comp = self.parents[key_parent].fitness
      #self.fitness_scores_gens.append(fitness_comp)
    #if (self.parent.fitness > self.child.fitness):
    #  self.parent = self.child
    #print("CHILD FITNESS:")
    #print(self.child.fitness)
    #print("PARENT FITNESS:")
    #print(self.parent.fitness)
    #exit()
  def Show_Best(self):
    fitness_comp_1 = 0
    for key_parent in self.parents:
      if self.parents[key_parent].fitness > fitness_comp_1:
        fitness_comp_1 = self.parents[key_parent].fitness
        best_parent = self.parents[key_parent]
    fitness_comp_2 = 0
    for key_parent in self.parents:
      if (self.parents[key_parent].fitness > fitness_comp_2) and (self.parents[key_parent].fitness != best_parent.fitness):
        fitness_comp_2 = self.parents[key_parent].fitness
        best_parent_2 = self.parents[key_parent]
    
    fitness_comp_change_1 = 0
    i = 0
    for key_parent in self.parents:
      change = abs(self.fitness_scores_gens[i][c.numberOfGenerations-2] - self.fitness_scores_gens[i][5])
      if change > fitness_comp_change_1:
        fitness_comp_change_1 = change
        best_parent_change_1 = self.parents[key_parent]
      i = i + 1

    fitness_comp_change_2 = 0
    i = 0
    for key_parent in self.parents:
      change = abs(self.fitness_scores_gens[i][c.numberOfGenerations-2] - self.fitness_scores_gens[i][5] )
      if (change > fitness_comp_change_2) and (self.parents[key_parent].fitness != best_parent_change_1.fitness):
        fitness_comp_change_2 = change
        best_parent_change_2 = self.parents[key_parent]
      i = i + 1
    #print(fitness_comp)
    index_list = list(range(0,len(self.fitness_scores_gens[0])))
    for i in range(c.populationSize):
      plt.plot(index_list,self.fitness_scores_gens[i])
    plt.xlabel("Generation #")
    plt.ylabel("Fitness Score")
    plt.savefig("FITNESS_PLOT.png")
    best_parent.Start_Simulation("GUI")
    best_parent.Wait_For_Simulation_To_End()
    best_parent_2.Start_Simulation("GUI")
    best_parent_2.Wait_For_Simulation_To_End()
    best_parent_change_1.Start_Simulation("GUI")
    best_parent_change_1.Wait_For_Simulation_To_End()
    best_parent_change_2.Start_Simulation("GUI")
    best_parent_change_2.Wait_For_Simulation_To_End()
    
