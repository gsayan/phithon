print("Type 'quit' to exit\nType 'help' for help")

import os
import importlib as imp
from colorama import init, Fore
init(convert=True)
import numpy as np
import numpy.linalg as lin
print(Fore.YELLOW+"numpy functions are ready to use"+Fore.WHITE)
import matplotlib.pylab as plt
print(Fore.YELLOW+"pyplot imported as plt"+Fore.WHITE)


pltdir = dir(plt)
for i in pltdir:
    if len(i) < 3:
        exec(i+" = plt."+i)
        del pltdir[pltdir.index(i)]

npdir = dir(np)
for i in npdir:
    if len(i) < 4:
        exec(i+" = np."+i)
        del npdir[npdir.index(i)]

lindir = dir(lin)
for i in lindir:
    if len(i) < 4:
        exec(i+" = lin."+i)
        del lindir[lindir.index(i)]

usens = True

inp = None

exc = "quit"

while inp != exc:
    inp = str(input("<calc/i> "))
#    for exprs in npdir2:
#        inp = inp.replace(exprs, "npe."+exprs)
    if usens == True:
        for exprs in npdir:
            if "np."+exprs in inp:
                pass
            else:
                inp = inp.replace(exprs, "np."+exprs)
        for exprs in lindir:
            if "lin."+exprs in inp:
                pass
            else:
                inp = inp.replace(exprs, "lin."+exprs)
    else:
        pass
    divs = inp.split(" ")
    if inp == "help":
        print("Enter 'quit' to close\n\
Use 'p' to execute a code and print the output\n\
Use 'np ' to execute a code using numpy\n\
Enter 'Help <module name>' for help regarding that module")
        iinp = None
        while iinp != exc:
            iinp = str(input("<Help> "))
            if iinp == "numpy":
                print("To use a function from numpy library use /<function name>\nTo see list of numpy functions hit 'nplib' or execute directly the help menu for numpy")
            elif iinp == "nplib":
                exec("help(np)")
            elif iinp == "E":
                print("Enter 'E <command> to execute")
            elif iinp == "Exit":
                pass
            elif iinp == "ODE":
                print("Enter ODE<order> to continue to ODEs. For example enter 'ODE1' will take you into 1st order differential equations.\n\
Then enter the algorithm you want to use.\n\
Euler\t\t-->\tEuler's Algorithm\n\
mEuler\t\t-->\tModified Euler's Algorithm\n\
rk4\t\t-->\t4th order Runge Kutta Algorithm\n\
mdp\t\t-->\tMidpoint method")
            elif iinp == "LinE":
                print("If the equations are\n\
a1*x1 + b1*x2 + c1*x3 = p1\n\
a2*x1 + b2*x2 + c2*x3 = p2\n\
a3*x1 + b3*x2 + c3*x3 = p3\n\
Write the inputs as\n\
a1,b1,ci,p1\n\
a2,b2,c2,p2\n\
a3,b3,c3,p3")
            else:
                print("Sorry, help isn't available for this :(")
    elif divs[0] == "p":
        Divs = inp.replace("p ","print('<calc/o>',")
        Divs = Divs + ")"
        try:
            exec(Divs)
        except:
            print("Invalid command: ",Divs)
    elif inp == "plot":
        print(Fore.YELLOW+"You are using pyplot section now\n"+Fore.WHITE)
        print("Pyplot functions are usable")
        iinp = None
        while iinp != exc:
            iinp = str(input("<plot/i> "))
            divs = iinp.split("&")
            for i in divs:
                while i[0] == " ":
                    i = i[1:]
            for i in divs:
                while i[-1] == " ":
                    i = i.replace(i,i[:-1])
            for i in divs:
                for j in pltdir:
                    if j in i:
                        i = i.replace(j, "plt."+j)
                if i[0] == " ":
                    i = i[1:]
                else:
                    pass
                try:
                    exec(i)
                except:
                    print(Fore.RED+"Invalid command: "+i+Fore.WHITE)
        print(Fore.YELLOW+"You just left pyplot section"+Fore.WHITE)
    elif divs[0] == "plt":
        iinp = inp[3:]
        while inp[0] == " ":
            inp = inp[1:]
        divs = iinp.split("&")
        for i in divs:
            while i[0] == " ":
                i = i[1:]
        for i in divs:
            while i[-1] == " ":
                i = i.replace(i,i[:-1])
        for i in divs:
            for j in pltdir:
                if j in i:
                    i = i.replace(j, "plt."+j)
            if i[0] == " ":
                i = i[1:]
            else:
                pass
            try:
                exec(i)
            except:
                print(Fore.RED+"Invalid command: "+i+Fore.WHITE)
    elif inp == "linE":
        print(Fore.YELLOW+"You are now in linear equation section"+Fore.WHITE)
        iinp = None
        while iinp != exc:
            iinp = str(input("<linE/i> Enter the coefficients: "))
            try:
                rows = iinp.split("//")
                mtx = []
                for i in rows:
                    i = str(i)
                    i = i.split("/")
                    for j in i:
                        j = float(j)
                    mtx.append(i)
                iinp = np.array(mtx).astype("complex")
                mat = iinp[:,:-1]
                col = iinp[:,-1]
                try:
                    invr = lin.inv(mat)
                    sols = np.dot(invr,col)
                    print("<linE/o> Solutions:\n\t",list(sols))
                except:
                    print(Fore.RED+"The equations are not solvable"+Fore.WHITE)
            except:
                if iinp == exc:
                    pass
                else:
                    print(Fore.RED+"Invalid command: "+iinp+Fore.WHITE)
        print(Fore.YELLOW+"You just left linE section"+Fore.WHITE)
    elif inp == "quadE":
        print(Fore.YELLOW+"You are now in quadratic equation section"+Fore.WHITE)
        iinp = None
        while iinp != exc:
            try:
                iinp = str(input("<quadE/i> Enter the coefficients: "))
                [a, b, c] = [complex(i) for i in iinp.split("/")]
                s1 = (-b + np.sqrt(b**2 - 4*a*c))/(2*a)
                s2 = (-b + np.sqrt(b**2 - 4*a*c))/(2*a)
                print("<quadE/o> Solutions:")
                print("\t",s1,s2)
            except:
                if iinp == exc:
                    pass
                else:
                    print(Fore.RED+"Invalid command: "+iinp+Fore.WHITE)
        print(Fore.YELLOW+"You just left quadE section"+Fore.WHITE)
    else:
        try:
            exec(inp)
        except:
            print(Fore.RED+"Invalid command: "+inp+Fore.WHITE)
    
