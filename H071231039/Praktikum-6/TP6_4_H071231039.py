def pasanganangka(angka):
    angka.sort()
    i = 0
    jumlah_pasangan = 0
    while i < len(angka) - 1 :
        if angka[i] == angka[i+1]:
            i+=2
            jumlah_pasangan += 1
        else:
            i+=1
    return jumlah_pasangan


list = input("Masukkan beberapa angka dengan spasi: ").split(" ")
print(f"Jumlah Pasangan adalah : {pasanganangka(list)}")