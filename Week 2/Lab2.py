
# Fungsi untuk mencetak tampilan menu utama. Sudah diimplementasikan.
def main_menu():
    print("="*20 + " Selamat datang di PacilSeeker! " + "="*20 + "\n"
    "(1) Masuk\n"
    "(2) Lihat riwayat CCTV\n"
    "(3) Tinjau kemungkinan tersangka\n"
    "(4) Cetak ringkasan tersangka\n"
    "(5) Keluar")

# Fungsi untuk mengecek apakah pengguna sudah login dan belum diblokir. Sudah diimplementasikan.
def authorized(logged: bool, banned: bool) -> bool:
    if logged == False:
        print("Silahkan untuk login terlebih dahulu.\n")
        return False
    if banned == True:
        print("Maaf, Anda telah gagal login 3 kali. Silakan keluar.\n")
        return False
    return True

# Fungsi untuk meminta data mahasiswa admin.
def ask_admin():
    student = int(input(f"Masukkan banyaknya mahasiswa admin: "))
    # Menggunakan For Loop dan infinite loop untuk mengulang program sebanyak mahasiswa admin
    for i in range(student):
            j = i + 1
            while True:
                npm = input(f"NPM mahasiswa admin ke-{j}: ")
                if not npm.isdigit():
                    print('NPM harus berupa angka!')
                    continue
                if len(npm) != 10:
                    print('NPM harus berjumlah 10 angka!')
                    continue
                list_admin.append(npm)
                break
    print()

# Fungsi untuk meminta data mahasiswa tersangka.
def ask_suspected():
    while True:
        student = int(input("Masukkan banyaknya mahasiswa tersangka: "))
        if student > 999999:
            print('Mahasiswa tersangka tidak boleh lebih dari 999999 orang!')
            continue
        elif student < 4:
            print("Mahasiswa tersangka harus minimal 4 orang!")
            continue
        break
    # Menggunakan For Loop dan infinite loop untuk mengulang program sebanyak mahasiswa tersangka.
    for i in range(student):
        j = i + 1
        while True:
            tersangka = input(f"Nama mahasiswa tersangka ke-{j}: ")
            list_suspected.append(tersangka) # Menyimpan data di list_suspected.
            break
    print()

# Fungsi untuk memvalidasi waktu, menghasilkan boolean
def is_time_valid(time_string) -> bool:
    if len(time_string) != 5 or time_string[2] != ':':
        return False
    
    hour = time_string[:2]
    minute = time_string[-2:]

    if not (hour.isdigit() and minute.isdigit()):
        return False
    if not int(time_string[:2]) <= 24 and not int(time_string[-2:]) <= 60:
        return False
    return True

# Fungsi untuk meminta data yang terekam CCTV.
def ask_case():
    case = int(input(f"Masukkan banyaknya data yang terekam CCTV: "))
    # Fungsi untuk meminta input nama, waktu, dan lantai tempat terdeteksi mahasiswa.
    while True:
        if case > 99:
            print("Banyak data tidak boleh lebih dari 99")
            continue
        break
    
    counter = 1
    for i in range(case):
        j = i + 1
        while True:
            print(f"========== Kasus ke-{j} ==========")
            nama = input("Nama mahasiswa: ")
            if len(nama) > 10:
                print("Nama tidak boleh lebih panjang dari 10 karakter!")
                continue
            waktu = input("Waktu terdeteksi (HH:MM) : ")
            if not is_time_valid(waktu):
                print("Input waktu tidak valid!")
                continue
            lantai = input("Lantai tempat terdeteksi (0-7): ")
            if not (lantai.isdigit() and int(lantai) <= 7 and int(lantai) >= 0):
                print("Input lantai tidak valid!")
                continue

            # Simpan input ke dalam list yang bersesuaian.
            list_name.append(nama)
            list_time.append(waktu)
            list_level.append(lantai)

            # Gunakan string formatting yang sesuai untuk membuat kode mahasiswa. Kemudian, simpan ke dalam "list_code".
            x = lantai
            if counter < 10:
                y = '0' + str(counter)
            else:
                y = str(counter)
            kode_mahasiswa = x + str(y)
            list_code.append(kode_mahasiswa)
            counter += 1
            break
        # if nama in list_suspected and i > 0:
        #     y ='0' + str(list_name.index(nama) + 1)
        #     list_code[i-1] = list_code[i-1][:2] + str(j)
    print()

