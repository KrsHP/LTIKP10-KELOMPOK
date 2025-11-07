
# Nama: Alfan Aditiansyah
# NIM: 2504879
# Kelas: RPL 1B

student_info = {
    "Alice": {"age":20, "major": "Computer Science"},
    "Bob": {"age": 21, "major": "Mathematics"},
    "Charlie:": {"age": 19, "major": "Physics"},
}

print("""
      +++++++++++++[List Nama]++++++++++++++
      1.Alice
      2.Bob
      3.Charlie
      +++++++++++++++++++++++++++++++++++++
      """)
user_input1= input("Masukan Nama Mahasiswa:")

if user_input1 in student_info:
    info = student_info[user_input1]
    print(f"Umur {user_input1} adalah {info['age']} dan prodinya adalah {info['major']}")
else:
    print("Tidak Valid")
