import os
import random
from myfunc import clear

#--------------------------------------------------------------------------------------------------#
#Permilihan Metode Numerik
#--------------------------------------------------------------------------------------------------#
def method():
	pil = 4
	print("Metode yang ingin di gunakan?")
	print("1. Metode Bisection")
	print("2. Regula Falsi")
	print("3. Exit")
	pil = int(input("Masukkan Pilihan : "))
	if(pil==1):
		jud = "Method Bisection"
	elif(pil==2):
		jud = "Regula Falsi"
	elif(pil == 3):
		exit()
	else:
		print("Wrong Input.")
		exit()
	return pil,jud

#--------------------------------------------------------------------------------------------------#
#Menghitung Persamaan
#--------------------------------------------------------------------------------------------------#
def f(x):
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

#--------------------------------------------------------------------------------------------------#
# Fungsi main
#--------------------------------------------------------------------------------------------------#
def main():
	#var
	check = 1
	n = 0

	clear ()

	#pil[0] berisi pilihan metode pil[1] berisi string metode
	print("%s"%(pil[1]))
	print("Persamaan, %s"%(pers))
	print()
	print("(Berapa angka dibelakang koma. Masukkan 16 jika tidak yakin)")
	rou = int(input("Pembulatan : "))
	err = float(input("Masukkan Error : "))

	while check >= 0:
		print()
		x1 = float(input("Masukkan X1 : "))
		x2 = float(input("Masukkan X2 : "))
		fx1 = round(f(x1),rou)
		fx2 = round(f(x2),rou)
		print()
		print("Nilai dari, F(%d) = %f " % (x1,fx1))
		print("Nilai dari, F(%d) = %f " % (x2,fx2))
		print()
		check = fx1*fx2
		if check < 0:
			print("Syarat sudah ok. f(%d)*f(%d) < 0 || %5.2f < 0"%(x1,x2,check))
		else:
			print("Syarat belum ok f(%d)*f(%d) >= 0 || %5.2f >= 0"%(x1,x2,check))

	print()
	#Mempersiapkan output berupa tabel
	print("X1 = %d , X2 = %d , Error = %.6f"% (x1,x2,err))
	print("_______________________________________________________")
	print("  n           x              f(x)             error    ")
	print("_______________________________________________________")

	#Hanya untuk initialisasi
	cekerr = err + random.randint(1,10)
	cektemp = cekerr + random.randint(1,10)

	while cekerr > err:
		#Counter Iterasi
		n = n + 1

		#pil[0] berisi pilihan metode pil[1] berisi string metode
		if (pil[0] == 1):
			x3 = round(((x1 + x2)/2),rou)
		elif (pil[0] == 2):
			x3 = round(((x1 * f(x2) - x2 * f(x1)) / (f(x2) - f(x1))),rou)

		fx3 = round(f(x3),rou)
		cekerr = abs(fx3)

		#Output Sesuai bentuk tabel
		print("%3d|     %.8f       %10.8f      %12.10f" % (n,x3,fx3,cekerr))

		#Print Akar Persamaan
		if cekerr <= err or cekerr == cektemp :
			print("________________")
			print("Akar Persamaan, %.36f"%(x3))
			print("Atau ~ %.4f"%(round(x3,4)))
			print("Error, %.4f"%(round(cekerr,4)))
			print()
			print("Note!")
			print("Saat Melakukan perhitungan pastikan gunakan pembulatan")
			print("agar mendapatkan jawaban yang sesuai dengan taraf error")
			break

		if f(x1) * f(x3) > 0:
			x1 = x3
		else :
			x2 = x3

		cektemp = cekerr

		#Agar memudahkan pembacaan iterasi. setiap 10 iterasi di stop.
		if n%10 == 0:
			input("Lanjut? Tekan enter.")

#--------------------------------------------------------------------------------------------------#
# Main Menu dan Pemanggilan fungsi fungsi
#--------------------------------------------------------------------------------------------------#
if __name__ == '__main__':
	clear()
	#Initialisasi Variable
	pil2 = 'y'
	pil3 = 'n'

	while(pil2 == 'y' or pil2 == 'Y'):
		if pil3 == 'n' or pil3 == 'N':
			print("ex. x^3 + 2*x^2 - 4*x - 4")
			pers = str(input("Masukkan Persamaan : "))
			p = persamaan(pers)

		print()

		#Pemilihan Metode Numerik
		pil = method()

		main()

		print()

		pil2 = input("Ulang ? (y/n) : ")
		if pil2 =='y' or pil2 == 'Y':
			pil3 = input("Ulang dengan Persamaan yang sama ? (y/n) : ")


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
#--------------------------------------------------------------------------------------------------#
# Metode Regula Falsi yang digunakan
# 1. Ambil dua titik sembarang  x1  dan   x2
# 2. Hitung nilai f(x1)  dan  f(x2)
# 3. Tentukan hasil kali tanda bilangan  f(x1) . f(x2)
#    Bila  f(x1).f(x2)  > 0 , ganti titik x1 dan x2 . Bila  f(x1).f(x2)  < 0  ( berlawanan tanda )
# 4. Hitung nilai  x3 = (x1 * f(x2) - x2 * f(x1)) / (f(x2) - f(x1))
# 5. Hitung nilai  f(x3)
#    Bila nilai f(x3) mendekati nol , maka x3 adalah akar persamaan . Selesai . Bila tidak,
# 6. Tentukan hasil kali tanda bilangan  f(x1).f(x3)
#    Bila tanda bilangan f(x1).f(x3)  >  0 , maka  x1  =  x3  ( nilai x1 menjadi  x3 )
#    Bila tanda bilangan  f(x1).f(x3)  <  0 , maka  x2  =  x3 ( nilai x2 menjadi  x3 )
# 7. Kembali ke langkah 4.
#--------------------------------------------------------------------------------------------------#
