# Minpro_DDP_2
# membuat web untuk jasa sewa server

## 1. Flowchart


### ![Flowchart_Minpro2(Revisi) drawio](https://github.com/user-attachments/assets/7c390df9-7d47-422e-88f4-f3bb97b4a484)



pada flowchart saya pertama-tama saya mulai dengan kata MULAI
lalu user akan memilih role, mau login sebagai admin atau user
untuk username dan password pastinya akan berbeda.


### A. Role User



Saat user memilih untuk menjadi user maka program akan meminta
untuk memasukkan username dan password, jika username dan password
salah, maka akan kembali ke halaman login di awal, namun jika username
dan password benar, user akan mendapatkan output sambutan dan akan 
ada output tabel untuk memilih-milih hosting.



Saat user akan memilih hosting yang akan dibeli, maka user harus
mengisi bagian input, input tersebut hanya bisa menginput angka 1 - 5
jika user menginput angka lebih dari 5, maka akan kembali ke halaman
login, namun jika user memilih angka 1 sampai ataupun 5, maka user
akan lanjut ke halaman pembelian.



Saat user sudah berada pada halaman pembelian, maka user akan
diminta untuk memastikan kembali pilihannya, jika pilihan user
salah/tidak benar, maka user akan kembali ke halaman login dan jika
oilihan user benar, makaa user akan disuruh untuk menginput Nama, Email
dan juga Domain yang user inginkan (Free domain setiap pembelian
Hosting, gacor...), setelah user menginput semua data, user akan
diminta untuk memastikan kembali, apakah semua data yang diinput
benar atau tidak, jika tidak, maka user akan mendapatkan peringatan
untuk mengisi data diri dengan benar, dan kembali ke halaman login
jika user memilih benar, maka user akan mendapatkan output "Selamat
web anda telah berhasil terbuat, terimakasih telah mempercayai kami!".



### B. Role Admin



Pada saat user memilih menggunakan role admin, maka user harus
memasukkan username dan password yang benar, jika salah maka
user akan mengulang kembali ke halaman login, namun jika user
benar, maka user akan mendapatkan output "Selamat datang atmint
login berhasil, silahkan pilih menu." pada saat login user admin
akan mendapatkan menu dan user admin dapat memilih pilihan yang 
ada dalam menu.



jika user memilih pilihan 1, yaitu tambah paket, maka user admin
dapat memasukkan nama dari paket hosting, jangka waktu hosting
dan harga hosting, setelah menentukan semuanya, maka akan di
cek ulang oleh program, apakah input sesuai dengan tipe data
yang diminta, jika tidak sesauai, maka akan kembali ke halaman
login, namun jika sesuai maka paket hosting akan tertambahkan
ke menu admin.



jika user memilih pilihan 2, yaitu tampilkan paket, pada menu ini
terkesab simpel, karena program hanya akan menunjukan paket paket
hosting yang ada di program.




jika user memilih pilihan 3, yaitu update paket, pada menu ini
user akan mendapatkan output menu paket, dan disuruh memilih
paket mana yang akan diupdate, jika sudah memilih, maka user
akan menginiput nama paket yang baru, setelah itu maka user
akan mendapatkan output bahwasannya paket yang lama telah diganti
dengan paket yang baru.




jika user memilih pilihan 4, yaitu delete paket, menu ini user
bisa menghapus paket yang ada di menu, pertama user akan mendapatkan
output dari menu, dan akan memilih untuk memasukkan nomor mana yang
mau dihapus, setelah itu maka user admin akan mendapatkan output
"paket (nama paket) telah dihapus".




jika user memilih pilihan 5, yaitu keluar, menu ini sangat super
duper simpel, saat user admin memilih ini, maka pemrograman akan
berhenti.




### C. Portal pada flowchart



dapat dilihat pada flowchar ada 4 warna potal diantaranya adalah


**1. Warna merah**


   Warna merah sendiri merujuk pada portal yang akan membawa
program kembali ke halaman login diawal.




**2. Warna Hijau**


   Warna Hijau sendiri adalah portal untuk menuju sebuah output
"Mohon isi data diri anda dengan benar." dan outputnya akan
menuju ke portal merah yang akan kembali ke halaman login di awal



 **3. Warna biru tua**


   Warna biru muda sendiri adalah portal untuk menuju
output akhir saat user berhasil membeli sebuah hosting
dan portal ini adalah portal menuju selesainya program.



**4. Warna ungu**


   Warna ungu adalah warna yang digunakan untuk
menuju ke program Selesai tanpa ada output.



---

## 2. Program Coding



### A. Function 


ada 5 fuction yang saya gunakan pada kode saya diantaranya adalah



**1. tampilPaket**


![Screenshot 2024-10-14 223534](https://github.com/user-attachments/assets/809bc286-5ac0-45f7-943e-6549eec2d775)



pada kode tampilPaket adalah salah satu function untuk CRUD admin, untuk variabel nomor adalah
variabel yang meruju pada index, dimana index akan dimulai dari anka 1, bukan 0 dan variabel paket
digunakan sebagai pematok atau patokan untuk table field atau penamaan dari isi tabel.



**2. khususAtmint**


![Screenshot 2024-10-14 224048](https://github.com/user-attachments/assets/c17b0a4c-1234-44b3-84f4-384ace7b170d)



function yang berfungsi sebagai tempat untuk memunculkan menu yang akan dilihat oleh
admin, return berfungsi untuk mengembalikan nilai yang akan dipilih admin nantinya


**3. tambahPaket**


![Screenshot 2024-10-14 224217](https://github.com/user-attachments/assets/46111049-377a-40e7-beb6-c448e5daddf3)




function yang berfungsi untuk CRUD admin yaitu create, berfungsi untuk menambahkan paket, paket
ditambahkan dengan cara menggunakan .append


**4. updatePaket**


![Screenshot 2024-10-14 224724](https://github.com/user-attachments/assets/da3900ef-7576-4027-ba5a-4da27e0fe497)



function ini juga merupakan salah satu function yang digunakan untuk CRUD, - 1 pada akhir
variabel nomor digunakan sebagai pengurangan, yaitu saat ada yang ingin diganti, maka nilainya akan berkurang
dan variabel nomor yang digunakan adalah dari variabel nomor yang digunakan sebelumnya sebagai pengganti
index.


**5. deletePaket**


![Screenshot 2024-10-14 225209](https://github.com/user-attachments/assets/db3a0aad-9c70-4b01-a7d2-2359e68f60be)



function ini digunakan untuk menghapus paket yang ada dalam paketHosting, untuk menghapus
paket pada function ini saya menggunakan .pop.





### B. Program role user 


jdisja
