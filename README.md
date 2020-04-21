# phithon
A console calculator app built with python

## Features
* Solving problems is easy
* Less lines of code
* Easy for exporting data or plots

## Installation
The program is built and tested in Python3 environment and uses numpy and matplotlib packages. Further modifications of the program may include SciPy, SymPy and similar packages. Run The `main.py` file using python to start using the calculator.

## Scopes
The calculator allows to perform calculations with less lines of codes. Using it one can calculate
- Use python shell for usual code execution, including storing data, using user defined functions, etc.
- Use numpy and matplotlib with less lines of codes
- Solve linear and quadratic equations

## Using the calculator
- The console lets you execute a code like defining a variable, defining functions, etc. just like in normal python console.
### Using numpy
- The program imports numpy by default as `np`. But the app has a variable `usens` (short for use namespace) set as `True` by default. Each input is modified to fit for the existing numpy function. An input `cosh(1)` will be seen as `np.cosh(1)`.
- Users are advised to avoid using variable or function names that resemble numpy function names. A user defined variable, for example, `acosh` will be read as `anp.cosh` and the code will not run.
 - Why this wierd design? Primarily to use namespaces of other libraries and user defined functions / variables flexibly.
- Users have an option to turn off this auto manipulation of code by setting
```python
usens = False
```
- Then one can use numpy library as np and codes will not be modified.
- Numpy functions and variables that have up to 3-letter names are imported as they are.
- `numpy.linalg` is imported as `lin` in the same fashion as `numpy`. Set `usens = False` to stop modifying inputs.
- Some of the functions overlap for numpy and linalg. Linalg functions are overwritten by numpy functions.
### Solving linear equations
1. Type `linE` and `Enter`
2. If your equations are
a1x1 + b1x2 = c1
a2x2 + b2x2 = c2
With x1, x2 variables, the input should be
```python
<linE/i> Enter the coefficients: a1/b1/c1//a2/b2/c2
```
- The output will be shown and will be stored as an array `sols`
- Use `quit` to come out of Linear Equations section
### Solving quadratic equations
1. Type 'quadE' and 'Enter'
2. If your equation is
ax^2 + bx + c = 0
The input should be
```python
<quadE/i> Enter the coefficients: a/b/c
```
- The output will be shown and stored as `s1` and `s2` respectively.
WARNING: `a`,`b` and `c` are used to define variables in this process. Please do not name other variables as `a`, `b` or `c` for they will be modified every time a quadratic equation is solved.
### 2D plot
- Type `plot` to get into the plot section. Input will be changed to match matplotlib functions. Use `&` for more than one command. As example, the following sets of commands are recognized identically.
```python
<plot> plot(x,y) & title("Graph") & show()
```
```python
<plot/i> plot(x,y)
<plot/i> title("Graph")
<plot/i> show()
```
For using a plot for once, you may also use a command like the following
```python
<calc/i> plt plot(x,y) & show()
