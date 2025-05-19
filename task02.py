#Student data management using dictionary

data_mahasiswa = {
    "202401" : {
        "nama":"farisa",
        "jurusan":"informatika",
        "ipk":3.5
    },
    
    "2024002": {
        "nama":"aden",
        "jurusan":"sistem informasi",
        "ipk": 4.0
    }
}


while True:
    print("pilih menu dibawah")
    print("1. menambah data")
    print("2. melihat data")
    print("3. cari Nim")
    print("4. hapu data dari Nim")
    print("5. keluar")
    
    
    pilih = input("pilih menu 1 - 5: ")
    
    if pilih == "1":
        nim = input("masukan Nim: ")
        nama = input("masukan nama: ")
        jurusan = input("masukan jurusan: ")
        ipk = input("masukan ipk: ")
        data_mahasiswa[nim] = {"nama":nama, "jurusan":jurusan, "ipk":ipk}
        print("data sudah ditambahkan")
        
    elif pilih == "2":
        print("data mahasiswa: ")
        for nim, data in data_mahasiswa.items():
            print(f"nim: {nim}, nama: {data["nama"]}, jurusan: {data["jurusan"]}, ipk: {data["ipk"]}")
            
    elif pilih == "3":
        nim = input("masukan nim yang dicari: ")
        if nim in data_mahasiswa:
            data = data_mahasiswa[nim]
            print(f"nama: {data["nama"]}, jurusan: {data["jurusan"]}, ipk: {data["ipk"]}")
        else:
            print("data tidak ditemukan")
    
    elif pilih == "4":
        nim = input("masukan nim yang mau dihapus: ")
        if nim in data_mahasiswa:
            del data_mahasiswa[nim]
            print("data berhasil di delet")
        else:
            print("nim tidak ditemukan ")
    elif pilih == "5":
        print("program selesai.")
        break
    else:
        print("pilihan tidak ada, coba lagi")
        