c = int(input("masukan suhu dalam celcius yang akan dikonversi :"))
k = int(input("masukkan suhu dalam kelvin yang akan dikonversi :"))
f =int(input("masukkan suhu dalam fahrenheit yang akan dikonversi :"))
f = c * 9/5 + 32
c =f * 5/9 - 32
c2 = k - 273

opsi =int(input("Merubah suhu ?\nTekan 1 jika mencari celcius dari farenheit : 2\nTekan 2 jika mencari farenheit : 3\nTekan 3 jika mencari celcius dari kelvin :"))

if opsi == 1 :
    print("Suhu celcius :",c)
elif opsi == 2 :
    print("Suhu farenheit :",f)
elif opsi == 3 :
    print("Suhu celcius :",c2)
else:
    print("Pilihan yang disediakan hanya ada 1,2,atau 3")