import math # Mengimpor math library

# Penulisan dibuat dalam satu baris dan penggunaan \n untuk masuk ke line berikutnya (enter)
print(">>====================================<<\n||                                    ||\n||  Welcome to Dek Depe's Calculator  ||\n||                                    ||\n>>====================================<<\n")

# Input data dengan menggunakan variable yang diformat
nama = str(input("Nama : "))
tanggal_lahir = str(input("Tanggal Lahir : "))
jurusan = str(input("Jurusan : "))
kelompok = int(input("Kelompok Mentoring : "))
motto = str(input("Motto : "))
alas = int(input("Masukkan alas (cm) : "))
tinggi = int(input("Masukkan tinggi (cm) : "))

# Output dari kode
# Penggunaan f-string untuk menampilkan variable, menggunakan ekspresi, dan menggunakan fungsi
print(f"\nHalo {nama} dari jurusan {jurusan}.") # \n agar lebih rapih
print(f"{nama} berasal dari kelompok mentoring {kelompok}.")
print(f"{nama} lahir pada {tanggal_lahir} dengan motto \"{motto}\".") # Penggunaan \" untuk menampilkan tanda kutip dalam string
print(f"Luas dari segitiga yang dimiliki {nama} adalah {alas*tinggi/2} cm^2.") # Rumus luas segitiga adalah alas * tinggi / 2
# Penggunaan math.ceil agar hasil dibulatkan ke atas
# math.hypot agar mendapatkan sisi miring dari segitiga siku-siku
print(f"Keliling dari segitiga yang dimiliki {nama} adalah {math.ceil(alas + tinggi + math.hypot(alas, tinggi))} cm dengan sisi miring sepanjang {math.hypot(alas, tinggi)} cm.")

# Closing dari code
print("\n>>==========================================<<\n||                                          ||\n||  Thanks for using Dek Depe's Calculator  ||\n||                                          ||\n>>==========================================<<")