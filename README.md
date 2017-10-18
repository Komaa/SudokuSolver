# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: In order to solve the naked twins problem we apply a constrain to the values of the peers in the same unit as the
twins. Since these value are already assign to one of the twin, they cannot be assigned to the peers in the same unit,
so we remove these value from the peers. In the general case, this is a permutation problem: if we can find a unit with
a permutation that is restricted to the same number of boxes, then we can apply a filter rule that generalize the naked
twins strategy. So, it is possible to optimise also "dressed" twins, trios ("dressed" or naked) and so on. I did not
implement it for lack of time, I will try to do so in the following days.


# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: In order to solve the diagonal sudoku problem we add the constrain that every element on the two principal diagonals
of the sudoku must be unique. In order to do so, we add the diagonal units to the row, column and square units and we
use them to apply the elimination and only choice strategies accordingly to the diagonal sudoku problem.

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solution.py` - Fill in the required functions in this file to complete the project.
* `test_solution.py` - You can test your solution by running `python -m unittest`.
* `PySudoku.py` - This is code for visualizing your solution.
* `visualize.py` - This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the `assign_value` function provided in solution.py

### Submission
Before submitting your solution to a reviewer, you are required to submit your project to Udacity's Project Assistant, which will provide some initial feedback.  

The setup is simple.  If you have not installed the client tool already, then you may do so with the command `pip install udacity-pa`.  

To submit your code to the project assistant, run `udacity submit` from within the top-level directory of this project.  You will be prompted for a username and password.  If you login using google or facebook, visit [this link](https://project-assistant.udacity.com/auth_tokens/jwt_login) for alternate login instructions.

This process will create a zipfile in your top-level directory named sudoku-<id>.zip.  This is the file that you should submit to the Udacity reviews system.

