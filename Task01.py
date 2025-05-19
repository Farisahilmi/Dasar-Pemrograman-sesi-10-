#disini saya akan bikin kotak list dengan buah buahan

keranjang_buah = []

for i in range(5):
    buah = input("masukan nama buah buahan: ")
    keranjang_buah.append(buah)


buah_tuple = tuple(keranjang_buah)

print(buah_tuple)

mencari_buah = input("mencari nama buah: ")

if mencari_buah in buah_tuple:
    print(f"{mencari_buah} ada dalam keranjang")
else:
    print(f"{mencari_buah} tidak ada dalam keranjang")
    

for buah in set(buah_tuple):
    hitung = buah_tuple.count(buah)
    print(f"{buah}: {hitung} kali")