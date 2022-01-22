# TAMPILANAN AWAL APLIKASI
def tampilan_awal_bank():
  # Isi Fungsi def
  print("="*80) # Line Tampilan
  print("\t\t\t    SELAMAT DATANG di BANK JAGO") # Tampilan
  print("="*80) # Line Tampilan
  print() # Sebagai Spasi
  print("\t\tAnda Harus Membuat Akun Virtual Bank Terlebih dahulu") # Tampilan
  tanya_user() # memanggil fungsi tanya_user() untuk menanyakan user untuk membuat akun
# AKHIR DARI TAMPILAN APLIKASI



# Fungsi untuk baris 
def spasi(): 
  # Isi Fungsi def yang berisikan pring kosong untuk spasi
  print() # Sebagai Spasi
  print() # Sebagai Spasi
  print() # Sebagai Spasi
  print() # Sebagai SPasi
  print() # Sebagai Spasi



# PERTANYAAN UNTUK PEMBUATAN AKUN "APAKAH ANDA INGIN BUAT AKUN ?"
# JIKA USER INGIN MEMBUAT AKUN AKAN LANJUT KE PEMBUATAN AKUN
# JIKA TIDAK AKAN MENGELUARKAN TAMPILAN KELUAR
def tanya_user(): # fungsi untuk menanyakan user untuk membuat akun
  spasi() # Memanggil Fungsi Spasi untuk membuat Spasi
  # Isi Fungsi def
  print("\t\t\t\tIngin Membuat Akun?") # Tampilan
  print("\t\t\t\t\t(y/t)") # Tampilan
  spasi() # Memanggil Fungsi Spasi
  print("Ketik 'y' untuk Ya ketik 't' Untuk Tidak") # Tampilan

  tanya=input(">>> ") # fungsi input untuk menjawab pertanyaan (Format String)
  if tanya == 'y' or tanya == 'Y' or tanya == 'Ya' or tanya == "YA": # Jika input y maka akan ke fungsi buat akun
    spasi() # Memanggil Fungsi Spasi untuk membuat spasi
    buat_akun() # memanggil fungsi buat_akun() untuk membuat akun
  elif tanya == 't' or tanya == 'T' or tanya == 'Tidak' or tanya == "TIDAK": # Jika input t maka akan ke menampilkan
    spasi() # Memanggil Fungsi Spasi untuk membuat spasi
    print("\t\t    TERIMAKASIH TELAH MENGGUNAKAN LAYANAN KAMI") # Tampilan input T
    spasi() # Memanggil Fungsi Spasi untuk membuat spasi
    exit() #fungsi keluar otomatis dari program
  else: # Keculai. Input tidak sesuai maka akan menampilkan ...
    print("ERROR : Input yang Anda masukkan Salah, silahkan input lagi") # Tampilan Else
    print("Ketik 'y' untuk Ya ketik 't' untuk Tidak") # Tampilan Else
    tanya_user() # memanggil kembali fungsi tanya user untuk membuat akun karena input yang tidak benar
# AKHIR DARI PERTANYAAN "APAKAH INGIN MEMBUAT AKUN"



