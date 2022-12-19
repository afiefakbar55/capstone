datax = {
    12202201:{
        'Nomor Plat':'B 1033 DC',
        'Nama Driver':'Bryan',
        'Merk':'Avanza',
        'Tanggal Peminjaman':'1 Desember 1996',
        'Lama Peminjaman': '3 Hari'
    },
    12202202:{
        'Nomor Plat':'B 612 AA',
        'Nama Driver':'Asep',
        'Merk':'Avanza',
        'Tanggal Peminjaman':'3 Desember 1996',
        'Lama Peminjaman': '3 Hari'
    }
}


def menu():
    while True:
        num = input(f'''
    {'='*20} Welcome to the future X-Car Rent {'='*20}
    
    1. Data rental mobil
    2. Menambahkan data order baru
    3. Mengubah data order
    4. Menghapus data order
    5. Exit

    Masukkan pilihan anda(1-5): ''')
        if num == '1':
            while True:
                read_num = input(f'''
    {'+'*20} Welcome to the future X-Car Rent {'+'*20}

    1. Tampilkan seluruh data
    2. Tampilkan data tertentu
    3. Kembali ke menu utama

    Silahkan pilih submenu read data (1-3):''')
                if read_num == '1':
                    read()
                    break
                elif read_num == '2':
                    read_spec()
                elif read_num == '3':
                    break
                else:
                    print('Masukkan angka 1-3 saja!')
        elif num == '2':
            create()
            break
        elif num == '3':
            update()
            break
        elif num == '4':
            delete()
            break
        elif num == '5':
            while True:
                p = input('Apakah anda yakin ingin keluar? (y/n)')
                if p.lower() == 'y':
                    print('Terima Kasih Sudah Berkunjung! ^^')
                    break
                elif p.lower() == 'n':
                    menu()
                    break
                else:
                    print("Masukkan 'y' or 'n' ")
            break
        else:
            print('Maaf pilihan anda salah')

def read():

    if datax == {}: # ----> Jika data kosong
        print('!!! Maaf data tidak ditemukan !!!')
        n_keluar()

    else:
        print('''\n********** Data X-Car Rent **********
======================================================================''')
        
        for i in datax :
            ngeprint(i)
        n_keluar() # ----> ketik 'n' untuk keluar  
        
def read_spec():
    kategori = input('Masukkan kategori: ').title()
    count = 0 # ----> untuk mencari adakah kategori dan data yang di input terdapat di dalam database
    if kategori != 'Order Id':
        data_mbl = input('Masukkan value kategori yang ingin dicari: ').title()
        if kategori == 'Nomor Plat':
            data_mbl = data_mbl.upper()
        for key,v in datax.items():
            for n,m in v.items():
                if kategori == n and data_mbl == m: # jika kategori dan data yang di input sama dengan yang ada di database
                    count += 1 # ----> memberi tahu bahwa telah ditemukan data sesuai dengan input
                    ngeprint(key)
                else:
                    count += 0

    else:
        data_order = input('Masukkan nomor order id yang ingin dicari: ').title()
        if data_order.isdigit():
            for key in datax.keys():
                if int(data_order) == key:
                    count += 1
                    ngeprint(key)
                else:
                    count += 0
        else:
            print('Masukkan nomor order id! ')

    if count == 0: # ----> Apabila tidak ada data ditemukan sesuai dengan nomor plat, maka print 'data tidak ditemukan'
        print('''!!! Maaf data tidak ditemukan !!!''')
        n_keluar()

