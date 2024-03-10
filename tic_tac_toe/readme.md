[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/ZgPGTv83)
# Overview 
> Tic-Tac-Toe Game Refactoring

**NOTE:** You may be asked by your lecturer to submit this assessment via GitHub classrooms. Please check closer to submission date.

## Objective

Refactor a given monolithic tic-tac-toe game, such that the code:

1. Is modular, consisting of at least two files that logically group related functions.
2. Implements an appropriate Python project folder structure.
3. Includes at least one test case.
4. Employs a 2D data structure.

In the process, you must use at least four functions, two classes, two files, and one import statement of your modules (not including imports used in the test case).

## Instructions

### Step 1: Review the Existing Code

Firstly, analyze the given tic-tac-toe game code. Understand the flow and functionality before proceeding with the refactoring.

### Step 2: Identify Components to Refactor

Identify the parts of the code that can be improved. Determine which parts of the code can be grouped logically into separate modules.

### Step 3: Modularizing the Code

Refactor the code to create at least two files. These files should contain logically grouped functions and classes. Ensure the file names are appropriate for the division you have chosen.

### Step 4: Create a Modern Python Folder Structure

The refactored code should adhere to the following modern Python folder structure:

```bash
tic_tac_toe/
|--- src/
|    |--- __init__.py
|    |--- module1.py
|    |--- module2.py
|--- tests/
|    |--- __init__.py
|    |--- test_tic_tac_toe.py
|--- setup.py
```

**Note**: 

- `__init__.py` files are used to indicate that a directory should be treated as a Python package. This allows the files within to be imported as a module in the test scripts or other python files.
- `setup.py` is a Python file used to specify what modules and dependencies must be installed. I will provide this file, along with instructions on how to install your modules using this file.
- You must give your Python files appropriate names. Do **not** use module1, 2, etc.
  
### Step 5: Create a Test Case

Develop at least one test case for your refactored code. The test case should reside in the 'tests' directory. 

### Step 6: Implement 2D Data Structure

Refactor the code such that it employs a 2D data structure for the tic-tac-toe game board.

### Step 7: Written Report

Once you have completed your refactoring, write a brief report addressing the following:

1. Justification for your refactoring decisions.
The reason I decided to split the board and the game into 2 files was so that it would be easier to call the board as a class rather than having it has it's own print command that printed the whole board over 4-5 lines. With this I got rid of the loop feature that was in the previous version and instead opted for having some of the features be there own statement meanig I could call them when required.

2. The challenges you would have faced maintaining and testing the original monolithic code.
without refactoring the code it would've been hard to debug this code and isolate specfific components as it makes finding the source of the error more challenging. Not to mention it's a lot more lengthy.
3. How you would modify your refactored code to handle a custom-sized tic-tac-toe game (larger than 3x3), and how this implementation would be easier to handle than in the original code.
I would have to modify the board aspect of the game and just add more print options to the current 'print board' function, but this mean I would have to refactor the possible win solutions given that it would be a lot more.

### Step 8: Short Answer (Knowledge Questions)

Provide brief answers to the knowledge-question worksheet.

1. Briefly explain: what is modular programming
Modular programming involves the act of dividing the usefullness of a program into free and exchangable modules
2. How can you import only a specific function or class from a module in Python? What is the syntax for this?
import
3. How would you explain Python's parameter-passing mechanism? Is it more similar to pass-by-value or pass-by-reference? Justify your answer.
It depends on what type of object you are passing through certain objects that are mutable display pass by reference whereas objects that are immutable show pass by value. 
4. Given the following Python code, what will be the output and why?
It display 'orignal' and 'new' and removes 'completly' this is because of 'completely' was assigned to the list and wasn't added in by a function this causes it to be removed.

    ```python
    def modify_list(list_):
        list_.append("new")
        list_ = ["completely", "new"]

    items = ["original"]
    modify_list(items)
    print(items)
    ```

5. In Python even though variables created within a function are local, there are still situations where you can modify data outside the scope with a local variable. Explain this anomaly and relate it to both mutability and pass by reference.
Variables produced inside a function are local by default, however because of the nature of pass by object reference and the mutability of the related objects, changes made to mutable objects sent into a function might influence data outside the function.


6. List two benefits of modular coding approaches. How do these benefits assist in the development of medium-sized applications?
When dealing wiht medium sized application having code that is easier to tests proves more beneficial as you can break down certain funcitons and test smaller functions compared to a big function that do multiple things. And it's easier to find certain functions and where they are located in modular coding due to it being broken down into smaller parts. 

### Submission

Please submit the refactored code, your test case, and the written report.

### Evaluation Criteria

Your refactoring will be evaluated on the clarity and modularity of your code, as well as the thoughtful reasoning behind your design decisions. Your test case should be robust and cover key aspects of the tic-tac-toe game functionality. The written report should accurately reflect your understanding of code refactoring, testing, and the flexibility of your new implementation.
