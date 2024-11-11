kalimat = str(input("Masukan Kalimat ="))
vokal = 'aiueoAIUEO'
jumlah_vokal = str(sum(1 for char in kalimat if char in vokal))

print("Jumlah huruf vokal =" +jumlah_vokal)
#penjelasan
#codingan ini untuk menghitung hurup vokal
