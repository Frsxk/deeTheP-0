# Penulisan opening dari program. Menggunakan \n untuk membuat new line.
print(">>==========================<<\n||                     	    ||\n|| Welcome to Interrogation ||\n||                     	    ||\n>>==========================<<\n")

while True: # Infinite loop agar variabel 'mulai' mendapatkan nilai yang cocok (Y/N)
    mulai = input("Mulai Interogasi (Y/N)? ") # Mulai program
    # Logika pertama
    if mulai == 'Y':
        print("Mari kita mulai interogasi.\n") # \n agar lebih rapih
        
        while True: # Infinite loop agar program dapat menerima banyak data interogasi
            nama = input("Siapa namamu? ")
            npm = input("Berapa nomor NPM mu? ")
            # Logika untuk npm
            counter = 0
            if not npm.isdigit(): # Cek apakah NPM berisi angka saja atau tidak
                print("NPM harus berupa angka!")
                print("------------------------------\n")
                continue
            for char in npm: # Menghitung berapa banyak karakter/digit dalam NPM
                if char.isdigit():
                    counter += 1
            if counter != 10: # Iterasi dihitung hingga 10 kali (10 digits)
                print("NPM harus sepanjang 10 digits!")
                print("------------------------------\n")
                continue
            npm = int(npm) # Mengubah nilai NPM menjadi integer

            pertanyaan_motif = input("Apakah kamu punya motif (Y/N)? ")
            # Logika untuk motif
            if pertanyaan_motif == 'Y':
                motif = input("Apa motif kamu tadi? ")
            elif pertanyaan_motif == 'N':
                motif = "tidak memiliki motif"
            else:
                print("Seseorang harus punya motif atau tidak punya motif sama sekali!")
                print("------------------------------\n")
                continue
                
            pertanyaan_alibi = input("Apakah kamu punya alibi (Y/N)? ")
            # Logika untuk alibi
            if pertanyaan_alibi == 'Y':
                alibi = input("Apa alibi kamu? ")
            elif pertanyaan_alibi == 'N':
                alibi = "tidak memiliki alibi"
            else:
                print("Seseorang harus punya alibi atau tidak punya alibi sama sekali!")
                print("------------------------------\n")
                continue
            print("") # Agar output lebih rapih dengan membuat new line
            
            # Logika kecurigaan dan hasil interogasi
            if pertanyaan_motif == "N" and pertanyaan_alibi == "Y":
                curiga = nama + " tidak terlalu mencurigakan sih"
                print(f"{nama} dengan NPM {npm} {motif} dan memiliki alibi {alibi}.\n{curiga}")
            elif pertanyaan_motif == "Y" and pertanyaan_alibi == "N":
                curiga = "Wah, " + nama + " mencurigakan nihh >:("
                print(f"{nama} dengan NPM {npm} memiliki motif {motif} tapi {alibi}.\n{curiga}")
            else:
                curiga = nama + " lumayan mencurigakan nih..."
                if pertanyaan_motif == "N" and pertanyaan_alibi == "N":
                    print(f"{nama} dengan NPM {npm} {motif} maupun alibi.\n{curiga}")
                else:
                    print(f"{nama} dengan NPM {npm} memiliki motif {motif} dan memiliki alibi {alibi}.\n{curiga}")
            print("------------------------------\n")
            
            valid = False # Menggunakan variabel tambahan karena while loop ada di dalam while loop yang lain, agar lebih mudah
            while not valid:
                lanjut = input("Lanjut interogasi (Y/N)? ")
                if lanjut == 'Y':
                    print("------------------------------\n")
                    valid = True
                elif lanjut == 'N':
                    print('Interogasi telah selesai\n')
                    valid = True
                    break
                else:
                    print("Input tidak valid!\n")
            if lanjut == 'N':
                break
        break
    elif mulai == 'N':
        print("Tidak jadi interogasi\n")
        break
    else:
        print("Input tidak valid!\n")
        continue
    
# Closing dari program. Penggunaan \n seperti opening.
print(">>==========================<<\n||                     	    ||\n|| Ending the Interrogation ||\n||                     	    ||\n>>==========================<<")