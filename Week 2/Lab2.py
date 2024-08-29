
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
        print("Silakan untuk login terlebih dahulu.\n")
        return False
    if banned == True:
        # HINT: Variable "banned" diubah statusnya pada fungsi yang bertujuan untuk mengecek percobaan login.
        print("Maaf, Anda telah gagal login 3 kali. Silakan keluar.\n")
        return False
    return True

# Fungsi untuk meminta data mahasiswa admin. Belum diimplementasikan.
# HINT: Impelementasikan logika loop yang sudah dipelajari pada pekan-pekan sebelumnya.
# Gunakan fungsi/method list yang sesuai untuk menambah elemen ke list.
def ask_admin():
    student = int(input(f"Masukkan banyaknya mahasiswa admin: "))
    # TODO: Implementasi fungsi untuk meminta input NPM mahasiswa dan menyimpannya di "list_admin".
    print()

# Fungsi untuk meminta data mahasiswa tersangka. Bel um diimplementasikan.
# HINT: Impelementasikan logika loop yang sudah dipelajari pada pekan-pekan sebelumnya.
# Gunakan fungsi/method list yang sesuai untuk menambah elemen ke list.
def ask_suspected():
    student = int(input("Masukkan banyaknya mahasiswa tersangka: "))
    # TODO: Implementasi fungsi untuk meminta input NPM mahasiswa dan menyimpannya di "list_suspected".
    print()

# Fungsi untuk meminta data yang terekam CCTV. Belum diimplementasikan.
# HINT: Impelementasikan input dan logika loop yang sudah dipelajari pada pekan-pekan sebelumnya.
# Gunakan fungsi/method list yang sesuai untuk menambah elemen ke list.
def ask_case():
    case = int(input(f"Masukkan banyaknya data yang terekam CCTV: "))
    # TODO 1: Implementasi fungsi untuk meminta input nama, waktu, dan lantai tempat terdeteksi mahasiswa.
    # TODO 2: Simpan input ke dalam list yang bersesuaian.
    # TODO 3: Gunakan string formatting yang sesuai untuk membuat kode mahasiswa. Kemudian, simpan ke dalam "list_code".

    # HINT: Iterasi dengan loop sebanyak input case.
    print()

# Fungsi untuk menjalankan menu login pada opsi menu 1. Belum diimplementasikan.
def execute_login():
    attempt = 0
    succeed = False
    while attempt < 3 and not succeed:
        npm = input("Masukkan NPM mahasiswa admin yang telah terdaftar:")
        # TODO 1: Implementasi fungsi untuk mengecek apakah NPM yang dimasukkan merupakan NPM mahasiswa admin.
        # HINT: Gunakan variabel succeed dengan mengubah nilainya menjadi True jika NPM ditemukan.

        # TODO 2: Implementasi fungsi untuk mengecek apakah percobaan login sudah mencapai 3 kali.
        # HINT: Increment variabel attempt jika login gagal. Jika sudah mencapai 3 kali, ubah status variabel yang bersangkutan pada fungsi lainnya.
    print()
    return attempt # Value yang di-return digunakan pada main untuk menandakan jumlah percobaan login.

# Fungsi untuk menjalankan menu yang menampilkan riwayat CCTV pada menu 2. Belum diimplementasikan.
# HINT: Anda hanya perlu menambahkan argumen yang bersesuaian pada fungsi print() yang sudah diimplementasikan.
def execute_logcheck():
    print("{:>4} | {:^10} | {:^7} | {:<15}".format("Kode", "Nama", "Waktu", "Lokasi (lantai)"))
    for i in range(len(list_code)):
        print("{:>4} | {:<10} | {:^7} | {:<15}".format("")) # TODO: Masukkan argumen dengan mengambil list yang bersesuaian pada elemen ke-i.
        print()

# Fungsi untuk menghitung persentase kemungkinan tersangka pada menu 3. Belum diimplementasikan.
def execute_suspect():
    while True:
        code = input("Masukkan kode mahasiswa tersangka: ")
        # TODO: Implementasi fungsi yang memvalidasi input code.
        # Hint: Gunakan if else statement untuk memvalidasi input code.
        break

    while True:
        time = input("Masukkan dugaan waktu kejadian: ")
        # TODO: Implementasi fungsi yang memvalidasi input time.
        # HINT: Gunakan if else statement serta string slicing untuk memvalidasi input time.
        '''HINT: Input time memiliki panjang 5 karakter, dengan elemen pada 2 index pertama dan 2 terakhir harus berupa angka.
        Anda dapat menggunakan method .isdigit(). Elemen pada 2 index pertama tidak boleh lebih dari 24, serta pada 2 terakhir
        tidak boleh lebih dari 60.'''
        break

    while True:
        level = input("Masukkan dugaan lokasi (lantai) kejadian: ")
        # TODO: Implementasi fungsi yang memvalidasi input level.
        # HINT: Gunakan if else statement untuk memvalidasi input level.
        # HINT: Input level harus berupa angka dan tidak boleh lebih dari 7 serta tidak boleh kurang dari 0.
        break

    num_code = int(code[-2:])
    num_time = int(time[:2]) * 60 + int(time[-2:])
    num_level = int(level)
    if num_code == 3:
        mux_code = 15
    else:
        mux_code = 10

    percentage = max((mux_code + (45 - abs(871 - num_time)) + (40 - abs(2 - num_level) * 5)), 0)
    list_result.append(list_suspected[num_code])
    list_percentage.append(percentage)

    print(f"Berhasil meninjau tersangka pada mahasiswa dengan nama {list_suspected[num_code]} pada pukul {time} di lantai {level}.\n")

# Fungsi untuk mencetak ringkasan tersangka pada menu 4. Belum diimplementasikan.
# HINT: Anda hanya perlu menambahkan argumen yang bersesuaian pada fungsi print() yang sudah diimplementasikan.
def execute_summarize():
    if len(list_percentage) == 0:
        most_suspected = "Tidak ada"
    else:
        print("{:>6} | {:^10} | {:<25}".format("Dugaan", "Nama", "Persentase Menjadi Pelaku"))
        for i in range(len(list_result)):
            print("{:>6} | {:<10} | {:<25}".format("")) # TODO: Masukkan argumen dengan mengambil list yang bersesuaian pada elemen ke-i. 
            if sum(list_percentage) // len(list_percentage) >= 40:
                index_name = list_percentage.index(max(list_percentage))
                most_suspected = list_result[index_name]
            else:
                most_suspected = logged_student + " (admin)"
                print(f"Nama/NPM mahasiswa tersangka yang paling mungkin: {most_suspected}\n")

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