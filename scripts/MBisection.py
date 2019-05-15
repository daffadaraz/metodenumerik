import os, random
from scripts.myfunc import clear,f,persamaan

#--------------------------------------------------------------------------------------------------#
# Fungsi main
#--------------------------------------------------------------------------------------------------#
def hitung(persp):
    #var
    n = 0
    p = persamaan(persp)

    clear ()

    #pil[0] berisi pilihan metode pil[1] berisi string metode
    print("Metode Numerik")
    print("Persamaan, %s"%(persp))
    print()
    print("(Berapa angka dibelakang koma. Masukkan 16 jika tidak yakin)")
    rou = int(input("Pembulatan : "))
    err = float(input("Masukkan Error : "))

    while True:
        print()
        x1 = float(input("Masukkan X1 : "))
        x2 = float(input("Masukkan X2 : "))
        fx1 = round(f(x1,p),rou)
        fx2 = round(f(x2,p),rou)
        print()
        print("Nilai dari, F(%d) = %f " % (x1,fx1))
        print("Nilai dari, F(%d) = %f " % (x2,fx2))
        print()
        check = fx1*fx2
        if check < 0:
        	print("Syarat sudah ok. f(%d)*f(%d) < 0 || %5.2f < 0"%(x1,x2,check))
        	break
        else:
        	print("Syarat belum ok f(%d)*f(%d) >= 0 || %5.2f >= 0"%(x1,x2,check))

    print()
    #Mempersiapkan output berupa tabel
    print("X1 = %d , X2 = %d , Error = %.6f"% (x1,x2,err))
    print("_______________________________________________________")
    print("  n           x              f(x)             error    ")
    print("_______________________________________________________")

    #Hanya untuk initialisasi
    cektemp = random.randint(1,100)

    while True:
        #Counter Iterasi
        n = n + 1

        x3 = round(((x1 + x2)/2),rou)

        fx3 = round(f(x3,p),rou)

        #Output Sesuai bentuk tabel
        print("%3d|     %.8f       %10.8f      %12.10f" % (n,x3,fx3,fx3))

        #Print Akar Persamaan
        if abs(fx3) <= err or abs(fx3) == cektemp :
        	print("________________")
        	print("Akar Persamaan, %.36f"%(x3))
        	print("Atau ~ %.4f"%(round(x3,4)))
        	print("Error, %.4f"%(round(fx3,4)))
        	print()
        	print("Note!")
        	print("Saat Melakukan perhitungan pastikan gunakan pembulatan")
        	print("agar mendapatkan jawaban yang sesuai dengan taraf error")
        	break

        if f(x1,p) * f(x3,p) > 0:
        	x1 = x3
        else :
        	x2 = x3

        cektemp = abs(fx3)

        #Agar memudahkan pembacaan iterasi. setiap 10 iterasi di stop.
        if n%10 == 0:
        	input("Lanjut? Tekan enter.")

#--------------------------------------------------------------------------------------------------#
## Metode Bisection yang digunakan
## 1. Ambil dua titik sembarang x1  dan  x2
## 2. Hitung nilai  f(x1)  dan  f(x2)
## 3. Tentukan hasil kali tanda bilangan f(x1).f(x2).
##     Bila f(x1).f(x2)  > 0 , ganti x1 dan x2   ,    Bila   f(x1).f(x2) < 0  (berlawanan tanda) ,
## 4.  Hitung    x3   =  ( x1 + x2 ) / 2
## 5. Hitung nilai  f(x3)
##     Bila f(x3)  mendekati nol  , maka  x3 adalah akar persamaan. Selesai.  Bila tidak
## 6. Tentukan hasil kali tanda bilangan  f(x1).f(x3)
##     Bila tanda bilangan   f(x1).f(x3)  >  0  maka  x1 =  x3  ( nilai x1 menjadi  x3 ).
##     Bila tanda bilangan   f(x1).f(x3)   <  0  maka  x2 =  x3  ( nilai x2 menjadi  x3 ).
## 7. Kembali ke langkah 4.