# Fungsi untuk menjalankan menu login pada opsi menu 1.
def execute_login():
    attempt = 0
    succeed = False
    while attempt < 3 and not succeed:
        npm = input("Masukkan NPM mahasiswa admin yang telah terdaftar: ")

        # Fungsi untuk mengecek apakah NPM yang dimasukkan merupakan NPM mahasiswa admin.
        if not npm in list_admin:
            print(f'Maaf, NPM {npm} tidak terdaftar sebagai admin.')
            attempt += 1
            continue
        succeed = True
        logged_student = npm
        print(f'Selamat datang, mahasiswa dengan NPM {npm}!')

        # Cek apakah percobaan login sudah mencapai 3 kali, dan mengubah variabel 'banned'
        if attempt == 3:
            banned = True
    print()
    return attempt # Value yang di-return digunakan pada main untuk menandakan jumlah percobaan login.

# Fungsi untuk menjalankan menu yang menampilkan riwayat CCTV pada menu 2.
def execute_logcheck():
    print("{:>4} | {:^10} | {:^7} | {:<15}".format("Kode", "Nama", "Waktu", "Lokasi (lantai)"))
    for i in range(len(list_code)):
        print("{:>4} | {:<10} | {:^7} | {:<15}".format(list_code[i], list_name[i], list_time[i], list_level[i]))
    print()

# Fungsi untuk menghitung persentase kemungkinan tersangka pada menu 3.
def execute_suspect():
    while True:
        code = input("Masukkan kode mahasiswa tersangka: ")
        # Implementasi fungsi yang memvalidasi input code.
        if not code in list_code:
            print(f"Maaf, mahasiswa dengan kode {code} tidak terdaftar pada sistem.")
            continue
        elif len(code) != 3:
            print('Kode yang dimasukkan tidak valid!')
        else:
            break
    
    while True:
        time = input("Masukkan dugaan waktu kejadian: ")
        # Menggunakan fungsi is_time_valid untuk memvalidasi input waktu.
        if is_time_valid(time):
            break
        else:
            print('Input waktu tidak valid!')
            continue

    while True:
        level = input("Masukkan dugaan lokasi (lantai) kejadian: ")
        # Logika untuk memvalidasi input level.
        if level.isdigit() and int(level) <= 7 and int(level) >= 0:
            break
        else:
            print(f"Maaf, lantai {level} tidak ada.")
            continue

    num_code = int(code[-1:])-1
    num_time = int(time[:2]) * 60 + int(time[-2:])
    num_level = int(level)
    if num_code + 1 == 3:
        mux_code = 15
    else:
        mux_code = 10

    percentage = max((mux_code + (45 - abs(871 - num_time)) + (40 - abs(2 - num_level) * 5)), 0)
    list_result.append(list_name[num_code])
    list_percentage.append(percentage)
    print(list_result, list_percentage, list_suspected)

    print(f"Berhasil meninjau tersangka pada mahasiswa dengan nama {list_name[num_code]} pada pukul {time} di lantai {level}.\n")

# Fungsi untuk mencetak ringkasan tersangka pada menu 4.
def execute_summarize():
    if len(list_percentage) == 0:
        most_suspected = "Tidak ada"
        print(f"Nama/NPM mahasiswa tersangka yang paling mungkin: {most_suspected}\n")
    else:
        print("{:>6} | {:^10} | {:<25}".format("Dugaan", "Nama", "Persentase Menjadi Pelaku"))
        for i in range(len(list_result)):
            print("{:>6} | {:<10} | {:<25}".format(i+1, list_result[i], str(list_percentage[i])+"%")) 
        if sum(list_percentage) // len(list_percentage) >= 40:
            index_name = list_percentage.index(max(list_percentage))
            most_suspected = list_result[index_name]
            print(f"Nama/NPM mahasiswa tersangka yang paling mungkin: {most_suspected}")
        else:
            most_suspected = logged_student + " (admin)"
            print(f"Nama/NPM mahasiswa tersangka yang paling mungkin: {most_suspected}")
        print()

# Program utama.
if __name__ == "__main__":
    list_admin = list()
    list_suspected = list()
    list_code = list()
    list_name = list()
    list_time = list()
    list_level = list()
    list_result = list()
    list_percentage = list()
    logged_student = str()

    running = True
    logged = False
    banned = False

    ask_admin()
    ask_suspected()
    ask_case()

    while running:
        main_menu()
        action = int(input("Masukkan pilihan menu: "))
        print("="*72)

        if action == 1:
            if banned == True:
                print("Maaf, Anda telah gagal login 3 kali. Silakan keluar.\n")
                continue
            attempt = execute_login()

            if attempt == 3:
                logged = True
                banned = True
            else:
                logged = True

        elif action == 2:
            if authorized(logged, banned) == False:
                continue
            execute_logcheck()

        elif action == 3:
            if authorized(logged, banned) == False:
                continue
            execute_suspect()

        elif action == 4:
            if authorized(logged, banned) == False:
                continue
            execute_summarize()

        elif action == 5:
            running = False

        else:
            print("Maaf, pilihan menu Anda tidak diketahui.\n")

    print("Terima kasih karena telah menggunakan PacilSeeker!")