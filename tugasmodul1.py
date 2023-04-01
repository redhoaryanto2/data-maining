def jumlahkarakter():
    nama = input('masukkan nama :')
    hitung = 0
    for jumlah in nama:
        if jumlah !=' ':
            hitung +=1
    print ('jumlah karakter nama :',hitung)

    nim = input ('\nmasukkan NIM:')
    hitung = 0 
    for jumlah in nim:
        if jumlah !=' ':
            hitung += 1
    print('jumlah karakter nama :', hitung)

jumlahkarakter()