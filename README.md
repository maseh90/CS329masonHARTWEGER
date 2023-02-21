# CS396masonHARTWEGER
a repo to showcase my CS 396 bots - Mason Hartweger (Northwestern University)

## "Random 3D Creature" Branch Overview

This version includes a file that can be used to generate a random "3D creature" (a random number of randomly shaped cubes that can rotate along the x-y plane with respect to each other). All of the cubes are linked together via simple joints that can rotate in either direction except with respect to the z-axis (the joints cannot rotate up and down). However, due to the variety of positions that the joints are attached to each other by, the range of motion is not limited.

The creatures can move on their own (despite there being no evolution occurring), but these movements are often barely noticeable. Sometimes, the creatures tend to "tense" up and refuse to move. moreover, if a snake is generated with no sensor-enabled cubes touching the ground, then the creature will typically not move either. On each creature, the green cubes indicate body cubes tht have sensors attached. Cubes that are blue have no sensors attached. 

### How the Creatures are Built

The initial "body" of the creature is constructed as a "3D snake" of a kind. A random number of initial body components are built on top of each other (in 5 possible different directions trending in the positive x-direction). For example, successive body elements are built either on top of each other, on bottom of each other, to the right, to the left, and forwards as shown in this diagram.

This shows the 5 ways in which the bodies can build upon themselves with successive elements:
<img width="476" alt="Screen Shot 2023-02-21 at 2 29 23 PM" src="https://user-images.githubusercontent.com/79173890/220451455-5c61d6e8-6819-46c9-90f8-f77b84f99775.png">

After the initial body is constructed, a random number of branches (consisting of random numbers of elements) are built off the main branch in random directions. These branches then build upon themselves in the same manner as was mentioned above for the main branch (using the same 5 possible ways). Here are two examples of how branches can be constructed from the original main branch.

In Example 1, one main branch consisting of 11 elements is constructed. Then, 4 limbs (additional branches) are constructed branching from element numbers 2, 5, 9, and 10 on the main body.

In Example 2, one main branch consisting of 4 elements is constructed. Then, 3 limbs (additional branches) are constructed branching from element numbers 1, 1 (multiple branches can protude from same body element), and 2 on the main body. As shown, the limbs can be longer than the main branch to create a number of different morphologies.

<img width="506" alt="Screen Shot 2023-02-21 at 2 29 32 PM" src="https://user-images.githubusercontent.com/79173890/220451498-66c5de18-eb10-4644-89ec-73d2bebef751.png">


### Instructions for Running

NOTE: If the command "python3 search.py produces an error, simply run the command again in Terminal.

To run the repository shown, first download the repository somewhere on your local computer.

Then, install Python 3, install Pyrosim, and install Pybullet according to the instructions at https://www.reddit.com/r/ludobots/wiki/installation/.

  *NOTE: EARLIER VERSIONS OF PYTHON MAY NOT WORK.
  
Then, change drive (in Terminal) to the correct folder where the downloaded repository files are stored, and execute the command "python3 search.py" to run the simulation. The simulation will generate a random 3D creature every time this command is executed. If the command fails to generate a creature, simply terminate the program (if haulted) and re-run the command. In the next iteration, the creature will be able to change and evolve over generations, but this has not yet been implemented. 

### References and Source Material

This is a part of an assignment for the course CS 396 (Artificial Life) at Northwestern University.

This repository was developed using guidance from the r/ludobots subreddit and the [tutorials](https://www.reddit.com/r/ludobots/wiki/installation/) there. This repository uses Python3 and [the pybullet physics simulation](https://pybullet.org/wordpress/).
