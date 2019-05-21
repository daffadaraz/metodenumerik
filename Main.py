import os, random, sys
import scripts
from scripts import clear,error

#--------------------------------------------------------------------------------------------------#
#Main Menu dan Pemanggilan fungsi fungsi
#--------------------------------------------------------------------------------------------------#
def method(p):
    print("Persamaan, %s"%(pers))
    pil = 4
    print("Metode yang ingin di gunakan?")
    print("1. Metode Bisection")
    print("2. Regula Falsi")
    print("3. Newton Raphson")
    pil = int(input("Masukkan Pilihan : "))

    if(pil == 1):
        scripts.MB(pers)
    elif(pil == 2):
        scripts.RF(pers)
    elif(pil == 3):
        scripts.NR(pers)
    else:
        print("Wrong Input.")
        exit()

    return 0

#--------------------------------------------------------------------------------------------------#
# Input persamaan dan perulangan.
#--------------------------------------------------------------------------------------------------#
if __name__ == '__main__':
    #Inisialisasi Variable
    pil2 = 'y'

    if( (len(sys.argv)>2)): #Error Usage
        error()
        exit()

    elif(len(sys.argv)==2): #jika Menggnuakan Argument
        pil3 = 'y'
        pers = str(sys.argv[1])
        if((sys.argv[1].find('x')) == -1):
            error()
            print('\nNo Variable or using other than x')
            exit()

    else:
        pil3 = 'n'

    clear()
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
            