# Metode Numerik
Metode Numerik yang saya dapatkan dari kuliah saya.

1. Metode Bisection
2. Regula Falsi
3. Newton Raphson
4. ...

# Requirement
Python 3
```bash
pip3 install sympy
```

# Cara Menggunakan

1. Clone Git ini (Download sebagai zip)
2. Jalankan Main.py
3. Masukkan persamaan
4. Pilih Metode
5. Tentukan Pembulatan yang di inginkan (biasanya 2 atau jika mau akurat >=16)
6. Masukkan Nilai awal
7. Dan pada setiap iterasi perkalian 10 tekan enter untuk melanjutkan iterasi

# Metode yang digunakan
## Metode Bisection
1. Ambil dua titik sembarang x1  dan  x2
2. Hitung nilai  f(x1)  dan  f(x2)
2. Tentukan hasil kali tanda bilangan f(x1).f(x2).

Bila f(x1).f(x2)  > 0 , ganti x1 dan x2   ,    Bila   f(x1).f(x2) < 0  (berlawanan tanda) ,

4. Hitung    x3   =  ( x1 + x2 ) / 2
5. Hitung nilai  f(x3)

Bila f(x3)  mendekati nol  , maka  x3 adalah akar persamaan. Selesai.  Bila tidak

6. Tentukan hasil kali tanda bilangan  f(x1).f(x3)

Bila tanda bilangan   f(x1).f(x3)  >  0  maka  x1 =  x3  ( nilai x1 menjadi  x3 ).

Bila tanda bilangan   f(x1).f(x3)  <  0  maka  x2 =  x3  ( nilai x2 menjadi  x3 ).

7. Kembali ke langkah 4.

## Metode Regula Falsi
1. Ambil dua titik sembarang x1 dan x2
2. Hitung nilai f(x1)  dan  f(x2)
3. Tentukan hasil kali tanda bilangan  f(x1) . f(x2)

Bila  f(x1).f(x2)  > 0 , ganti titik x1 dan x2 . Bila  f(x1).f(x2)  < 0  ( berlawanan tanda )

4. Hitung nilai  x3 = (x1 * f(x2) - x2 * f(x1)) / (f(x2) - f(x1))
5. Hitung nilai  f(x3)

Bila nilai f(x3) mendekati nol , maka x3 adalah akar persamaan . Selesai . Bila tidak,

6. Tentukan hasil kali tanda bilangan  f(x1).f(x3)

Bila tanda bilangan f(x1).f(x3)  >  0 , maka  x1  =  x3  ( nilai x1 menjadi  x3 )

Bila tanda bilangan  f(x1).f(x3)  <  0 , maka  x2  =  x3 ( nilai x2 menjadi  x3 )

7. Kembali ke langkah 4.


## Metode Netwon Raphson
Langkah-langkah metode Newton Raphson

1. Ambil satu titik sembarang   x1
2. Tentukan f '(x)
3. Hitunglah nilai  f(x1)  dan  f '(x1)
4. Tentukan nilai   x2   =   x1  -   f(x1) / f '(x1)
5. Hitunglah nilai  f(x2) .

Bila nilai f(x2) mendekati 0 , x2 adalah akar persamaan , selesai.

Bila tidak

6. Tentukan   x1  =  x2   ( nilai  x1 digantikan  x2 )
7. Kembali ke langkah 3.

# Note
Menggunakan Python 3.7 dan Ubuntu (Sudah di test di windows juga)

Saat Melakukan perhitungan pastikan gunakan pembulatan agar mendapatkan jawaban yang sesuai dengan taraf error

Kalian juga dapat menggunakan script masing masing metode tanpa Main.py (Namun harus membawa myfunc.py)

Apabila terdapat kesalahan atau ingin memperbaiki code saya dapat menghubungu saya melalui daffa.daraz@protonmail.com

(Ini code berantakan banget, saya bikin-nya sekalian belajar Python soalnya.)