# SISTEM PEMBUATAN AKUN
def buat_akun(): # fungsi untuk membuat akun
  # Isi Fungsi def
  print() # Sebagai Spasi
  print('-'*80) # Line Tampilan
  print ("\t\t\t\tPembuatan AKUN Rekening") # Tampilan
  print('-'*80) # Line Tampilan
  print("NOTE : Perhatikan pengisian Anda saat Pembuatan AKUN Rekening, semua yang Anda isi akan terproses sebagaimana Anda mengisinya. Perhatikan dengan baik dan hati-hati") # Tampilan
  spasi() # Memanggil Fungsi Spasi

  # BUAT NAMA
  nama = None # Mendefinisikan nilai kosong pada variabel kosong
  while nama != '0': # Perulangan while jika variabel nama tidak kosong
    try: # coba buat
      nama = input("Masukkan Nama Lengkap Anda : ") # fungsi input untuk user (Format String)
      if nama == "": # jika nama kosong akan keluar hasil
        print("Input yang Anda masukkan KOSONG . Harap input kembali dengan benar") 
      elif (type(int(nama)))==int : # mendefinisikan variabel nama dengan intger(angka) jika isi input dengan angka maka akan keluar hasil 
        print("ERROR : Masukkan input dengan HURUF . Jangan Memasukkan ANGKA, SIMBOL, atau KOSONG")
    except ValueError: # fungsi untuk mengecualikan debugging/error yaitu jika input tidak sesuai(integer)/kosong
      break # Berhenti dari Perulangan/Looping karena input sesuai
  # AKHIRAN

  # BUAT UMUR
  while True: # perulangan while dengan bernilai True . Jika try bernilai False maka akan looping
    try: # Coba buat
      umur = int(input("Masukkan Umur : "))# fungsi input untuk user (Format Integer)
      umurr = str(umur) # mendefinisikan nilai umur menjadi string
      if len(umurr) > 2: # jika panjang umur lebih dari 2 maka akan keluar hasil error dan akan mengulang lagi
        print("Error : Input Anda lebih dari 2 Digit") # Tampilan IF
      else:
        break # jika benar maka perulangan/looping berhenti
    except ValueError: # fungsi untuk mengecualikan debugging/error yaitu jika input tidak sesuai(integer)/kosong
      print("ERROR : Masukkan input dengan ANGKA . Jangan memasukkan HURUF, SIMBOL, atau KOSONG")
  # AKHIRAN

  # BUAT JENIS KELAMIN
  jenis_kelamin = None # Mendefinisikan nilai kosong pada variabel kosong
  while jenis_kelamin != '0': # Perulangan while jika variabel nama tidak kosong
    try: # Coba buat
      jenis_kelamin = input("Masukkan Jenis Kelamin Anda : ") # fungsi input untuk user (Format String)
      if jenis_kelamin == "": # jika nama kosong akan keluar hasil
        print("Input yang Anda masukkan KOSONG . Harap input kembali dengan benar") # Tampilan IF
      elif (type(int(jenis_kelamin)))==int : # mendefinisikan variabel nama dengan intger(angka) jika isi input dengan angka maka akan keluar hasil 
        print("ERROR : Masukkan input dengan HURUF . Jangan Memasukkan ANGKA, SIMBOL, atau KOSONG") # Tampilan ELIF
    except ValueError: # fungsi untuk mengecualikan debugging/error yaitu jika input tidak sesuai(integer)/kosong
      break #berhenti dari perulangan/looping karena input sesuai   
  # AKHIRAN

  # BUAT ASAL TEMPAT LAHIR
  tempat_lahir = None # Mendefinisikan nilai kosong pada variabel kosong
  while tempat_lahir != '0': # Perulangan while jika variabel nama tidak kosong
    try: # Coba buat
      tempat_lahir = input("Masukkan Tempat Lahir Anda : ") # fungsi input untuk user (Format String)
      if tempat_lahir == "": # jika nama kosong akan keluar hasil
        print("Input yang Anda masukkan KOSONG . Harap input kembali dengan benar") # Tampilan IF
      elif (type(int(tempat_lahir)))==int : # mendefinisikan variabel nama dengan intger(angka) jika isi input dengan angka maka akan keluar hasil 
        print("ERROR : Masukkan input dengan HURUF . Jangan Memasukkan ANGKA, SIMBOL, atau KOSONG") # Tampilan ELIF
    except ValueError: # fungsi untuk mengecualikan debugging/error yaitu jika input tidak sesuai/kosong
      break #berhenti dari perulangan/looping karena input sesuai
  # AKHIRAN

  # BUAT TANGGAL KELAHIRAN
  count = 3 # variabel yang berisi int/angka untuk mendefisinikan nilai perhitungan (loop)
  while count > 0: # perulangan while dengan bernilai count
    tanggal_kelahiran = input("Masukkan Tanggal Lahir Lahir Anda (format:dd-mm-yyyy) : ") # fungsi input untuk user (format integer)
    if len(tanggal_kelahiran) == 10: # fungsi len(hitung panjang input dari variabel) jika panjang input = 10 maka bernilai True
      break # fungsi berhenti dari perulangan jika user benar menginput dengan sesuai
    else:
      print("ERROR : Masukkan Ulang Dengan Benar Sesuai Dengan Format. Gunakan tAnda '-' (strip) pada tanggal-bulan-tahun (contoh: 00-00-0000")
      count +=1 # menambahkan nilai variabel(count) yang bernilai intg jika user salah memasukkan input maka variabel (count) akan bertambah lalu akan membuat perulangan
  # AKHIRAN

  # BUAT ALAMAT
  alamat = None # Mendefinisikan nilai kosong pada variabel kosong
  while alamat != '0': # Perulangan while jika variabel nama tidak kosong
    try: # Coba buat
      alamat = input("Masukkan Alamat Lengkap Anda : ") # fungsi input untuk user (Format String)
      if alamat == "": # jika nama kosong akan keluar hasil
        print("Input yang Anda masukkan KOSONG . Harap input kembali dengan benar") 
      elif (type(int(alamat)))==int : # mendefinisikan variabel nama dengan intger(angka) jika isi input dengan angka maka akan keluar hasil 
        print("ERROR : Masukkan input dengan HURUF . Jangan Memasukkan ANGKA, SIMBOL, atau KOSONG")
    except ValueError: # Kecuali NilaiError(Value Error) jika input bersifat string/kosong maka akan tampil
      break #berhenti dari perulangan/looping karena input sesuai
  # AKHIRAN

  # BUAT SALDO AWAL
  while True: # perulangan while dengan bernilai True . Jika try bernilai False maka akan looping
    try: # Coba buat
      saldo = int(input("Masukkan Nominal Uang Yang Ingin Anda Tabung : Rp.")) # fungsi input untuk user (format integer)
      if saldo >= 100000: # Jika input saldo lebih dari 10.000 maka bersifat True
        break # Berhenti dari perulangan/looping 
      else: # Kecuali . Input saldo kurang dari 100.000 maka akan menampilkan
        print("Nominal tidak boleh kurang Rp.100000") # Tampilan Else
        continue # Fungsi untuk melanjutkan perulangan
    except ValueError: # Kecuali NilaiError(Value Error) jika input bersifat string/kosong maka akan tampil
      print("ERROR : Masukkan input dengan ANGKA . Jangan memasukkan HURUF, SIMBOL, atau KOSONG")
  # AKHIRAN



  # Fungsi DEF untuk menampilkan hasil data Informasi akun yang dibuat
  def informasi_akun():
    # Isi Fungsi def
    # DICTIONARY DATA USER
    user = { # bukaan isi Dictionary
        'nama' : nama, # isi Dictionary yang memasukkan format input dari nama
        'umur' : umurr, # isi Dictionar yang memasukkan format input dari umur
        'jenis kelamin' : jenis_kelamin, # isi Dictionary yang memasukkan format input dari jenis kelamin
        'tempat' : tempat_lahir, # isi Dictionary yang memasukkan format input dari tempat lahir
        'tanggal' : tanggal_kelahiran, # isi Dictionary yang memasukkan format input dari tanggal lahir
        'alamat' : alamat, # isi Dicionary yang memasukkan format input dari alamat
        'saldo': saldo # isi Dicrionary yang memasukkan format input dari saldo
        } # penutup isi Dictionary
    # AKHIRAN DICTIONARY
    
    # Tampilaan INFORMASI USER jika akun berhasil dibuat
    spasi() # memanggil fungsi Spasi
    print("\t\t\t  HALLO",user.get('nama') ,"AKUN BERHASIL DIBUAT") # Tampilan dengan mengambil kata kunci dari Dictionary nama
    print("\t\t\t    format biodata pengguna :") # tampilan
    print() # sebagai spasi
    print("Nama :",user.get('nama')) # Tampilan dengan mengambil kata kunci dari Dictionary nama
    print("Jenis Kelamin :",user.get('jenis kelamin')) # Tampilan dengan mengambil kata kunci dari Dictionary jenis kelamin
    print("Tempat/Tgl Lahir :",user.get('tempat'),",",user.get('tanggal')) # Tampilan dengan mengambil kata kunci dari Dictionary tempat dan tanggal lahir
    print("Alamat :",user.get('alamat')) # Tampilan dengan mengambil kata kunci dari Dictionary alamat
    print("Jumlah Saldo Tabungan Anda : Rp.",user.get('saldo')) # Tampilan dengan mengambil format input Saldo
    print() # Sebagai Spasi
    # Akhiran



  # FUNGSI UNTUK PEMBUATAN PIN & LOGIN AKUN DENGAN PIN
  def buat_pin():
    spasi() # Memanggil Fungsi Spasi untuk membuat spasi
    print("\t\t      Buat PIN Anda untuk masuk ke dalam akun")
    spasi() # Memanggil Fungsi Spasi untuk membuat spasi

    # PEMBUATAN PIN 
    while True: # perulangan while dengan bernilai True . Jika try bernilai False maka akan looping
      try: # Coba buat
        pin1 = int(input("Masukkan PIN Anda : ")) # fungsi input untuk user 
        pin_1 = str(pin1) # mendefinisikan nilai umur menjadi string
        if len(pin_1) == 6: # Fungsi Len untuk menghitung karakter, jika pin1 = 6 Maka,
          break # Berhenti dari Perulangan/Looping karena input sesuai
        else: # Kecuali
          print("PIN harus 6 digit") # # Tampilan Else (Output)
          print("Periksa kembali PIN yang Anda masukkan") # Tampilan Else (Output)
          continue # Untuk melanjutkan perulangan
      except ValueError:  # Kecuali NilaiError(Value Error) jika input bersifat string/kosong maka akan tampil
        print() # Spasi
        print("ERROR : Anda Harus Membuat Ulang\nTidak boleh KOSONG atau memasukkan dengan HURUF") # Tampilan ERROR (Output)
        print() # Spasi
        buat_pin() # Memanggil kembali Fungsi buat_pin jika terjadi Error

    # PIN KE2 UNTUK MENGKONFIRMASI
    while True: # perulangan while dengan bernilai True . Jika try bernilai False maka akan looping
      try: # Coba buat
        pin2 = int(input("Masukkan PIN sekali lagi untuk mengkonfirmasi: ")) # fungsi input untuk user
        break # Berhenti dari Perulangan/Looping
      except ValueError: # # Kecuali NilaiError(Value Error) jika input bersifat string maka akan tampil
        print() # Spasi
        print("ERROR : Anda Harus Membuat Ulang\nTidak boleh KOSONG atau memasukkan dengan HURUF") # Tampilan ERROR (Output)
        print() # Spasi
        buat_pin() # Memanggil kembali Fungsi buat_pin jika terjadi Error
  # AKHIRAN PEMBUATAN PIN  

  # Setelah selesai membuat PIN dengan benar
  # Maka akan masuk ke LOGIN
  # LOGIN
    if pin2 == pin1: # Jika pin1 dan pin2 sinkron(sama)
      spasi() # Memanggil Fungsi Spasi untuk membuat spasi
      print("\t\t\t\tPIN Berhasil Dibuat") # Tampilan Jika PIN-1 Sinkron(sama)dengan PIN-2
      spasi() # Memanggil Fungsi Spasi untuk membuat spasi
      print("Apakah Anda Ingin Masuk ke AKUN ? ") #tanya
      print("(y/t)")
      print()
      count = 3 # variabel yang berisi int/angka untuk mendefisinikan nilai perhitungan (loop)
      while count > 0:
        tanya = input(">>> ") # fungsi input untuk menjawab pertanyaan
        if tanya == 'y'or tanya == 'Y' or tanya == 'Ya' or tanya == 'YA' : # Jika user menjawab/menginput ya
          # FUNGSI LOGIN
          spasi() # Memanggil Fungsi Spasi untuk membuat spasi
          print("\t\t\t\t   MASUKKAN PIN") # Tampilan untuk input Y
          spasi() # Memanggil Fungsi Spasi untuk membuat spasi
          while True: # perulangan while dengan bernilai True . Jika try bernilai False maka akan looping
            try: # Coba buat
              login = int(input("Masukkan PIN : ")) # Fungsi Input untuk memasukkan PIN
              if login == pin2: # Jika input login sama dengan pin2(pin pembuatan) maka print
                spasi() # Memanggil Fungsi Spasi untuk membuat spasi
                print("\t\t\t\t Berhasil Masuk") # Tampilan Jika Benar
                spasi() # Memanggil Fungsi Spasi untuk membuat spasi
                informasi_akun() # Memanggil Fungsi Informasi Akun Karena PIN LOGIN dengan PIN AKUN sama
                break # Berhenti dari Perulangan/Looping

              # JIKA MAKA INPUT LOGIN PIN TIDAK SESUAI
              elif login != pin2: # JIKA MAKA INPUT LOGIN PIN TIDAK SESUAI maka akan tampil ...
                spasi() # Memanggil Fungsi Spasi untuk membuat spasi
                print("\t\t\tPIN SALAH . Harap masukkan PIN lagi") # Tampilan Jika PIN LOGIN salah
                print() 
                # MASUKKAN PIN UNTUK KE2 KALI
                login_lagi = int(input("Masukkan PIN lagi: "))
                # JIKA LOGIN KE-3 SESUAI DENGAN AKUN PIN
                if login_lagi == pin2: # Jika PIN LOGIN dengan PIN AKUN sama maka akan ...
                  spasi() # Memanggil Fungsi Spasi untuk membuat spasi
                  print("\t\t\t\t Berhasil Masuk") # Tampilan Jika Benar
                  spasi() # Memanggil Fungsi Spasi untuk membuat spasi
                  informasi_akun() # Memanggil Fungsi Informasi Akun Karena PIN LOGIN dengan PIN AKUN sama
                  break # Berhenti dari Perulangan/Looping

                # JIKA MAKA INPUT LOGIN PIN TIDAK SESUAI
                elif login_lagi != pin2: # JIKA MAKA INPUT LOGIN PIN TIDAK SESUAI
                  spasi() # Fungsi Spasi untuk membuat Spasi
                  print("\t\t      PIN SALAH . Harap masukkan PIN sekali lagi") # Tampilan jika Login AKUN tidak sama dengan PIN AKUN
                  print()
                  # MASUKKAN PIN UNTUK KE3 KALI
                  login_lagi2 = int(input("Masukkan PIN sekali lagi: "))
                  # JIKA LOGIN KE-3 SESUAI DENGAN AKUN PIN
                  if login_lagi2 == pin2: # Jika PIN LOGIN dengan PIN AKUN sama maka akan ...
                    spasi() # Memanggil Fungsi Spasi untuk membuat spasi
                    print("\t\t\t\t Berhasil Masuk") # Tampilan Jika Benar
                    spasi() # Memanggil Fungsi Spasi untuk membuat spasi
                    informasi_akun() # Memanggil Fungsi Informasi Akun Karena PIN LOGIN dengan PIN AKUN sama
                    break # Berhenti dari Perulangan/Looping
                  # JIKA MASUKKAN PIN KE-3 SALAH MAKA
                  else: # Kecuali . Jika User salah memasukkan PIN ke-3 maka akan menampilkan ...
                    spasi() # Fungsi Spasi untuk membuat Spasi
                    print("\t\t\tMaaf Anda sudah gagal masuk sebanyak 3x ") # Tampilan ELSE (OUTPUT)
                    print("\t\t\t\tAkun Anda TERBLOKIR") # Tampilan ELSE
                    tanya_user() # Memanggil Fungsi tanya_user untuk Menanyakan apabila ingin membuat akun ulang
            except ValueError: # Kecuali NilaiError(Value Error) jika input bersifat string/kosong maka akan tampil
              print()
              print("ERROR : Anda Harus Memasukan Ulang\nTidak boleh KOSONG atau memasukkan dengan HURUF") # Tampilan Error
              print()
          break # Berhenti dari Perulangan/Looping
        elif tanya == 't' or tanya == 'T' or tanya == 'Tidak' or tanya == 'TIDAK': # Jika user menjawab/menginput T maka akan kembali menanyakan user
          tanya_user() # Memanggil Fungsi Tanya User
          break # Berhenti dari Perulangan/Looping
        else: # Jika tidak ada input yang sesuai
          print("ERROR : Input yang Anda masukkan SALAH. Input ulang yang benar dengan format 'y' atau 't'") # Tampilan ERROR (Output)
          count +=1 # Perulangan

    else: # Kecuali . PIN tidak sama makan akan menampilkan ...
      print() # Spasi
      print("ERROR : PIN Anda tidak sama. Anda harus membuat PIN ulang") # Tampilan ELSE (Output)
      print() # Spasi
      buat_pin() # Memanggil fungsi buat pin kembali
