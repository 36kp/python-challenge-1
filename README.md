# Variety Food Truck

## About
This program is developed to demonstrate my learnings as a part of AI Boot-camp by University of Pennsylvania, Liberal and Professional Studies. [More Info...](https://bootcamp.sas.upenn.edu/artificial-intelligence/landing/)
<br/><br/>
This program puts the topics discussed in **Programming for AI : Part 1** into action

## Topics covered in this program
1. Data structures
    1. Dictionary
    2. List
2. Loops
    1. `for` loop
    2. `while` loop
3. Conditional statements
    1. `if` conditions
    2. `match`-`case` conditions
4. Data manipulation
    1. String manipulations
    2. Type conversions
    3. List and dictionary traversal
    4. List comprehension
5. User Interface
    1. Command line interface
    2. Structured output
    3. Input valudations
    4. User error handling

## How to run this program
Follow instructions below to run this program
> NOTE: Following setup and commands are tested in macOS Sonoma 14.5 only

### Pre-requisites
- Dev environment setup using [Anaconda](https://www.anaconda.com/download).
- Make sure that following commands are recognized
    - `python --version`
    - `git --version`

## Usage
- Checkout git repository using git clone
`git clone https://github.com/36kp/python-challenge-1.git`
- Go to the repo home directory
`cd \YOUR_PATH\python-challenge-1`
- Execute the program
`python menu.py`
- Follow on-screen instructions :-)

> NOTE: This program is designed to exit after one order. However, it can be configured in code to work for multiple orders in a loop by removing/commenting out following lines:
```
        # Complete order and exit. Remove this break to keep program running
        # for multiple customers
        break
```