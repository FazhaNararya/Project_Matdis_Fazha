# Fungsi untuk Memvalidasikan ISBN yang digitnya ada 10
def validate_isbn10(isbn):
    isbn = isbn.replace('-', '').replace(' ', '') 
    if len(isbn) != 10:
        return False

    total = 0
    for i in range(9):
        total += (10 - i) * int(isbn[i])

    # Digit terakhir bisa berupa angka atau 'X'
    if isbn[9].upper() == 'X':
        total += 10
    else:
        total += int(isbn[9])

    return total % 11 == 0

# Fungsi untuk Memvalidasikan  ISBN yang digitnya ada 13
def validate_isbn13(isbn):
    isbn = isbn.replace('-', '').replace(' ', '') 
    if len(isbn) != 13:
        return False

    total = 0
    for i in range(12):
        multiplier = 1 if i % 2 == 0 else 3
        total += multiplier * int(isbn[i])

    check_digit = (10 - (total % 10)) % 10
    return check_digit == int(isbn[12])

#Codingan utama
if __name__ == "__main__":
    print("Hallo Programmer Selamat Datang diValidasi ISBN 10 atau 13 Digit")
   
    isbn = input("Silahkan Masukkan Digit ISBN mu: ")

    if len(isbn.replace('-', '').replace(' ', '')) == 10:
        if validate_isbn10(isbn):
            print("ISBN dengan 10 Digit valid.")
        else:
            print("ISBN dengan 10 Digit valid.")

    elif len(isbn.replace('-', '').replace(' ', '')) == 13:
        if validate_isbn13(isbn):
            print("ISBN dengan 13 Digit valid.")
        else:
            print("ISBN dengan 13 Digit tidak valid.")

    else:
        print("Panjang ISBN mu tidak valid.ISBN mu Harus 10 atau 13 Digit.")
