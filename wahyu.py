# Import module bahasa
import gettext
gettext.install('hitunggaji', 'locale')

# Buat daftar karyawan
karyawan = []

def daftar_karyawan():
    nama = input(_("Masukkan nama karyawan : "))
    pekerjaan = input(_("Masukkan pekerjaan karyawan : "))
    gaji = int(input(_("Masukkan gaji karyawan : ")))
    karyawan.append([nama, pekerjaan, gaji])

def lihat_karyawan():
    print(_("\nSemua Karyawan :"))
    for data in karyawan:
        print(_("Nama : "), data[0])
        print(_("Pekerjaan : "), data[1])
        print(_("Gaji : "), data[2])
        print(_("==============================="))

def hapus_karyawan():
    nama = input(_("Masukkan nama karyawan yang ingin dihapus : "))
    for i in range(len(karyawan)):
        if karyawan[i][0] == nama:
            karyawan.pop(i)
            print(_("\nKaryawan berhasil dihapus"))
            break
    else:
        print(_("\nKaryawan tidak ditemukan"))

def gaji_tertinggi():
    gaji_tertinggi = 0
    nama_tertinggi = ''
    for data in karyawan:
        if data[2] > gaji_tertinggi:
            gaji_tertinggi = data[2]
            nama_tertinggi = data[0]
    return gaji_tertinggi, nama_tertinggi

def main():
    while True:
        print(_("\nMenu Meghitung Gaji Karyawan :"))
        print(_("1. Daftar Karyawan"))
        print(_("2. Lihat Karyawan"))
        print(_("3. Hapus Karyawan"))
        print(_("4. Gaji Tertinggi"))
        print(_("5. Keluar"))
        pilihan = int(input(_("Masukkan pilihan anda : ")))
        if pilihan == 1:
            daftar_karyawan()
        elif pilihan == 2:
            lihat_karyawan()
        elif pilihan == 3:
            hapus_karyawan()
        elif pilihan == 4:
            gaji, nama = gaji_tertinggi()
            print(_("\nGaji Tertinggi : "), gaji)
            print(_("Nama : "), nama)
        elif pilihan == 5:
            break
        else:
            print(_("\nPilihan tidak valid, silahkan coba lagi"))

if __name__ == "__main__":
    main()