def create(): 
    while True:
        create_num = input(f'''\n{'*'*20} menambah order X-Car Rent: {'*'*20}
    1. Tambah data order
    2. Kembali ke menu utama
    
    Pilih pilihan menu diatas (1/2): ''')  # ----> Pilih menu angka 1 atau 2
        if create_num == '1':              # ----> Di Pilihan 1 kita akan memasukkan data-data baru ke dalam database kita 
            print('\nSilahkan masukkan nomor plat mobil: ')
            plat1,plat2,plat3 = nomor_plat() # ----> Input nomor plat di dalam fungsi nomor_plat()
            plat = f'{plat1} {plat2} {plat3}'
            while True:
                driver = input('Masukkan nama driver: ').title()
                if driver.isalpha():
                    merk = input('Masukkan merk mobil: ').title()
                    tanggal_pinjam = tgl_pinjam()
                    lm_pinjam = lama_pinjam() + ' hari'

                    for id in datax.keys(): 
                        pass
                    order_id = id + 1 # ----> Untuk menambahkan order id secara otomatis

                    while True:
                        simpan_data = input('\nApakah anda yakin ingin menyimpan data ini? (y/n)') # ----> Untuk memvalidasi apakah kita ingin menyimpan data tambahan tersebut atau tidak

                        if simpan_data.lower() == 'y':
                            datax.update({order_id:{'Nomor Plat':plat, 'Nama Driver':driver,'Merk':merk,'Tanggal Peminjaman':tanggal_pinjam, 'Lama Peminjaman':lm_pinjam}}) # ----> update data baru
                            print('\nData telah tersimpan!')
                            break
                        elif simpan_data.lower() == 'n':
                            break
                        else:
                            print("Hanya bisa 'y' atau 'n' saja!")

                    break
                else:
                    print('Masukkan huruf saja!\n')
        elif create_num == '2':
            menu()
            break
        else:
            print('Masukkan angka 1 atau 2')

def update():
    while True:
        update_num = input(f'''\n{'*'*20} menambah order X-Car Rent: {'*'*20}
    1. Ubah data sesuai order id
    2. Kembali ke menu utama

    Silahkan pilih sub menu update data (1-2) : ''')
        if update_num == '1':
            order_id = int(input('Masukkan Order id: '))
            count = 0 # ----> untuk mengecek apakah order id yang di input ada di data atau tidak
            for key in datax.keys():
                if order_id == key:
                    count += 1
                    ngeprint(key)

            if count >0:
                yakin = input('Apakah anda yakin ingin mengubah data diatas? (y/n) ')
                if yakin.lower() == 'y':
                    for key in datax.keys():
                        if order_id == key:
                            fitur = input("Masukkan kategori apa yang ingin diubah: ").title()
                            if fitur == 'Nomor Plat':
                                plat1,plat2,plat3 = nomor_plat()
                                datax[key][fitur] = f'{plat1} {plat2} {plat3}'
                                print('\nSelamat anda berhasil mengubah data X-Car Rent!\n')
                            elif fitur == 'Tanggal Peminjaman':
                                tanggal = tgl_pinjam()
                                datax[key][fitur] = tanggal
                                print('\nSelamat anda berhasil mengubah data X-Car Rent!\n')
                            elif fitur == 'Lama Peminjaman':
                                lama1 = lama_pinjam()
                                datax[key][fitur] = lama1 + ' hari'
                                print('\nSelamat anda berhasil mengubah data X-Car Rent!\n')
                            elif fitur == 'Nama Driver':
                                nama = input('Masukkan nama driver: ').title()
                                while True:    
                                    if nama.isalpha():
                                        datax[key][fitur] = nama
                                        print('\nSelamat anda berhasil mengubah data X-Car Rent!\n')
                                        break
                                    else:
                                        print('Masukkan nama driver saja!\n')            
                            elif fitur == 'Merk':
                                merek = input('Masukkan nama merk mobil: ')
                                datax[key][fitur] = merek
                                print('\nSelamat anda berhasil mengubah data X-Car Rent!\n')
                            else:
                                print('Masukkan kategori saja!\n')
            else:
                print('\nData tidak ditemukan !')
                n_keluar()
        elif update_num == '2':
            menu()
            break
        else:
            print('Masukkan angka 1 atau 2 saja.')
                        
