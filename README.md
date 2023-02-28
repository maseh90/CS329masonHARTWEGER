# CS396masonHARTWEGER
a repo to showcase my CS 396 bots - Mason Hartweger (Northwestern University)

## "EVOLVING Random 3D Creatures" Branch Overview

This version includes a file that can be used to generate a random "3D creature" (a random number of randomly shaped cubes that can rotate along the x-y plane with respect to each other), and these creatures are then EVOLVED according to a fitness function that maximizes the distance they travel away from the origin. All of the cubes are linked together via simple joints that can rotate in either direction except with respect to the z-axis (the joints cannot rotate up and down). However, due to the variety of positions that the joints are attached to each other by, the range of motion is not limited. On each creature, the green cubes indicate body cubes tht have sensors attached. Cubes that are blue have no sensors attached. 

### DOCUMENT SECTIONS
SECTION 1: How the Creatures are Built

SECTION 2: How the Creature's Brain is Generated

SECTION 3: How the Creatures are Evolved

SECTION 4: Examples of Evolution

SECTION 5: Instructions for Running

SECTION 6: References and Source Material

### 1. How the Creatures are Built

The initial "body" of the creature is constructed as a "3D snake" of a kind. A random number of initial body components are built on top of each other (in 5 possible different directions trending in the positive x-direction). For example, successive body elements are built either on top of each other, on bottom of each other, to the right, to the left, and forwards as shown in this diagram.

EXAMPLE:

<img width="263" alt="Screen Shot 2023-02-21 at 4 02 11 PM" src="https://user-images.githubusercontent.com/79173890/220468792-f05b5dae-9b5e-4be0-90c3-d6cb71663653.png">


This shows the 5 ways in which the bodies can build upon themselves with successive elements:
<img width="476" alt="Screen Shot 2023-02-21 at 2 29 23 PM" src="https://user-images.githubusercontent.com/79173890/220451455-5c61d6e8-6819-46c9-90f8-f77b84f99775.png">

After the initial body is constructed, a random number of branches (consisting of random numbers of elements) are built off the main branch in random directions. These branches then build upon themselves in the same manner as was mentioned above for the main branch (using the same 5 possible ways). Here are two examples of how branches can be constructed from the original main branch.

In Example 1, one main branch consisting of 11 elements is constructed. Then, 4 limbs (additional branches) are constructed branching from element numbers 2, 5, 9, and 10 on the main body.

In Example 2, one main branch consisting of 4 elements is constructed. Then, 3 limbs (additional branches) are constructed branching from element numbers 1, 1 (multiple branches can protude from same body element), and 2 on the main body. As shown, the limbs can be longer than the main branch to create a number of different morphologies.

<img width="506" alt="Screen Shot 2023-02-21 at 2 29 32 PM" src="https://user-images.githubusercontent.com/79173890/220451498-66c5de18-eb10-4644-89ec-73d2bebef751.png">

As of right now, the creatures are being built with a random range of elements on the main body (between 1 and 10 elements), which can be modified by changing the range of the self.body_num_el in the initialization of the solution file. The creatures are then given a random number of limbs (between 1 and 7 limbs), which can be modified by changing the range of the self.number_limbs in the initialization of the solution file. The number of elements per limb ranges between 2 and 7 and can be similarly modified by changing the self.number_elements_per_limb range.

### 2. How the Creature's Brain is Generated

The brains of the creatures are developed as follows. First, it must be understood that the sensor/motor neurons in each body/limb are completely independent of one another. Therefore, the body and all the respective limbs essentially have their own isolated connections. 

Within a given body/limb, motor neurons are placed at the intersection of all joints. Sensor neurons are randomly assigned to some of the individual segments. The sensor neurons are then connected to all the other motor neurons in the body/limb with random weights for each of the generated synapses. Once evolution is simulated, these weights will be constantly mutating and changing. Here is a diagram of how the brain is constructed for one of the limbs -- this figure can be generalized to all limbs/bodies in the 3D creatures.

This is a figure representing a single limb. There are 2 segments with sensors on them, which are each connected to all 3 of the motor neurons located at the links between segments. Each of the arrows represents a synapse connecting the neurons, which will be given a specific weight:

