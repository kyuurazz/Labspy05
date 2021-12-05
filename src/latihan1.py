## Tabel
def garis():
    print(52*"=")

Daftar_Nomor = {'Ari':'081267888', 'Dina':'087677776'}
print()
garis()
print("| {0:^20} | {1:^25} |".format("Nama", "Nomor Telepon"))
garis()
for data in Daftar_Nomor.items():
    print(f"| {data[0]:<20} | {data[1]:<25} |")
garis()
print()

## Tampilkan kontaknya Ari
print("Kontak Ari:", Daftar_Nomor['Ari'])

## Tambah kontak baru dengan nama Riko, nomor 087654544
Daftar_Nomor['Riko'] = "087654544"

## Ubah kontak Dina dengan nomor baru 088999776 
Daftar_Nomor['Dina'] = "088999776"

## Tampilkan semua Nama
print(Daftar_Nomor.keys())

## Tampilkan semua Nomor
print(Daftar_Nomor.values())

## Tampilkan daftar Nama dan nomornya
print(Daftar_Nomor.items())

## Hapus kontak Dina
del Daftar_Nomor['Dina']
print(Daftar_Nomor)
print()