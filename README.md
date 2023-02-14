# CS396masonHARTWEGER
a repo to showcase my CS 396 bots - Mason Hartweger (Northwestern University)

"snake" branch: This version includes a file that can be used to generate a random "snake" (a random number of randomly shaped cubes that can rotate along the x-y plane with respect to each other). All of the cubes are linked together via simple joints that can rotate in either direction except with respect to the z-axis (the joints cannot rotate up and down). The snakes can move on their own (despite there being no evolution occurring), but these movements are often barely noticeable. Sometimes, the snakes tend to "tense" up and refuse to move. moreover, if a snake is generated with no sensor-enabled cubes touching the ground, then the snake will typically not move either. On each snake, the green cubes indicate body cubes tht have sensors attached.Cubes that are blue have no sensors attached. NOTE: If the command "python3 search.py produces an error, simply run the command again in Terminal.

To run the repository shown, first download the repository somewhere on your local computer.

Then, install Python 3, install Pyrosim, and install Pybullet according to the instructions at https://www.reddit.com/r/ludobots/wiki/installation/.

  *NOTE: EARLIER VERSIONS OF PYTHON MAY NOT WORK.
  
Then, change drive (in Terminal) to the correct folder where the downloaded repository files are stored, and execute the command "python3 search.py" to run the simulation.
