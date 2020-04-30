print("Type 'quit' or 'exit' to exit")

import os
import importlib as imp
from colorama import init, Fore
from builtins import *
init(convert=True)
iniglobal = tuple(globals())
import numpy as np
for i in dir(np):
    if i in iniglobal:
        pass
    else:
        exec("from numpy import "+i)
print(Fore.YELLOW+"numpy functions are ready to use"+Fore.WHITE)
initialglobal = globals()
import numpy.linalg as lin
for i in dir(lin):
    if i in initialglobal:
        pass
    else:
        exec("from numpy.linalg import "+i)
initialglobal = globals()
print(Fore.YELLOW+"numpy.linalg functions are ready to use"+Fore.WHITE)
import matplotlib.pylab as plt
for i in dir(plt):
    if i in initialglobal:
        pass
    else:
        exec("from matplotlib.pylab import "+i)
print(Fore.YELLOW+"matplotlib.pylab functions are ready to use"+Fore.WHITE)
#from intg import riems, trapiz, simp13
initialglobal = tuple(globals())

warn = True
ode1warn = True
linEwarn = True

inp = ""

exc = ["quit", "exit"]
yeps = ["yes", "Yes", "Y", "y"]
nopes = ["no", "No", "N", "n"]
initialglobals = globals()

while inp not in exc:
    inp = str(input("<calc/i> "))
    divs = inp.split(" ")
    if inp in exc:
        pass
    elif divs[0] == "p":
        Divs = inp.replace("p ","print('<calc/o>',")
        Divs = Divs + ")"
        try:
            exec(Divs)
        except:
            print(Fore.Red+"\aInvalid command: ",Divs+Fore.WHITE)
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
                i = i[:-1]
            if i[0] == " ":
                i = i[1:]
            else:
                pass
            icode = compile(i,"str", "exec")
            try:
                exec(icode)
            except:
                print(Fore.RED+"\aInvalid command: "+i+Fore.WHITE)
    elif inp == "linE":
        print(Fore.YELLOW+"You are now in linear equation section"+Fore.WHITE)
        if warn == True:
            if linEwarn == True:
                print(Fore.LIGHTRED_EX+"\aThis section will use names 'rowsofdata', 'matrixofdata', 'matrxoperator', 'columnofdata', 'inverseofoperator' and 'solutionsdata'. You will not see this warning again."+Fore.WHITE)
                linEwarn = False
            else:
                pass
        else:
            pass
        iinp = ""
        while iinp not in exc:
            iinp = str(input("<linE/i> Enter the coefficients: "))
            if iinp in exc:
                pass
            else:
                try:
                    rowsofdata = iinp.split("//")
                    matrixofdata = []
                    for i in rowsofdata:
                        i = str(i)
                        i = i.split("/")
                        for j in i:
                            j = float(j)
                        matrixofdata.append(i)
                    iinp = np.array(matrixofdata).astype("complex")
                    matrixoperator = iinp[:,:-1]
                    columnofdata = iinp[:,-1]
                    try:
                        invrseofoperator = lin.inv(matrixoperator)
                        solutionsdata = np.dot(invrseofoperator,columnofdata)
                        print("<linE/o> Solutions:\n\t",list(solutionsdata))
                    except:
                        print(Fore.RED+"\aThe equations are not solvable"+Fore.WHITE)
                except:
                    if iinp in exc:
                        pass
                    else:
                        print(Fore.RED+"\aInvalid command: "+iinp+Fore.WHITE)
        print(Fore.YELLOW+"You just left linE section"+Fore.WHITE)
    elif inp == "quadE":
        print(Fore.YELLOW+"You are now in quadratic equation section"+Fore.WHITE)
        if warn == True:
            if quadEwarn == True:
                print(Fore.LIGHTRED_EX+"This section uses names 'iinp', 'asolution', 'bsolution', 'csolution', 'solution1' and 'solution2'. You will not see this warning again."+Fore.WHITE)
                quadEwarn = False
            else:
                pass
        else:
            pass
        iinp = ""
        while iinp not in exc:
            try:
                iinp = str(input("<quadE/i> Enter the coefficients: "))
                [asolution, bsolution, csolution] = [complex(i) for i in iinp.split("/")]
                solution1 = (-bsolution + np.sqrt(bsolution**2 - 4*asolution*csolution))/(2*asolution)
                solution2 = (-bsolution + np.sqrt(bsolution**2 - 4*asolution*csolution))/(2*asolution)
                print("<quadE/o> Solutions:")
                print("\t",solution1,solution2)
            except:
                if iinp in exc:
                    pass
                else:
                    print(Fore.RED+"Invalid command: "+iinp+Fore.WHITE)
        print(Fore.YELLOW+"You just left quadE section"+Fore.WHITE)
    elif inp[-1] == ":":
        yourcommand = [inp]
        iinp = " "
        while iinp[-1] != ";":
            iinp = str(input("...> "))
            yourcommand.append(iinp)
        yourcommand[-1] = yourcommand[-1][:-1]
        allcommands = "\n".join(yourcommand)
        yourcode = compile(allcommands,"str","exec")
        try:
            exec(yourcode)
        except:
            print(Fore.RED+"Invalid command: "+allcom+Fore.WHITE)
            pass
    elif divs[0] == "ODE1":
        namesinode1 = ['namesinode1', 'namesstring','proceed', 'restofit', 'algorithm', 'firststring', 'func', 'funcod', 'initialconditions', 'additionals', 'otherjobs', 'rng', 'outputfilename', 'toplot', 'toshow', 'initialscopy', 'funv', 'algorithmvalue', 'fun', 'p', 'c', 'endsat', 'h', 'xvar0', 'yvar0', 'r', 's', 'xlist', 'ylist', 'xylist', 'xval', 'yval', 'xsols', 'ysols', 'xysols', 'outfile']
        namesstring = " ,".join(namesinode1)
        if warn == True:
            if ode1warn == True:
                print(Fore.MAGENTA+"The names"+namesstring+" will be used\nYou will not see this warning again"+Fore.WHITE)
                iinp = str(input("Do you wish to continue? (y/n) "))
                ode1warn = False
                if iinp in yeps:
                    proceed = True
                else:
                    proceed = False
            else:
                proceed = True
        else:
            proceed = True
        if proceed == True:
            restofit = " ".join(divs[1:])
            algorithm = divs[1]
            firststring = restofit.split("dydx")[1]
            yourfunction = firststring.split("~")[0]
            restofit = firststring.split("~")[1]
            initialconditions = restofit.split("@")[0]
            restofit = restofit.split("@")[1]
            if "&" in restofit:
                additionals = restofit.split("&")[0]
                otherjobs = restofit.split("&")[1:]
                otherjobs = " ".join(otherjobs)
            else:
                additionals = restofit
                otherjobs = ""
            if "expt" in otherjobs:
                outputfilename = otherjobs.split("expt(")[1].split(")")[0]
            else:
                outputfilename = ""
            toplot = "plot" in otherjobs
            toshow = "show" in otherjobs
            initialscopy = initialconditions.split(",")
            exec("xvar0 = "+initialscopy[0])
            exec("yvar0 = "+initialscopy[1])
            additionalscopy = additionals.split(",")
            if len(additionalscopy) > 2:
                exec("startsfrom = "+additionalscopy[1])
                exec("endsat = "+additionalscopy[2])
            else:
                startsfrom = xvar0
                exec("endsat = "+additionalscopy[1])
            exec("stepsize = "+additionalscopy[0])
            funv = 1
            algorithmvalue = 1
            funcod = compile("def fun(x,y):\n\treturn "+yourfunction,"str","exec")
            try:
                exec(funcod)
            except:
                print(Fore.RED+"Invalid function: "+yourfunction+Fore.WHITE)
                funv = 0
        if funv == 1:
            if algorithm == "mEul":
                def update(x,y,h):
                    p = y
                    c = y
                    p += h*fun(x,y)
                    c += h/2*(fun(x,y)+fun(x+h,p))
                    return x+h,c
            elif algorithm == "sEul":
                def update(x,y,h):
                    x += h
                    y += h*fun(x,y)
                    return x,y
            elif algorithm == "RK4":
                def update(x,y,h):
                    p = h*fun(x,y)
                    q = h*fun(x+h/2,y+p/2)
                    r = h*fun(x+h/2,y+q/2)
                    s = h*fun(x+h,y+r)
                    x += h
                    y += (p+2*q+2*r+s)/6
                    return x,y
            else:
                print(Fore.RED+"Unknown algorithm"+Fore.WHITE)
                algorithmvalue = 0
            if algorithmvalue == 1:
                if startsfrom == xvar0:
                    def desoln():
                        x = xvar0
                        y = yvar0
                        xlist = [xvar0]
                        ylist = [yvar0]
                        xylist = [[xvar0,yvar0]]
                        while x < endsat:
                            x,y = update(x,y,stepsize)
                            xlist.append(x)
                            ylist.append(y)
                            xylist.append([x,y])
                        xval = np.array(xlist)
                        yval = np.array(ylist)
                        return xval,yval,xylist
                else:
                    def desoln():
                        x = xvar0
                        y = yvar0
                        xlist = [xvar0]
                        ylist = [yvar0]
                        xylist = [[xvar0,yvar0]]
                        while x > startsfrom:
                            x,y = update(x,y,-stepsize)
                            xlist.append(x)
                            ylist.append(y)
                            xylist.append([x,y])
                        xlist = xlist[::-1]
                        ylist = ylist[::-1]
                        xylist = xylist[::-1]
                        x = xvar0
                        y = yvar0
                        while x < endsat:
                            x,y = update(x,y,stepsize)
                            xlist.append(x)
                            ylist.append(y)
                            xylist.append([x,y])
                        xval = np.array(xlist)
                        yval = np.array(ylist)
                        return xval,yval,xylist
                xsols, ysols, xysols = desoln()
                if (toplot, toshow) == (False, False):
                    print("<calc/o> Solutions ready")
                else:
                    if toplot == True:
                        plt.plot(xsols,ysols)
                        plt.title("Solution for\ndy/dx = "+yourfunction)
                        plt.show()
                    else:
                        pass
                    if toshow == True:
                        print("<calc/o>\tx\t\t\t\ty")
                        for i in xysols:
                            print("<calc/o>\t"+str(i[0])+"\t\t\t\t"+str(i[1]))
                    else:
                        pass
                if outputfilename != "":
                    try:
                        outfile = open(outputfilename,"w+")
                        for i in xysols:
                            outfile.write(str(i[0])+"\t\t\t"+str(i[1])+"\n")
                        outfile.close()
                        del outfile
                        print("<calc/o> Solutions data exported")
                    except:
                        print(Fore.RED+"Cannot read file name. Please restart."+Fore.WHITE)
                else:
                    pass
            else:
                pass
        else:
            pass
    elif divs[0] == "load":
        try:
            if divs[1] == "group":
                if "z_" in divs[2]:
                    try:
                        if divs[2].split("z_")[-1].isdigit() == True:
                            num = int(divs[2].split("z_")[-1])
                            codelines = "\
class z"+str(num)+":\n\
    def __init__(self, intg):\n\
        self.intg = int(intg)%"+str(num)+"\n\
    def __add__(self, another):\n\
        return z"+str(num)+"((self.intg+another.intg)%"+str(num)+")\n\
    def __mul__(self, another):\n\
        return z"+str(num)+"((self.intg*another.intg)%"+str(num)+")\n\
    def __sub__(self, another):\n\
        return z"+str(num)+"((self.intg-another.intg)%"+str(num)+")\n\
    def __truediv__(self, another):\n\
        a = another.intg\n\
        b = a\n\
        while (a*b)%"+str(num)+" != 1:\n\
            b += 1\n\
        return z"+str(num)+"((self.intg*b)%"+str(num)+")\n\
z"+str(num)+"0 = z"+str(num)+"(0)\n\
z"+str(num)+"1 = z"+str(num)+"(1)"
                            cod = compile(codelines, "str", "exec")
                            exec(cod)
                        else:
                            print(Fore.RED+"Invalid expression. Please enter z_n to define a modulo n group"+Fore.WHITE)
                    except:
                        print(Fore.RED+"Invalid command: "+inp+Fore.WHITE)
                else:
                    print("This is unsupported")
                    print("bbbb")
                    pass
            else:
                print("This is unsupported")
                print("aaaa")
                pass
        except:
            print(Fore.RED+"Invalid command: "+inp+Fore.WHITE)
    else:
        cod = compile(inp,"str","exec")
        try:
            exec(cod)
        except:
            print(Fore.RED+"Invalid command: "+inp+Fore.WHITE)
