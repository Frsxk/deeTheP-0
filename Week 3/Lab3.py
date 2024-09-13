import turtle as t
import random

def initialize_turtle():
    # Fungsi untuk menggambar tabel dan objek tersangka
    pen.pendown()
    pen.hideturtle()
    pen.penup()
    pen.speed(0)

    # Menggambar koordinat kartesius (hanya +)
    # Sumbu X
    pen.goto(0, -250)
    pen.left(90)
    pen.pendown()
    pen.forward(500)
    pen.penup()
    # Sumbu Y
    pen.goto(-250, 0)
    pen.right(90)
    pen.pendown()
    pen.forward(500)
    pen.penup()

    # Menggambar index dari koordinat dan memberikan label
    move = 50
    move_small = 20
    turn = 90
    pen.home()

    # Sumbu X
    for i in range(2):
        for j in range(5):
            pen.pendown()
            pen.forward(move)
            last_position = pen.position()
            pen.left(turn)
            pen.forward(move_small)
            pen.penup()
            pen.backward(move)
            if i == 1:
                k = (j+1)*-1
            else:
                k = j+1
            pen.write(k, False, align="center", font=('Arial', 8, 'normal'))
            pen.goto(last_position)
            pen.right(turn)
        pen.home()
        move, move_small, turn = move *-1, move_small *-1, turn *-1

    # Sumbu Y
    for i in range(2):
        for j in range(5):
            pen.pendown()
            pen.left(turn)
            pen.forward(move)
            last_position = pen.position()
            pen.right(turn)
            pen.forward(move_small)
            pen.penup()
            pen.backward(move/1.2)
            if i == 1:
                k = (j+1)*-1
            else:
                k = j+1
            pen.write(k, False, align="center", font=('Arial', 8, 'normal'))
            pen.goto(last_position)
        pen.home()
        pen.right(180)
        move, move_small, turn = move *-1, move_small *-1, turn *-1
    
    # Menggambar bentuk dengan menggunakan fungsi plot_point()
    list_index.clear() # Agar list_index tidak berisi data dobel dalam pemanggilan initialize_turtle() yang selanjutnya
    for k in list_nama:
        plot_point(k)
        list_index.append(count_index(k))

    # Menulis teks
    pen.goto(0, 270)
    pen.write("Tingkat motif", False, align='center', font=('Arial', 8, 'normal'))
    pen.goto(270, 0)
    pen.write("Tingkat alibi", False, align='left', font=('Arial', 8, 'normal'))

    highest_value = max(list_index)
    highest_index = list_nama[list_index.index(highest_value)]
    pen.goto(0, -270)
    pen.write(f"Tersangka dengan index pelaku tertinggi bernilai {highest_value} adalah {highest_index}", False, align='center', font=('Arial', 8, 'normal'))

    # Menginisialisasi screen
    screen = t.Screen()
    screen.screensize(1500, 1500)
    screen.mainloop()

def seperate_coordinates(string):
    # Fungsi untuk memisahkan dua string koordinat
    # Contoh eksekusi: 13 -> [1, 3], 5-5 -> [5, -5] dst.
    result = []
    current = string[0]

    # Cek apakah string tidak mengandung -
    if len(string) == 2 and current != '-':
        return [string[0], string[1]]
    
    # Logika untuk memisah string
    for character in string[1:]:
        if character == '-' and current != '':
            result.append(current)
            current = character
        else:
            if current == '-':
                current += character
            else:
                result.append(current)
                current = character

    if current:
        result.append(current)
    return result

def plot_point(tersangka):
    # Fungsi untuk menggambar objek tersangka
    index = list_kombinasi[list_nama.index(tersangka)]
    motif = int(seperate_coordinates(index)[0])
    alibi = int(seperate_coordinates(index)[1])

    color = (random.random(), random.random(), random.random())
    if motif  >= 0 and alibi >= 0:
        draw_square(color, motif, alibi, tersangka)
    elif motif < 0 and alibi >= 0:
        draw_diamond(color, motif, alibi, tersangka)
    elif motif < 0 and alibi < 0:
        draw_triangle(color, motif, alibi, tersangka)
    elif motif > 0 and alibi < 0:
        draw_circle(color, motif, alibi, tersangka)

def count_index(tersangka):
    # Fungsi untuk menghitung indeks pelaku
    index = list_kombinasi[list_nama.index(tersangka)]
    motif, alibi = seperate_coordinates(index)
    
    index_pelaku = (int(motif)/2) - (int(alibi)/2)

    return index_pelaku

def draw_square(color, x, y, nama):
    # Fungsi untuk menggambar persegi
    # Set up awal
    posisi_x = (x * 50) + 10
    posisi_y = (y * 50) - 10
    pen.setheading(0)
    pen.goto(posisi_x, posisi_y)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()

    # Menggambar perseegi
    for i in range(4):
        pen.left(90)
        pen.forward(20)
    pen.end_fill()
    pen.penup()

    # Menulis nama dan titik posisi
    pen.goto(posisi_x+5, posisi_y+10)
    pen.write(nama, False, align='left', font=('Arial', 8, 'normal'))
    pen.goto(posisi_x+5, posisi_y)
    pen.write(f"{str(x)}, {str(y)}", False, align='left', font=('Arial', 8, 'normal'))
    pen.home()

