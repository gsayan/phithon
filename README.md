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
- The program uses imports numpy as `np`
- All the names from `numpy` and `numpy.linalg` are imported unless there is a name clash with the modulesimported before. In that case, one can call the function as `np.[function name]`
- `numpy.linalg` is imported as `lin`.
### Solving linear equations
1. Type `linE` and `Enter`
2. If your equations are
a1x1 + b1x2 = c1
a2x2 + b2x2 = c2
With x1, x2 variables, the input should be
```python
<linE/i> Enter the coefficients: a1/b1/c1//a2/b2/c2
```
- The output will be shown and will be stored as an array `solutionsdata`
- Use `quit` to come out of Linear Equations section
### Solving quadratic equations
1. Type 'quadE' and 'Enter'
2. If your equation is
ax^2 + bx + c = 0
The input should be
```python
<quadE/i> Enter the coefficients: a/b/c
```
- The output will be shown and stored as `solution1` and `solution2` respectively.
### 2D plot
Type `plt` followed by command to use `matplotlib.pylab` efficiently. Use `&` for more than one command. As example, the following sets of commands are recognized identically.
```python
<calc/i> plot(x,y) & title("Graph") & show()
```
```python
<calc/i> plot(x,y)
<calc/i> title("Graph")
<calc/i> show()
```
### Solving ODE
To solve ordinary differential equation of degree 1, the command is `ODE1` followed by the algorithm followed by `dydx` followed by `~` and initial conditions, and then `@` followed by step size and desired range of solution. For example,the command
```python
<calc/i> ODE1 mEul dydx sin(x)+cos(x**2-pi/2) ~ 0 , 1 @ 0.01 , -1 , 3
```
is for solving dydx = sin(x)+cos(x^2-pi/2), with y(0) = 1, step size = 0.1 in the range (-1,3) in modified Euler method
The solution data is stored as variables `xsols` and `ysols`
Use `&` followed by a special statement to plot, show or export
Methods:
- `sEul` for standard Euler's method
- `mEul` for modified Euler's method
- `RK4` for 4th order Runge-Kutta method
Special statements:
- 'show` for printing the solutions as a table
- `plot` for plotting the solution
- `expt("[file name or location]")` to export the data
### Running loops
TO run loops, like for, while etc, write your command line by line and end with a `;`. An example:
```python
<calc/i> for i in range(8):
...>    j = 3+sin(i*pi/2)
...>    print(j);
```
## Special operations
This application is expected to support some special operations as well. For now,it supports only Zn group operations.
### The modulo group
To start using a modulo group, for example Z7, write out the following command
```python
<calc/i> load group z_7
```
This creates a class, `z7` that turns an integer into its modulo 7 integer, with appropriate operations `+`, `-`, `*`. Applicability of `/` depends on the group.
Use `a.intg` to see the integer associated with `a`.
