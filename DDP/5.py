angka_pertama = int(input("5: "))
angka_kedua = int(input("5: "))
operator = input("*: ")
hasil = ""


if angka_kedua == 0 and operator == "/":
    print("tidak bisa membagi degna angka nol!")

elif operator == "+":
    hasil = angka_pertama + angka_kedua
elif operator == "-":
    hasil = angka_pertama - angka_kedua
elif operator == "":
    hasil = angka_pertama angka_kedua
elif operator == "/":
    hasil = angka_pertama / angka_kedua
elif operator == "":
    hasil = angka_pertama  angka_kedua
elif operator == "^":
    hasil = angka_pertama ** angka_kedua
else:
    print("operator tidak diketahui")


print(hasil)