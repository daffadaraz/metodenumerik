import os, random
from scripts.myfunc import clear
import scripts.MBisection as MB
import scripts.RegulaFalsi as RF
import scripts.NewtonRaphson as NR

#--------------------------------------------------------------------------------------------------#
#Main Menu dan Pemanggilan fungsi fungsi
#--------------------------------------------------------------------------------------------------#
def method(p):
    pil = 4
    print("Metode yang ingin di gunakan?")
    print("1. Metode Bisection")
    print("2. Regula Falsi")
    print("3. Newton Raphson")
    pil = int(input("Masukkan Pilihan : "))

    if(pil == 1):
        MB.hitung(pers)
    elif(pil == 2):
        RF.hitung(pers)
    elif(pil == 3):
        NR.hitung(pers)
    else:
        print("Wrong Input.")
        exit()

    return 0

#--------------------------------------------------------------------------------------------------#
# Input persamaan dan perulangan.
#--------------------------------------------------------------------------------------------------#
if __name__ == '__main__':
    clear()
    #Initialisasi Variable
    pil2 = 'y'
    pil3 = 'n'
    while(pil2 == 'y' or pil2 == 'Y'):
        if (pil3 == 'n' or pil3 == 'N'):
            print("ex. x^3 + 2*x^2 - 4*x - 4")
            pers = str(input("Masukkan Persamaan : "))
        print()

        #Pemilihan Metode Numerik
        method(pers)

        print()
        pil2 = input("Ulang ? (y/n) : ")
        if (pil2 =='y' or pil2 == 'Y'):
        	pil3 = input("Ulang dengan Persamaan yang sama ? (y/n) : ")
        	clear()
        else:
            exit()
            
