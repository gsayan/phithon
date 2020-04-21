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
WARNING: The app uses namespaces of `numpy`, `numpy.linalg` and `matplotlib.pylab` for normal code execution. For easy use it substitutes function names. For example, using `sin` in the console by default will use `numpy.sin` to calculate. Also an user defined function, say `sine` will get transformed into `numpy.sine` which is not a valid function and the code will not run. To avoid it, set
```python
usens = False
```

