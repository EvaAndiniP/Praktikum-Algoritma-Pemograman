menu = "y" or "Y"
while menu == "y" or "Y":
    print(" ========================================")
    print("Waroeng Nongkrong")
    print("Disokin aja")
    print("Masukkan Nama Anda : ")
    nama = input()
    print("Masukkan Alamat Anda : ")
    alamat = input()
    print("Masukkan No. Telepon Anda : ")
    telepon = input()
    print("Masukkan Tanggal Pemesanan : ")
    tanggal = input()
    print("Pemesanan ini Atas Nama : " + nama)
    print(" ========================================")
    print(" 1. Basreng Bojot : Rp 10.000")
    print(" 2. Baso Aci :  Rp 15.000")
    print(" 3. Seblak Jeletot : Rp 12.000")
    print(" 4. Indomie Goreng : Rp 10.000")
    print(" 5. Kwetiaw : Rp. 24.000")
    print(" ========================================")
    listMenu=str(input(" Masukkan angka sesuai Yang ingin Anda Beli = "))
    jumlahPesanan=int(input(" Jumlah dibeli = "))
    if listMenu == "1":
        namaMenu= " Basreng Bojot "
        harga=(10000*jumlahPesanan)
        if jumlahPesanan >= 5:
            totalHarga=int(harga)
        else:
            totalHarga=int(harga)
    elif listMenu == "2":
        namaMenu= " Baso Aci "
        harga = (15000*jumlahPesanan)
        if jumlahPesanan >= 5:
            totalHarga =int(harga)
        else:
            totalHarga =int(harga)
    elif listMenu == "3":
        namaMenu= " Seblak Jeletot "
        harga=int(12000*jumlahPesanan)
        totalHarga=int(harga)
    elif listMenu == "4":
        namaMenu= " Indomie Goreng"
        harga=int(10000*jumlahPesanan)
        totalHarga = int(harga)
    elif listMenu == "5":
        namaMenu= " Kwetiaw"
        harga=int(240000*jumlahPesanan)
        pajak = int(harga * 0.1)
        totalHarga = int(harga)
    else:
        menu=input(" Maaf,Menu yang dipilih tidak tersedia di restoran")
 
    print(" ===== Struk Pembelian =====")
    print(" Nama\t\t\t : " + nama)
    print(" Alamat\t\t\t : " + alamat)
    print(" No. Telepon\t\t : " + telepon)
    print(" Tanggal Pemesanan\t : " + tanggal)
    print(" Menu\t\t\t :" + namaMenu)
    print(" Jumlah Pesanan\t\t :", jumlahPesanan)
    print(" Harga\t\t\t :", harga)
    print(" ------------------------------")
    print(" Total Pembayaran\t :", totalHarga)
    print(" ------------------------------")
    menu = input(" Mau pesan lagi? pilih Y jika Ya, pilih N jika Tidak (Y/N)")
    if menu == "N"or "n":
        break