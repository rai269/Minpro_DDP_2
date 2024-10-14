while True:
    from prettytable import PrettyTable

    uUser  = "RehanParis"
    pUser  = "2409116083"

    uAdmin = "RehanGokil"
    pAdmin = "Admin#1234"

    # nama paket hosting
    paketHosting = [
        {"nama": "Paket b ajah", "Jangka Waktu": "1 bulan", "Harga": 50000},
        {"nama": "Paket Gokil", "Jangka Waktu": "3 bulan", "Harga": 135000},
        {"nama": "Paket Mangsut Amat", "Jangka Waktu": "6 bulan", "Harga": 250000},
        {"nama": "Paket Goks Abiezz", "Jangka Waktu": "9 bulan", "Harga": 360000},
        {"nama": "Paket Gacor Abiezz", "Jangka Waktu": "1 tahun", "Harga": 450000}
    ]

    # function untuk read
    def tampilPaket():
        tabel = PrettyTable()
        tabel.field_names = ["No", "Paket", "Jangka Waktu", "Harga"]
        nomor = 1 
        for paket in paketHosting:
            tabel.add_row([f"[{nomor}]", paket['nama'], paket['Jangka Waktu'], f"Rp{paket['Harga']:,}"])
            nomor += 1
        print(tabel)

    # function untuk menampilkan menu atmint
    def khususAtmint():
        print("Menu paket")
        print("[1]. Tambah paket")
        print("[2]. Tampilkan paket")
        print("[3]. Update paket")
        print("[4]. Hapus paket")
        print("[5]. Keluar")
        pilihan = int(input("Masukkan pilihan: "))
        return pilihan

    # function untuk create
    def tambahPaket():
        print("Tambah Paket")
        nama = input("Masukkan nama paket yang ingin ditambahkan: ")
        jangkaWaktu = input("Masukkan Jangka Waktu yang ingin ditambahkan: ")
        harga = int(input("Masukkan Harga paket yang ingin ditambahkan: "))
        paketHosting.append({"nama": nama, "Jangka Waktu": jangkaWaktu, "Harga": harga})
        print(f"Paket {nama} berhasil ditambahkan")

    # function untuk update
    def updatePaket():
        tampilPaket()
        print("Update data paket")
        nomor = int(input("Masukkan nomor yang mau diupdate: ")) - 1
        paketLama = paketHosting[nomor]
        paketBaru = input("Masukkan nama paket baru: ")
        paketHosting[nomor]['nama'] = paketBaru
        print(f"{paketLama} telah diganti menjadi {paketBaru}")

    # function untuk delete
    def deletePaket():
        tampilPaket()
        print("Hapus paket")
        nomor = int(input("Masukkan nomor yang mau dihapus: ")) - 1
        paketLama = paketHosting.pop(nomor)
        print(f"Paket {paketLama['nama']} telah dihapus")

    # menampilkan output pilihan saat mau login
    tabel = PrettyTable()
    tabel.field_names = ["No", "Log In sebagai"]
    tabel.add_row(["[1]", "User "])
    tabel.add_row(["[2]", "Admin"])
    print(tabel)

    # input login untuk user
    pilih = int(input("Log in sebagai: "))
    try:
        if pilih == 1:
            print("Selamat datang, silahkan log in")
            LogUu = input("Masukkan Username anda: ")
            LogUp = input("Masukkan Password anda: ")
            if LogUu == uUser  and LogUp == pUser :
                print(f"Halo, Selamat datang {LogUu}")
                print("Silahkan pilih paket Hosting Server yang anda inginkan")

                # menampilkan paket data untuk user
                tabel = PrettyTable()
                tabel.field_names = ["No", "Paket", "Jangka Waktu", "Harga"]
                tabel.add_row(["[1]", "Paket b ajah", "1 bulan", "Rp50.000"])
                tabel.add_row(["[2]", "Paket Gokil", "3 bulan", "Rp135.000"])
                tabel.add_row(["[3]", "Paket Mangsut Amat", "6 bulan", "Rp250.000"])
                tabel.add_row(["[4]", "Paket Goks Abiezz", "9 bulan", "Rp360.000"])
                tabel.add_row(["[5]", "Paket Gacor Abiezz", "1 tahun", "Rp450.000"])

                print (tabel)

                # user memilih paket
                try:
                    pilihPaket = int(input("Masukkan pilihan anda: "))
                except ValueError:
                    print("Input harus berupa angka")

                # percabangan 1
                if pilihPaket == 1:
                    print("""Anda memilih Paket b ajah dengan jangka waktu 1 bulan dan harga Rp50.000
Konfirmasi apakah pilihan anda benar?""")
                    konfir = input("ya/tidak: ").lower()

                    if konfir == "ya":
                        print("Silahkan masukkan data diri anda")
                        dataDiriNama = input("Nama (Nama sesuai dengan nama di KTP): ")
                        dataDiriEmail = input("Email (email harus benar sesuai dengan yang digunakan): ")
                        dataDiriDomain = input("Domain (pastikan alamat domain lengkap (contoh : www.ayanamirei.com)): ")

                        data_diri_table = PrettyTable()
                        data_diri_table.field_names = ["Nama", "Email", "Domain", "Harga"]
                        data_diri_table.add_row([f"{dataDiriNama}", f"{dataDiriEmail}", f"{dataDiriDomain}", "Rp50.000"])
                        print(data_diri_table)

                        dataDiriAsk = input("Apakah data diri anda sudah benar? ya/tidak: ")

                        if dataDiriAsk == "ya":
                            print(f"""Selamat, web anda {dataDiriDomain} telah berhasil terbuat. Terima kasih sudah mempercayai kami!
Untuk donasi bisa mengirimkan ke DANA kami dengan nomor 082251794135 (i'm broke :(  )""")
                            break
                        else:
                            print("Mohon isi data diri anda dengan benar")    
                    else:
                        print("Anda membatalkan pilihan")

                # percabangan 2
                elif pilihPaket == 2:
                    print("""Anda memilih Paket Gokil dengan jangka waktu 3 bulan dan harga Rp135.000
Konfirmasi apakah pilihan anda benar?""")
                    konfir = input("ya/tidak: ").lower()

                    if konfir == "ya":
                        print("Silahkan masukkan data diri anda")
                        dataDiriNama = input("Nama (Nama sesuai dengan nama di KTP): ")
                        dataDiriEmail = input("Email (email harus benar sesuai dengan yang digunakan): ")
                        dataDiriDomain = input("Domain (pastikan alamat domain lengkap (contoh : www.ayanamirei.com)): ")

                        data_diri_table = PrettyTable()
                        data_diri_table.field_names = ["Nama", "Email", "Domain", "Harga"]
                        data_diri_table.add_row([f"{dataDiriNama}", f"{dataDiriEmail}", f"{dataDiriDomain}", "Rp135.000"])
                        print(data_diri_table)

                        dataDiriAsk = input("Apakah data diri anda sudah benar? ya/tidak: ")

                        if dataDiriAsk == "ya":
                            print(f"""Selamat, web anda {dataDiriDomain} telah berhasil terbuat. Terima kasih sudah mempercayai kami!!
Untuk donasi bisa mengirimkan ke DANA kami dengan nomor 082251794135 (i'm broke :(  )""")
                            break
                        else:
                            print("Mohon isi data diri anda dengan benar")    
                    else:
                        print("Anda membatalkan pilihan")

                # percabangan 3        
                elif pilihPaket == 3:
                    print("""Anda memilih Paket Mangsut Amat dengan jangka waktu 6 bulan dan harga Rp250.000
Konfirmasi apakah pilihan anda benar?""")
                    konfir = input("ya/tidak: ").lower()

                    if konfir == "ya":
                        print("Silahkan masukkan data diri anda")
                        dataDiriNama = input("Nama (Nama sesuai dengan nama di KTP): ")
                        dataDiriEmail = input("Email (email harus benar sesuai dengan yang digunakan): ")
                        dataDiriDomain = input("Domain (pastikan alamat domain lengkap (contoh : www.ayanamirei.com)): ")

                        data_diri_table = PrettyTable()
                        data_diri_table.field_names = ["Nama", "Email", "Domain", "Harga"]
                        data_diri_table.add_row([f"{dataDiriNama}", f"{dataDiriEmail}", f"{dataDiriDomain}", "Rp250.000"])
                        print(data_diri_table)

                        dataDiriAsk = input("Apakah data diri anda sudah benar? ya/tidak: ")

                        if dataDiriAsk == "ya":
                            print(f"""Selamat, web anda {dataDiriDomain} telah berhasil terbuat. Terima kas ih sudah mempercayai kami!!
Untuk donasi bisa mengirimkan ke DANA kami dengan nomor 082251794135 (i'm broke :(  )""")
                            break
                        else:
                            print("Mohon isi data diri anda dengan benar")    
                    else:
                        print("Anda membatalkan pilihan")

                # percabangan 4
                elif pilihPaket == 4:
                    print("""Anda memilih Paket Goks Abiezz dengan jangka waktu 9 bulan dan harga Rp360.000
Konfirmasi apakah pilihan anda benar?""")
                    konfir = input("ya/tidak: ").lower()

                    if konfir == "ya":
                        print("Silahkan masukkan data diri anda")
                        dataDiriNama = input("Nama (Nama sesuai dengan nama di KTP): ")
                        dataDiriEmail = input("Email (email harus benar sesuai dengan yang digunakan): ")
                        dataDiriDomain = input("Domain (pastikan alamat domain lengkap (contoh : www.ayanamirei.com)): ")

                        data_diri_table = PrettyTable()
                        data_diri_table.field_names = ["Nama", "Email", "Domain", "Harga"]
                        data_diri_table.add_row([f"{dataDiriNama}", f"{dataDiriEmail}", f"{dataDiriDomain}", "Rp360.000"])
                        print(data_diri_table)

                        dataDiriAsk = input("Apakah data diri anda sudah benar? ya/tidak: ")

                        if dataDiriAsk == "ya":
                            print(f"""Selamat, web anda {dataDiriDomain} telah berhasil terbuat. Terima kasih sudah mempercayai kami!!
Untuk donasi bisa mengirimkan ke DANA kami dengan nomor 082251794135 (i'm broke :(  )""")
                        else:
                            print("Mohon isi data diri anda dengan benar")    
                    else:
                        print("Anda membatalkan pilihan")

                # percabangan 5
                elif pilihPaket == 5:
                    print("""Anda memilih Paket Gacor Abiezz dengan jangka waktu 1 tahun dan harga Rp450.000
Konfirmasi apakah pilihan anda benar?""")
                    konfir = input("ya/tidak: ").lower()

                    if konfir == "ya":
                        print("Silahkan masukkan data diri anda")
                        dataDiriNama = input("Nama (Nama sesuai dengan nama di KTP): ")
                        dataDiriEmail = input("Email (email harus benar sesuai dengan yang digunakan): ")
                        dataDiriDomain = input("Domain (pastikan alamat domain lengkap (contoh : www.ayanamirei.com)): ")

                        data_diri_table = PrettyTable()
                        data_diri_table.field_names = ["Nama", "Email", "Domain", "Harga"]
                        data_diri_table.add_row([f"{dataDiriNama}", f"{dataDiriEmail}", f"{dataDiriDomain}", "Rp450.000"])
                        print(data_diri_table)

                        dataDiriAsk = input("Apakah data diri anda sudah benar? ya/tidak: ")

                        if dataDiriAsk == "ya":
                            print(f"""Selamat, web anda {dataDiriDomain} telah berhasil terbuat. Terima kasih sudah mempercayai kami!!
Untuk donasi bisa mengirimkan ke DANA kami dengan nomor 082251794135 (i'm broke :(  )""")
                            break
                        else:
                            print("Mohon isi data diri anda dengan benar")    
                    else:
                        print("Anda membatalkan pilihan")
                else:
                    print("Pilihan tidak valid")     
            else:
                print("Username atau Password salah")

        # input untuk login atmint
        elif pilih == 2:
            print("Selamat datang!")
            LogUu = input("Masukkan Username admin: ")
            LogUp = input("Masukkan Password admin: ")
            if LogUu == uAdmin and LogUp == pAdmin:
                print(f"Login berhasil! Selamat datang {LogUu}")
                
                # percabangan atmint
                while True:
                    pilihan = khususAtmint()
                    if pilihan == 1:
                        tambahPaket()
                    elif pilihan == 2:
                        tampilPaket()
                    elif pilihan == 3:
                        updatePaket()
                    elif pilihan == 4:
                        deletePaket()
                    elif pilihan == 5:
                        print("Keluar dari sistem admin.")
                        break
                    else:
                        print("Pilihan tidak valid")
            else:
                print("Username atau Password admin salah")
        else:
            print("Angka yang anda masukkan tidak ada")
    except ValueError:
        print("Input harus berupa angka")