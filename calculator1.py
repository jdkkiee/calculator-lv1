while True:

    print("\n=== KALKULATOR ===")
    print("1. Hitung")
    print("2. Keluar")

    pilihan = input("Pilih: ")

    if pilihan == "2":
        print("Program selesai.")
        break

    elif pilihan == "1":

        angka1 = float(input("Masukkan angka pertama: "))
        operator = input("Masukkan operator (+, -, *, /): ")
        angka2 = float(input("Masukkan angka kedua: "))

        if operator == "+":
            hasil = angka1 + angka2

        elif operator == "-":
            hasil = angka1 - angka2

        elif operator == "*":
            hasil = angka1 * angka2

        elif operator == "/":
            hasil = angka1 / angka2

        else:
            hasil = "Operator tidak valid"

        print("Hasil:", hasil)

    else:
        print("Pilihan tidak valid.")