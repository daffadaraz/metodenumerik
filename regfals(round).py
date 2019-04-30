import os
from myfunc import clear

def f(x): #Atur sesuai dengan persamaan mu
    return (pow(x,3) + (2 * pow(x,2)) - (4*x) - 4)

def main():
    #var
    check = 1
    n = 0

    clear ()

    print("Regula Falsi")
    print("Persamaan, F(x) = x^3 + 2x^2 - 4x -4") #Jangan lupa edit
    print("")
    print("(Berapa angka dibelakang koma)")
    rou = int(input("Pembulatan : "))
    err = float(input("Masukkan Error : "))

    while check > 0: #Menentukan X1 dan X2
    	print("")
    	x1 = float(input("Masukkan X1 : "))
    	x2 = float(input("Masukkan X2 : "))
    	fx1 = round(f(x1),rou)
    	fx2 = round(f(x2),rou)
    	print("")
    	print("Nilai dari, F(%d) = %f " % (x1,f(x1)))
    	print("Nilai dari, F(%d) = %f " % (x2,f(x2)))
    	print("")
    	check = fx1*fx2
    	if check<0:
    		print("Syarat sudah ok. %d*%d < 0 >> %5.2f<0"%(fx1,fx2,check))
    		break
    	else :
    		print("Syarat belum ok f(%d)*f(%d) > 0 >> %5.2f>0"%(x1,x2,check))
    print()

    #Mempersiapkan output berupa tabel
    print("X1 = %d , X2 = %d , Error = %.2f"% (x1,x2,err))
    print("______________________________________________________")
    print("  n           x              f(x)             error   ")
    print("______________________________________________________")

    cekerr = err + 1;
    cektemp = cekerr + 1;
    while cekerr > err: #Iterasi / Pencarian Akar
        n = n + 1
        x3 = round(((x1 * f(x2) - x2 * f(x1)) / (f(x2) - f(x1))),rou)
        fx3 = round(f(x3),rou)
        cekerr = abs(fx3)

        #OUTPUT
        print("%3d|     %.8f      %10.8f      %12.10f" % (n,x3,fx3,cekerr))
        if cekerr <= err or cekerr == cektemp :
            print("________________")
            print("Akar Persamaan, %f"%(round(x3,rou)))
            print("Error, %.4f"%(round(cekerr,4)))
            break

        if fx1 * fx3 > 0:
            x1 = x3
        else :
            x2 = x3
            
        cektemp = cekerr
        if n%10 == 0:
            input("Lanjut? Tekan enter.")

if __name__ == '__main__':
    main()

# Metode Regula Falsi yang digunakan
# 1. Ambil dua titik sembarang  x1  dan   x2
# 2. Hitung nilai f(x1)  dan  f(x2)
# 3. Tentukan hasil kali tanda bilangan  f(x1) . f(x2)
#    Bila  f(x1).f(x2)  > 0 , ganti titik x1 dan x2 . Bila  f(x1).f(x2)  < 0  ( berlawanan tanda )
# 4. Hitung nilai  xx3 = ((fx1 * x2) - (fx2 * x1)) / (fx1 - fx2)
# 5. Hitung nilai  f(x3)
#    Bila nilai f(x3) mendekati nol , maka x3 adalah akar persamaan . Selesai . Bila tidak,
# 6. Tentukan hasil kali tanda bilangan  f(x1).f(x3)
#    Bila tanda bilangan f(x1).f(x3)  >  0 , maka  x1  =  x3  ( nilai x1 menjadi  x3 )
#    Bila tanda bilangan  f(x1).f(x3)  <  0 , maka  x2  =  x3 ( nilai x2 menjadi  x3 )
# 7. Kembali ke langkah 4.