<img width="485" alt="Screen Shot 2023-02-21 at 4 18 25 PM" src="https://user-images.githubusercontent.com/79173890/220471616-e3b957fe-bf8d-4db9-92bd-3830ced9f3b3.png">

### 3. How the Creatures are Evolved

The creatures are evolved according to the following methodology. Firstly, there are a set of X (some number between 1 and 15) original parents. This represents Generation #0. These are the original parents. 

For each of these original parents, a random 3D body is generated from scratch. This random 3D body has an entirely random phenotype and genotype. As mentioned above, these parents can have different numbers of main body segments, different numbers of limbs and different numbers of body segments on those limbs, different body/limb segment locations, different joint locations between body/limb segments, differently sized body/limb segments, or differently positioned body/limb segments relative to each other. These bodies are completely random relative to the methodology used for generating them.

Then, these original parents are mutated in random ways over the course of Y (some number between 0 and infinity) generations. In each of these generations after the original (Generation #0), something is tweaked regarding the parents. On any given Generation #Y', the "parent" is considered to have the best "fitness" of all the generations thus far (in Generation #0, the original "parent" is considered to have the best fitness given there are no generations preceding this one). 

A fitness function is a function by which the creatures are evaluated for whether they will pass down their genetic information -- the results of the fitness function, after simulation has ended in each generation, is the "fitness" of that creature. For example, in these files, the fitness function analyzes the distance that the creature has traveled from the origin in the x-direction in a certain number of time steps:

 fitness(creature) = absolute_value(x_coordinate_creature_at_end_of_simulation)
 
At every generation #Y', the fitness function of the parent and child are evaluated. If the child has a greater fitness function, then the child (and all of its data and mutations) replaces the parent. After this, the child is then subjected to more mutations, and the process of replacement continues every generation.

There are two possible mutations that can occur at every generation #Y' :

1. Body Mutation (Random Deletions) : 

In each generation, a random limb of the body is chosen to possibly undergo a deletion of one of the body segments. Once this limb is selected, a "coin" is flipped to see if this limb will actually undergo a mutation (removal of the last segment of the limb). There is a 50% chance that the limb will NOT be modified (no changes to the body will occur in this generation) and a 50% chance the limb will be modified. Therefore, there is a 50% chance, on a given generation, that the body of the creature (the physical number of segments of the creature) will change. If the change improves fitness, then, as stated above, the genotype of the creature will change to reflect this in future generations.

2. Brain Mutation : 

In each creature, there are a random number of synapses generated (connections between sensor and motor neurons). As mentioned above, each of these synapses have weights. In each generation, 3 of the limbs of the creature are randomly selected. In each limb selected, one of the synapse weights in the respective limbs is modified. The new synapse weight is a random number between -1 and +1. This happens in every generation, and there is no chance that mutation of the synapse weights cannot occur. If the changes improve fitness, then they are carried over into the next generation, as mentioned above.

In every generation, the brain and body of the creature are completely regenerated to reflect the mutated body and brain. Whether these new bodies and brains replace the old bodies and brains depends on the effect on the fitness functions that the respective mutations have, relative to the parents.


### 4. Examples of Evolution



### 5. Instructions for Running

NOTE: If the command "python3 search.py produces an error, simply run the command again in Terminal.

To run the repository shown, first download the repository somewhere on your local computer.

Then, install Python 3, install Pyrosim, and install Pybullet according to the instructions at https://www.reddit.com/r/ludobots/wiki/installation/.

  *NOTE: EARLIER VERSIONS OF PYTHON MAY NOT WORK.
  
Then, change drive (in Terminal) to the correct folder where the downloaded repository files are stored, and execute the command "python3 search.py" to run the simulation. The simulation will generate a random 3D creature every time this command is executed. If the command fails to generate a creature, simply terminate the program (if haulted) and re-run the command. In the next iteration, the creature will be able to change and evolve over generations, but this has not yet been implemented. 

### 6. References and Source Material

This is a part of an assignment for the course CS 396 (Artificial Life) at Northwestern University.

This repository was developed using guidance from the r/ludobots subreddit and the [tutorials](https://www.reddit.com/r/ludobots/wiki/installation/) there. This repository uses Python3 and [the pybullet physics simulation](https://pybullet.org/wordpress/).
