def counterClockwise(Angka):
    angka_baru = []
    for i in range((len(Angka) - 1), -1, -1): 
        temporary = [] ##Membuat list baru setiap perubahan i
        for j in range(len(Angka)):
            temporary.append(Angka[j][i]) ## Memasukkan nilai yang diinginkan ke dalam list temporary
        # print(temporary)
        angka_baru.append(temporary)
    return(angka_baru)

List_Awal = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print(counterClockwise(List_Awal))