def delete():
    while True:
        hapus_menu = input(f'''
{'='*20} Menghapus data order X-Car Rent {'='*20} 
1. Hapus data sesuai Order id
2. Kembali ke menu utama

Silahkan pilih submenu diatas(1-2): ''')
        if hapus_menu == '1':
            hapus_id = input('Masukkan Order id: ')
            count = 0
            for key in datax.copy().keys(): # ----> Agar masih bisa terus looping walaupun size dictionary berubah
                if str(key) == hapus_id:
                    count += 1
                    ngeprint(key)
                    while True:
                        yakin_hapus = input('\nApakah anda yakin ingin menghapus data tersebut? (y/n)')
                        if yakin_hapus.lower() == 'y':
                            listx = []  # ----> Untuk menampung key datax
                            for i in datax.keys():     
                                listx.append(i)
                            for y in range(len(listx)):
                                if int(hapus_id) <= listx[y]: 
                                    if y < len(listx)-1:                                   
                                        datax[listx[y]] = datax[listx[y+1]] # ----> untuk mengganti value key di hapus_id dengan value selanjutnya
                                    else:
                                        del datax[listx[y]] # ----> Lalu menghapus data terakhir (Agar apabila ada data terhapus, order id auto terupdate menjadi berurut lagi)
                            print('\nData telah terhapus!')
                            break
                        elif yakin_hapus.lower() == 'n':
                            break
                        else:
                            print('\nKetik y atau n saja! ')
                else:
                    count += 0
            if count == 0:
                print('\n!!! Maaf data tidak ditemukan !!!')
                n_keluar()
        elif hapus_menu == '2':
            menu()
            break
        else:
            print('Masukkan angka 1 atau 2')


def cek_bulan(bln):
    list_bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
    if bln.isalpha():    
        if bln in list_bulan: # ----> Jika input bulan sesuai dengan nama bulan
            return True
        else:
            return False
    else:
        return False

def ngeprint(key):
    print(f'''
Order id            |   {key}
---------------------------------------------------------
Nomor Plat          |   {datax[key]["Nomor Plat"]}
Nama Driver         |   {datax[key]["Nama Driver"]}
Merk                |   {datax[key]["Merk"]}
Tanggal Peminjaman  |   {datax[key]["Tanggal Peminjaman"]}
Lama Peminjaman     |   {datax[key]["Lama Peminjaman"]}\n''')

def n_keluar():
    while True:
        ketik_n =input('Ketik n untuk keluar:').lower() # ----> agar data masih bisa terlihat setelah ditampilkan
        if ketik_n == 'n':
            return False

def nomor_plat():
    while True:
        plat1 = input('Masukkan kode wilayah: (cth: B)').upper()
        if plat1.isalpha() and len(plat1)<=2:
            while True:
                plat2 = input('Masukkan nomor polisi: (cth: 3124)')
                if plat2.isdigit() and len(plat2)<=4:
                    while True:
                        plat3 = input('Masukkan seri akhir wilayah: (cth: KC)').upper()
                        if plat3.isalpha() and len(plat3)<=3:
                            return plat1,plat2,plat3
                        else:
                            print('Masukkan 4 huruf saja.')
                else:
                    print('Masukkan 4 angka saja.\n')
        else:
            print('Masukkan maksimal 2 huruf saja.\n')

def tgl_pinjam():
    while True:
        tgl = input('Masukkan tanggal berapa mobil ingin dipinjam: ')
        if tgl.isdigit() and int(tgl) <= 31:
            while True:
                bulan = input('Masukkan di bulan apa mobil ingin dipinjam: ').title()
                if cek_bulan(bulan):
                    while True:    
                        tahun = input('Masukkan tahun berapa mobil ingin dipinjam: ').title()
                        if tahun.isdigit() and len(tahun)<=4:
                            date_pinjam = f'{tgl} {bulan} {tahun}'
                            return date_pinjam
                        else:
                            print('Masukkan 4 angka saja!\n')
                else:
                    print('Masukkan nama bulan saja!\n')
        else:
            print('Masukkan angka tanggal saja! (Maksimal tanggal 31)\n')

def lama_pinjam():
    while True:
        lama1 = input('Masukkan berapa hari mobil ingin dipinjam: ')
        if lama1.isdigit():
                return lama1
        else:
            print('Masukkan angka saja!')

menu()
