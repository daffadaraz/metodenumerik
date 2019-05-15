import os
from sympy import Symbol, Derivative

# ClearScreen
def clear():
    if os.name == "nt":
        os.system('cls')
        pass
    else:
        os.system('clear')

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

def persamaana(pers):
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
    function = pers
    deriv= Derivative(function, x)
    return str(deriv.doit())
