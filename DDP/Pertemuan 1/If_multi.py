nama = "Lin"
mapel = "ddp"
nilai = 90

if(nilai >= 85 and nilai <= 100):
    grade = "A"
elif(nilai >= 75 and nilai < 85):
    grade = "B"
else:
    grade = "C"

print(f"Nama \t\t: {nama}")
print(f"Mata kuliah \t: {mapel}")
print(f"Nilai \t\t: {nilai}")
print(f"Grade \t\t: {grade}")