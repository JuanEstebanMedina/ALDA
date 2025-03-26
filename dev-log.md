# Code Journal

## Introduction
This document serves as a detailed record of every step taken during the project. It includes descriptions of tasks, decisions made, and any issues encountered.
Every Python function should have its algorithmic complexity in time and space included as a comment. (It uses [Black](https://github.com/psf/black))

## Table of Contents
1. [Day 1](#day-1)
2. [Day 2](#day-2)
3. [Day 3](#day-3)
4. [Conclusion](#conclusion)

## Day 1
### Tasks Completed
- Task 1: Initialize the project.

The first thing I should do is verify that I have the correct `python` version
```sh
python --version  # Example output: Python 3.11.9
```

Install `virtualenv`
```sh
pip install virtualenv
```

Verify if `virtualenv` is correctly installed
```sh
python -m virtualenv --version  
# Example output: virtualenv 20.29.2
```

Create a virtual environment using `virtualenv`
```sh
python -m virtualenv env  # Creates "env" folder
```

Activate the virtual environment
```sh
.\env\Scripts\activate
```

Now, I can add all dependencies related to the project
```sh
pip install pandas black numpy matplotlib pytest coverage
```

Also, I had to install Anaconda and on the `Anaconda Prompt` use
```sh
conda install ipykernel
```

To format the code with the Black library, use
```sh
black .
```

#### *Here concludes the project structure creation*

## Day 2
### Tasks Completed
- Task 1: Generate random data module in Python and test it

First thing to do is create the files `generator.py` and `test_generator.py` in their respective subdirectories.

To follow the TDD methodology, it is important to create the respective test before the actual implementation.

Once the tests are completed, the next step is to implement the functionality and ensure that all tests pass.

- Task 2: Experimental analysis algorithm plots - 3 or more sorting algorithms.


To execute `sorting_experiments.py` use
```sh
python -m algorithm_analysis.experiments.sorting_experiments
```



### Decisions Made
- Decision 1: Description of the decision.
- Decision 2: Description of the decision.

### Issues Encountered
- Issue 1: Description of the issue.
- Issue 2: Description of the issue.

## Day 3
### Tasks Completed
- Task 1: Description of the task.
- Task 2: Description of the task.

### Decisions Made
- Decision 1: Description of the decision.
- Decision 2: Description of the decision.

### Issues Encountered
- Issue 1: Description of the issue.
- Issue 2: Description of the issue.

## Conclusion
Summary of the overall progress, key learnings, and next steps.