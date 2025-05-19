inventory = {}

pilihan = ""

while pilihan != "7":
    print("pilih menu dibawah ini")
    print("1. tambah barang")
    print("2. tampilkan semua barang")
    print("3. cari barang")
    print("4. update stok")
    print("5. hapus barang")
    print("6. analisis data")
    print("7. keluar")
    pilih = input("pilih menu 1 - 7: ")
    

    if pilihan == "1":
        nama_barang = input("Masukkan nama barang: ")
        if nama_barang in inventory:
            print("Barang sudah ada di inventory.")
        else:
            stok_input = input("Masukkan stok barang: ")
            if stok_input.isdigit():
                stok = int(stok_input)
                inventory[nama_barang] = stok
                print(f"Barang '{nama_barang}' dengan stok {stok} berhasil ditambahkan.")
            else:
                print("Stok harus berupa angka positif.")

    elif pilihan == "2":
        if not inventory:
            print("Inventory kosong.")
        else:
            print("\nDaftar Barang di Inventory:")
            for nama, stok in inventory.items():
                print(f"- {nama}: {stok} unit")
    
    elif pilihan == "3":
        nama_cari = input("Masukkan nama barang yang dicari: ")
        if nama_cari in inventory:
            print(f"Barang '{nama_cari}' ditemukan dengan stok {inventory[nama_cari]} unit.")
        else:
            print(f"Barang '{nama_cari}' tidak ditemukan di inventory.")

    elif pilihan == "4":
        nama_update = input("Masukkan nama barang yang ingin diupdate: ")
        if nama_update in inventory:
            stok_baru = input("Masukkan stok baru: ")
            if stok_baru.isdigit():
                inventory[nama_update] = int(stok_baru)
                print(f"Stok untuk '{nama_update}' telah diperbarui menjadi {stok_baru} unit.")
            else:
                print("Stok harus berupa angka positif.")
        else:
            print(f"Barang '{nama_update}' tidak ditemukan di inventory.")

    
    elif pilihan == "5":
        nama_hapus = input("Masukkan nama barang yang ingin dihapus: ")
        if nama_hapus in inventory:
            del inventory[nama_hapus]
            print(f"Barang '{nama_hapus}' telah dihapus dari inventory.")
        else:
            print(f"Barang '{nama_hapus}' tidak ditemukan di inventory.")

    elif pilihan == "6":
        if not inventory:
            print("Inventory kosong, tidak ada data untuk dianalisis.")
        else:
            total_jenis = len(inventory)
            total_stok = sum(inventory.values())
            barang_terbanyak = max(inventory, key=inventory.get)
            barang_tersedikit = min(inventory, key=inventory.get)

            print("\n=== ANALISIS DATA INVENTORY ===")
            print(f"Jumlah jenis barang: {total_jenis}")
            print(f"Total stok semua barang: {total_stok}")
            print(f"Barang dengan stok terbanyak: {barang_terbanyak} ({inventory[barang_terbanyak]} unit)")
            print(f"Barang dengan stok tersedikit: {barang_tersedikit} ({inventory[barang_tersedikit]} unit)")

    elif pilihan == "7":
        print("Program selesai.")
    else:
        print("Pilihan tidak valid.")