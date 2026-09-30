angka1 = float(input("Masukann angka pertama:"))
operator =input("Masukan Operator (+, -, *, /):")
angka2 = float(input("Masukan angka 2:"))

if operator == "+":
    hasil = angka1 + angka2

elif operator == "-":
    hasil = angka1 - angka2

elif operator == "*":
    hasil = angka1 * angka2

elif operator == "/":
    hasil = angka1 / angka2

else:
    print("Operator tidak  ditemukan")

print("Hasil:", hasil)