def draw_triangle(color, x, y, nama):
    # Fungsi untuk menggambar segitiga
    # Set up awal
    posisi_x = (x * 50) - 10
    posisi_y = (y * 50) - 15
    pen.setheading(0)
    pen.goto(posisi_x, posisi_y)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()

    # Menggambar segitiga
    for i in range(3):
        pen.forward(25)
        pen.left(120)
    pen.end_fill()
    pen.penup()

    # Menulis nama dan titik posisi
    pen.goto(posisi_x+25, posisi_y+10)
    pen.write(nama, False, align='left', font=('Arial', 8, 'normal'))
    pen.goto(posisi_x+25, posisi_y)
    pen.write(f"{str(x)}, {str(y)}", False, align='left', font=('Arial', 8, 'normal'))
    pen.home()
    
def draw_diamond(color, x, y, nama):
    # Fungsi untuk menggambar belah ketupat
    # Set up awal
    posisi_x = (x * 50) + 5
    posisi_y = (y * 50) - 15
    pen.setheading(0)
    pen.goto(posisi_x, posisi_y)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()

    # Menggambar belah ketupat
    pen.left(45)
    pen.forward(20)
    for i in range(3):
        pen.left(90)
        pen.forward(20)
    pen.end_fill()
    pen.penup()

    # Menulis nama dan titik posisi
    pen.goto(posisi_x+18, posisi_y+10)
    pen.write(nama, False, align='left', font=('Arial', 8, 'normal'))
    pen.goto(posisi_x+18, posisi_y)
    pen.write(f"{str(x)}, {str(y)}", False, align='left', font=('Arial', 8, 'normal'))
    pen.home()

def draw_circle(color,x ,y, nama):
    # Fungsi untuk menggambar lingkaran
    # Set up awal
    posisi_x = (x * 50) - (x * 2)
    posisi_y = (y * 50) - 10
    pen.setheading(0)
    pen.goto(posisi_x, posisi_y)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()

    # Menggambar lingkaran, menulis nama dan lokasi lingkaran
    pen.circle(15)
    pen.end_fill()
    pen.penup()
    pen.goto(posisi_x+20, posisi_y+10)
    pen.write(nama, False, align='left', font=('Arial', 8, 'normal'))
    pen.goto(posisi_x+20, posisi_y)
    pen.write(f"{str(x)}, {str(y)}", False, align='left', font=('Arial', 8, 'normal'))
    pen.home()


# Main program
print("Welcome to DekPenol Graphing\n" + "-"*40 + "\n")
list_nama = list()
list_kombinasi = list()
list_index = list()

# Looping opsi pilihan sampai keluar (opsi 3)
while True:
    # Tampilan menu utama program
    print("Pilihan:\n"
    "1) Tambah Tersangka\n"
    "3) Cetak Grafis Tersangka\n"
    "2) Exit\n" + "-"*40)

    choice = input("Pilihan: ")
    print()

    if choice == "1":
        # Opsi 1 menanyakan jumlah tersangka
        while True:
            tersangka = input("Masukkan jumlah tersangka: ")
            if not tersangka.isdigit():
                print("Jumlah tersangka harus dalam angka!")
                print()
                continue
            else:
                tersangka = int(tersangka)
                print()
                break
        
        # Ulangi sebanyak tersangka untuk mendapatkan data untuk setiap tersangka
        for i in range(tersangka):
            j = i+1
            nama = input(f"Masukkan nama tersangka ke-{j}: ")

            while True:
                tingkat_motif = int(input("Masukkan tingkat motif (antara -5 sampai 5): "))
                tingkat_alibi = int(input("Masukkan tingkat alibi (antara -5 sampai 5): "))
                kombinasi = str(tingkat_motif) + str(tingkat_alibi)
                print()

                if (tingkat_motif or tingkat_alibi) > 5 or (tingkat_motif or tingkat_alibi) < -5:
                    print("Nilai tingkat motif dan alibi harus diantara -5 sampai 5!")
                    print()
                    continue
                elif kombinasi in list_kombinasi:
                    print("Kombinasi ini sudah dimasukkan sebelumnya!")
                    print()
                    continue
                list_nama.append(nama)
                list_kombinasi.append(kombinasi)
                break
        print("-"*40)

    elif choice == "2":
        if len(list_nama) > 0:
            # Memastikan screen turtle dapat ditutup dan digunakan kembali
            try:
                pen = t.Turtle()
                initialize_turtle()
            except t.Terminator:
                pen = t.Turtle()
                pen.hideturtle()
                initialize_turtle()
        else:
            print("Belum ada tersangka yang ditambahkan. Gunakan pilihan 1 untuk menambah tersangka.\n")
            continue

    elif choice == "3":
        print("Terima kasih telah menggunakan DekPenol Graphing.")
        exit()
    else:
        # Jika opsi selain 1-3
        print("Input tidak valid!")
        print("-" * 40)
        continue


# DDP-0 ASIK BANGET!