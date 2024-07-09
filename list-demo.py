
#1- bmw, mercedes, opel, mazda elemanlarına ait bir liste oluştur.
cars = ['bmw', 'mercedes', 'opel', 'mazda']
#2- liste kaç elemanlı
result = len(cars)
#listenin ilk ve son elemanları
result = cars[0]
result = cars[-1]
# mazda değerini toyoto ile değiştirir
cars[-1] = "toyota"
result = cars
# merecedes listenin bir elemanı  mı?
result = "merecedes" in cars
result = "mercedes" in cars
#listenin -2 indeksindeki değer nedir?
result = cars[-2]
#listenin ilk üç elemanını alın
result = cars[0:3]
result = cars[:0]
result = cars[:1]
result = cars[:2]
#listenin son 2 elemanı yerine toyota ve renult değerlerini ekleyin
cars[-2:] = ["toyota","renult"]
result = cars
#listeye audi ekleyin
reult = cars + ["audi"]
#listenin son elemanını silin
del cars [-1]
result = cars
result = cars[::-1]



#yeni liste
    #StudentA : Yaren Bilgi 2012, (70,60,70)
studentA = ["yaren", "bilgi", 2010, [70,60,70]]
    #studentB : İsa Turan 1999, (80,80,70)
studentB = ["isa","turan",1999,[80,80,70]]
    #studentC : Kerem Yılmaz 1998, (80,70,90)
studentC = ["kerem","yılmaz",1998,[80,70,90]]


result = studentA[0]
result = studentB[1]
result = studentC[2]
result = f"{studentA[0]} {studentA[1]} {2019-studentA[2]}yaren bilgi 9 yaşında ve not ortalaması 66 {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}"

print(result)
