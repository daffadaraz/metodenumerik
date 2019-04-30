import os
from myfunc import clear

#Persamaan Ubah Sesuai Keinginan
def f(x):
	return (pow(x,3) + (2 * pow(x,2)) - (4*x) - 4)

def main():
	#var
	check = 1
	n = 0

	clear()

	print("Metode Bisection")
	print("Persamaan, F(X) = x^3 + 2x^2 - 4x - 4") #jangan lupa ubah ini nya.
	print("")
	print("(Berapa angka dibelakang koma)")
	rou = int(input("Pembulatan : "))
	err = float(input("Masukkan Error : "))

	#Check apabila Fx1*Fx2
	while check > 0:
		print("")
		x1 = float(input("Masukkan X1 : "))
		x2 = float(input("Masukkan X2 : "))
		fx1 = round(f(x1),rou)
		fx2 = round(f(x2),rou)
		print("")
		print("Nilai dari, F(%d) = %8.3f " % (x1,fx1))
		print("Nilai dari, F(%d) = %8.3f " % (x2,fx2))
		print("")
		check = fx1*fx2
		if check<0:
			print("Syarat sudah ok.")
			break
		else :
			print("Syarat belum ok %5.2f>0"%(check))

	print("")

	print("X1 = %d , X2 = %d , Error = %.2f"% (x1,x2,err))
	print("______________________________________________________")
	print("  n           x              f(x)             error   ")
	print("______________________________________________________")

	cekerr = err + 1;
	cektemp = cekerr + 1;
	#Cek apabila taraf error sudah sesuai dengan keinginan.
	while cekerr > err:
		n = n + 1
		x3 = round(((x1 + x2)/2),rou)
		fx3 = round(f(x3),rou)
		cekerr = abs(fx3)

		if fx1 * fx3 > 0:
			x1 = x3
		else :
			x2 = x3

		#OUTPUT
		print("%3d|     %.8f       %10.8f      %12.10f" % (n,x3,fx3,abs(fx3)))

		if cekerr <= err or cekerr == cektemp :
			print("_____________________")
			print("Akar Persamaan, %f"%(round(x3,rou)))
			print("Error, %.4f"%(round(cekerr,rou)))
			break

		cektemp = cekerr
		if n%10 == 0:
			input("lanjut?")

if __name__ == '__main__':
	main()

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