# AKHIR PEMBUATAN PIN & LOGIN AKUN DENGAN PIN
  buat_pin() # Memanggil kembali fungsi Buat PIN agar fungsi Buat PIN bisa berjalan



  # FUNGSI Untuk Input User Memlih Menu
  def menu():
    # ISI DEF MENU
    print('-'*80) # Sebagai Line Tampilan
    print("\t\t\t\t MENU ATM BANK JAGO") # Tampilan
    print('-'*80) # Sebagai Line Tampilan
    spasi() # Memanggil fungsi Spasi sebagai Spasi
    saldo_akun = saldo # Memasukkan nilai saldo pada fungsi DEF buat akun ke dalam fungsi Menu dengan variabel yang berbeda
    # Saya memakai perulangan try dan except karena nilai input bersifat integer
    while True: # Jika Benar (Perulangan/looping)
      try: # Coba Buat
        print("1.Cek Saldo") # Tampilan
        print("2.Transfer Uang") # Tampilan
        print("3.Tarik Tunai") # Tampilan
        print("4.Keluar ATM") # Tampilan
        print() # Sebagai Spasi
        menu = int(input("Silahkan pilih menu : ")) # Fungsi Input Untuk Memilih Menu (format integer)
        if menu == 1: # Jika input Menu adalah 1 . Maka
          spasi() # Memanggil Fungsi Spasi sebagai Spasi
          print("Sisa Saldo Anda adalah sebesar Rp.",saldo_akun) # Tampilan dari pilihan 1 dan memanggil format dari variabel saldo_akun
          print() # Memanggil Fungsi Cek Saldo
        elif menu == 2: # Jika input Menu adalah 2 maka akan beralih ke menu transfer uang
          spasi() # Memanggil Fungsi Spasi sebagai Spasi 
          print("Untuk Mentransfer Uang Silahkan Masukkan Nomor Rekening Tujuan") # Tampilan
          norek = int(input("Masukan Nomor Rekening Tujuan : ")) # Fungsi Input untuk memasukkan Nomor Rekening tujuan (format integer)
          no_rek = str(norek) # Menjadikan variabel nomor rekening dari integer menjadi string agar bisa menggunakan fungsi len untuk menghitung panjang karakter
          print() # Sebagai Spasi
          if len(no_rek) == 10: # Jika panjang digit Nomor Rekening Tujuan sama dengan 10 digit . Maka
            spasi() # Memanggil Fungsi Spasi sebagai Spasi
            print("Nomor Rekening ditemukan, silahkan masukkan nominal yang yang akan di transfer") # Tampilan jika Nomor Rekening Tujuan berdigit 10
            print() # Sebagai Spasi
            while True: # Jika Benar (Perulangan/looping)
              try: # Coba Buat
                nominal_transfer = int(input("Nominal Yang Akan Di Transfer : Rp.")) # Fungsi Input Untuk Memasukkan Jumlah Transfer (format integer)
                if nominal_transfer <= saldo_akun : # Jika Nominal Transfer Kurang dari Jumlah Saldo yang dipunyai . Maka
                  saldo_akun = saldo_akun - nominal_transfer # Jumlah Saldo Akun dikurangi dengan Nominal Transfer
                  spasi() # Memanggil fungsi Spasi sebagai Spasi
                  print("Transfer Anda berhasil dilakukan") # Tampilan Berhasil Transaksi
                  print("Jumlah saldo Anda sekarang adalah sebesar Rp.",saldo_akun) # Tampilan dengan menamahkan dan memanggil variabel Saldo Akun yang sudah di kalkulasikan
                  print() # Sebagai Spasi
                  break # Berhenti dari perulangan karena transaksi sudah berhasil
                else: # Kecuali (yang artinya nominal transfer lebig besar dari Jumlah Saldo yang dipunyai)
                  spasi() # Memanggil Fungsi Spasi sebagai Spasi
                  print("Maaf saldo Anda tidak mencukupi") # Tampilan dari Else
                  print() # Sebagai Spasi
                  continue
              except ValueError: # Kecuali NilaiError(Value Error) jika input bersifat string/kosong maka akan tampil
                spasi() # Memanggil Fungsi Spasi sebagai Spasi
                print("ERROR : Masukkan input dengan ANGKA. Jangan memasukkan SIMBOL, HURUF, atau KOSONG") # Tampilan jika input tidak sesuai dengan format
                print() # Sebagai Spasi
          else: # Kecuali (Nomor rekening lebih dari 10 Digit) . Maka
            spasi() # Memanggil fungsi Spasi sebagai spasi
            print("ERROR : Nomor Rekening tujuan tidak ditemukan atau tidak terdaftar.") # Tampilan Else
            print("Silahkan masukkan Nomor Rekening tujuan dengan digit 10 angka tidak kurang dan tidak lebih.") # Tampilan Else
            print() # Sebagai Spasi
            continue # Sebagai melanjutkan perulangan karena tidak sesuai
        elif menu == 3: # Jika Input Menu adalah 3 . Maka
          spasi() # Memanggil fungsi Spasi sebagai Spasi
          # DICTIONARY pilihan untuk Tarik Tunai
          pilihan = { # Bukaan Dictionary
              'limapuluh' : '1. Rp.50.000', # pilihan untuk tarik tunai
              'seratus' : '2. Rp.100.000', # pilihan untuk tarik tunai
              'seratuslimapuluh' : '3. Rp.150.000', # pilihan untuk tarik tunai
              'duaratus' : '4. Rp.200.000', # pilihan untuk tarik tunai
              'lainnya' : '5. Lainnya' # pilihan untuk tarik tunai
              } # Penutup Dictionary
          while True: # Jika Benar (perulangan/looping)
            try: # Coba Buat
              print(pilihan.get('limapuluh'),"\t\t", pilihan.get('seratuslimapuluh')) # Tampilan dengan mengambil kata kunci dari Dictionary 
              print(pilihan.get('seratus'),"\t\t", pilihan.get('duaratus')) # Tampilan dengan mengambil kata kunci dari Dictionary 
              print() # Sebagai Spasi
              print(pilihan.get('lainnya')) # Tampilan dengan mengambil kata kunci dari Dictionary
              spasi() # Memanggil fungsi Spasi sebagai Spasi
              pilih = int(input(">>> ")) # Fungsi Input Untuk Memilih (format integer)
              if pilih == 1: # Jika pilihan Tarik Tunai adalah 1 . Maka
                if saldo_akun >= 50000:
                  saldo_akun = saldo_akun - 50000 # Saldo Akun dikurangi dengan 50.000 (sesuai pilihannya)
                  print() # Sebagai Spasi
                  print("Sisa saldo Anda : Rp.",saldo_akun) # Tampilan Sisa Saldo setelah melakukan Pengambilan/Penarikan Uang dan memanggil variabel saldo setelah transaksi
                  spasi() # Memanggil fungsi Spasi sebagai Spasi
                  break # Berhenti dari Perulangan/Looping
                else:
                  print()
                  print("Maaf saldo Anda tidak mencukupi")
                  spasi()
                  break
              elif pilih == 2: # Jika pilihan Tarik Tunai adalah 2 . Maka
                if saldo_akun >= 100000:
                  saldo_akun = saldo_akun - 100000 # Saldo Akun dikurangi dengan 100.000 (sesuai pilihannya)
                  print() # Sebagai Spasi
                  print("Sisa saldo Anda : Rp.",saldo_akun) # Tampilan Sisa Saldo setelah melakukan Pengambilan/Penarikan Uang dan memanggil variabel saldo setelah transaksi
                  spasi() # Memanggil fungsi Spasi sebagai Spasi
                  break # Berhenti dari Perulangan/Looping
                else:
                  print()
                  print("Maaf saldo Anda tidak mencukupi")
                  spasi()
                  break
              elif pilih == 3: # Jika pilihan Tarik Tunai adalah 3 . Maka
                if saldo_akun >= 150000:
                  saldo_akun = saldo_akun - 150000 # Saldo Akun dikurangi dengan 150.000 (sesuai pilihannya)
                  print("Sisa saldo Anda : Rp.",saldo_akun) # Tampilan Sisa Saldo setelah melakukan Pengambilan/Penarikan Uang dan memanggil variabel saldo setelah transaksi
                  print() # Sebagai Spasi 
                  spasi() # Memanggil fungsi Spasi sebagai Spasi
                  break # Berhenti dari Perulangan/Looping
                else:
                  print()
                  print("Maaf saldo Anda tidak mencukupi")
                  spasi()
                  break
              elif pilih == 4: # Jika pilihan Tarik Tunai adalah 4 . Maka
                if saldo_akun >= 200000:
                  saldo_akun = saldo_akun - 200000 # Saldo Akun dikurangi dengan 200.000 (sesuai pilihannya)
                  print() # Sebagai Spasi
                  print("Sisa saldo Anda : Rp.",saldo_akun) # Tampilan Sisa Saldo setelah melakukan Pengambilan/Penarikan Uang dan memanggil variabel saldo setelah transaksi
                  spasi() # Memanggil fungsi Spasi sebagai Spasi
                  break # Berhenti dari Perulangan/Looping
                else:
                  print()
                  print("Maaf saldo Anda tidak mencukupi")
                  spasi()
                  break
              elif pilih == 5: # Jika pilihan Tarik Tunai adalah 5 . Maka
                spasi() # Memanggil fungsi Spasi sebagai Spasi
                while True: # Jika Benar (perulangan/looping)
                  try: # Coba Buat
                    lainnya = int(input("Masukkan nominal uang yang ingin Anda tarik : Rp.")) # Fungsi Input Untuk Memasukkan Nominal Penarikan Uang (format integer)
                    if lainnya <= saldo_akun : # Jika Nominal Jumlah Tarik lebih kecil dari Jumlah Saldo . Maka
                      saldo_akun = saldo_akun - lainnya # Jumlah Saldo Akun dikurangi dengan Nominal Tarik Tunai
                      print() # Sebagai Spasi
                      print("Sisa saldo Anda : Rp.",saldo_akun) # Tampilan Sisa Saldo setelah melakukan Pengambilan/Penarikan Uang dan memanggil variabel saldo setelah transaksi
                      spasi() # Memanggil fungsi Spasi sebagai Spasi
                    else: # Kecuali (yaitu jumlah Nominal Tarik Tunai lebih besar dari Jumlah Saldo) . Maka
                      print() # Sebagai Spasi
                      print("Maaf saldo Anda tidak mencukupi") # Tampilan Else. ERROR karena Transaksi tidak bisa dilakukan
                      spasi() # Memanggil fungsi Spasi sebagai Spasi
                    break # Berhenti dari Perulangan/Looping
                  except ValueError: # Kecuali NilaiError(Value Error) jika input bersifat string/kosong maka akan tampil
                    spasi()
                    print("ERROR : Masukkan Angka bukan Huruf atau Kosong") # Tampilan jika input tidak sesuai dengan format
                    print()
                break # Berhenti dari Perulangan/Looping
              else: # Kecuali (Pilihan Tarik Tunai bukan 1,2,3,4,5) . Maka
                spasi() # Memanggil fungsi Spasi sebagai Spasi
                print("ERROR : Nomor yang Anda input tidak ada pada pilihan") # Tampilan jika input tidak sesuai dengan format
                print("Silahkan Input lagi dengan benar") # Tampilan jika input tidak sesuai dengan format
                print()
            except ValueError: # Kecuali NilaiError(Value Error) jika input bersifat string/kosong maka akan tampil
              spasi() # Memanggil fungsi Spasi sebagai Spasi
              print("ERROR : Masukkan Angka bukan Huruf atau kosong") # Tampilan jika input tidak sesuai dengan format
              print()
        elif menu == 4: # Jika Pilihan Menu adalah 4 . Maka
          spasi() # Memanggil fungsi Spasi sebagai Spasi
          print("\t\t\t TERIMAKASIH TELAH MENGGUNAKAN LAYANAN KAMI") # Tampilan Menu 4.KELUAR
          exit() # Memanggil Fungsi Keluar
        else: # Kecuali. Jika input tidak ada yang sesuai maka akan menampilkan
          spasi() # Memanggil fungsi Spasi sebagai Spasi
          print("ERROR : Pilihan tidak tersedia") # Tampilan jika input tidak sesuai dengan format
          print() # Sebagai Spasi
          continue # Fungsi untuk kembali ke variabel menu
      except ValueError: # Kecuali NilaiError(Value Error) jika input bersifat string/kosong maka akan tampil
        spasi() # Memanggil fungsi Spasi sebagai Spasi
        print("Masukkan input dengan ANGKA. Jangan memasukkan SIMBOL, HURUF, atau KOSONG") # Tampilan jika input tidak sesuai dengan format
        print() # Sebagai Spasi
        # Maka akan Mengulang kembali ke atas (try) karena nilai False akibat input bernilai string
        
  menu() # Memanggil Fungsi DEF Menu agar semua fungsi Menu bisa berjalan

tampilan_awal_bank() # Memanggil Fungsi DEF Tampilan Awal Bank agar APLIKASI bisa berjalan
