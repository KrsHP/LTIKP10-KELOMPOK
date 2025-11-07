
# Nama: Alfan Aditiansyah
# NIM: 2504879
# Kelas: RPL 1B

# Nama: Kresna Hono Putro
# NIM: 2501870
# Kelas: RPL 1B

student_info = {
    "Alice": {"Umur":20, "Jurusan": "Rekayasa Perangkat Lunak"},
    "Bob": {"Umur": 21, "Jurusan": "Matematika"},
    "Charlie": {"Umur": 19, "Jurusan": "Fisika"},
    "Kirk": {"Umur": 19, "Jurusan": "Biologi"},
}

#Fungsi print ListNama
def ListNama():
    print("+++++++++++++[List Nama]++++++++++++++")
    for i, nama_mahasiswa in enumerate(student_info.keys(), start = 1):
        print(f"{i}. {nama_mahasiswa}")
    print("++++++++++++++++++++++++++++++++++++++")

    user_input1= input("Masukan Nama Mahasiswa:")

    if user_input1 in student_info:
        info = student_info[user_input1]
        print(f"Umur {user_input1} adalah {info['Umur']} dan prodinya adalah {info['Jurusan']}")
    else:
        print("Tidak Valid")

def FungsiUI():
    print("+++++++++++++[Selamat Datang]++++++++++++++")
    print("1.Menambahkan Nama\n2.Melihat Nama\n3.Mengubah Nama\n4.Keluar")
    print("+++++++++++++++++++++++++++++++++++++++++++\n")

#Jalankan FungsiUI
FungsiUI()

#Jalankan fungsi ListNama
ListNama()
