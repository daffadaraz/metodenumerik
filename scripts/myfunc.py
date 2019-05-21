import os
from sympy import Symbol, Derivative

# ClearScreen
def clear():
    if os.name == "nt":
        os.system('cls')
        pass
    else:
        os.system('clear')

# Error Message
def error():
    print('Usage : Main.py')
    print('        Main.py <"Persamaan"> ')
    print('ex.     Main.py "x^3 + 2*x^2 - 4*x - 4"')

#--------------------------------------------------------------------------------------------------#
#Menghitung Persamaan
#--------------------------------------------------------------------------------------------------#
def f(x,p):
    return (eval(p))

#--------------------------------------------------------------------------------------------------#
#Merubah bentuk persamaan
#--------------------------------------------------------------------------------------------------#
def persamaan(pers):
	n = 1
	while((pers.find("^")) == 1):
		n = n + 1
		pers = pers.replace("x^%d"%(n),"pow(x,%d)"%(n))
	return pers

def persamaana(pers): #Alternative
    n = 1
    while((pers.find("^")) == 1):
        n = n + 1
        q = n - 1
        pers = pers.replace("^%d"%(n),("*x"*q))
    return pers

#--------------------------------------------------------------------------------------------------#
#Menentukan Turunan persamaan
#--------------------------------------------------------------------------------------------------#
def turunan(pers):
    x= Symbol('x')
    deriv= Derivative(pers, x)
    return str(deriv.doit())
