import os, random
from scripts.myfunc import clear,f,persamaana,persamaan,turunan

#--------------------------------------------------------------------------------------------------#
# Fungsi main
#--------------------------------------------------------------------------------------------------#

def hitung(persp):
    n = 1
    p = persamaana(persp)
    #2. Tentukan f '(x)
    trn = turunan(p)

    clear()
    print("Newton Raphson")
    print("Persamaan, %s"%(persp))
    print()
    print()
    print("(Berapa angka dibelakang koma. Masukkan 2 jika tidak yakin)")
    rou = int(input("Masukkan Pembulatan : "))
    print("(Ingin mendekati nilai berapa. Masukkan 0 jika tidak yakin)")
    err = float(input("Masukkan Error : "))

    #1. Ambil satu titik sembarang   x1
    print()
    x1 = float(input("Masukkan X1 : "))

    #3. Hitunglah nilai  f(x1)  dan  f '(x1)

    fx1 = f(x1,p)
    ftx1 = f(x1,trn)

    print()
    print("Nilai dari, F(%d)  = %f " % (x1,fx1))
    print("Nilai dari, F'(%d) = %f " % (x1,ftx1))
    print()

    print()
    #Mempersiapkan output berupa tabel
    print("x1 = %d ,  f(x1) = %f , f'(x1) = %f , Error = %.6f"% (x1,fx1,ftx1,err))
    print("______________________________________________________________________________")
    print("  n           f(x1)              f'(x1)              x2                f(x2)")
    print("______________________________________________________________________________")

    cektemp = random.randint(1,100)
    while True:

        #4. Tentukan nilai   x2   =   x1  -   f(x1) / f '(x1)
        x2 = round((x1 - fx1 / ftx1),rou)

        #5. Hitunglah nilai  f(x2) .
        fx2 = round(f(x2,p),rou+2)

        #Output Sesuai bentuk tabel
        print("%3d|     %.8f       %10.8f          %.8f          %.8f" % (n,fx1,ftx1,x2,fx2))

        #Bila nilai f(x2) mendekati 0 , x2 adalah akar persamaan , selesai.
        if fx2 == err or fx2 == cektemp or n == 10:
            print("________________")
            print("Akar Persamaan, %.36f"%(x2))
            print("Atau ~ %.4f"%(round(x2,4)))
            print("Error, %.4f"%(round(fx2,4)))
            print()
            print("Note!")
            print("Saat Melakukan perhitungan pastikan gunakan pembulatan")
            print("agar mendapatkan jawaban yang sesuai dengan taraf error")
            break
        #Bila tidak
        #6. Tentukan   x1  =  x2   ( nilai  x1 digantikan  x2 )
        else:
            x1 = x2
            fx1 = f(x1,p)
            ftx1 = f(x1,trn)

        cektemp = fx2
        n = n + 1

        #7. Kembali ke langkah 3.

        if n%10 == 0:
            input("Lanjut? Tekan enter.")

#--------------------------------------------------------------------------------------------------#
#Langkah-langkah metode Newton Raphson
#1. Ambil satu titik sembarang   x1
#2. Tentukan f '(x)
#3. Hitunglah nilai  f(x1)  dan  f '(x1)
#4. Tentukan nilai   x2   =   x1  -   f(x1) / f '(x1)
#5. Hitunglah nilai  f(x2) .
#Bila nilai f(x2) mendekati 0 , x2 adalah akar persamaan , selesai.
#Bila tidak
#6. Tentukan   x1  =  x2   ( nilai  x1 digantikan  x2 )
#7. Kembali ke langkah 3.
