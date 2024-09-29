import time
import random

# Kodunuzu buraya yazınız
OyuncuPuani = 0
BilgisayarPuani = 0

while True:
    secenek = input("Taş mı Kağıt mı Makas mı?")
    #Eger kullanici tas "VEYA" kagit "VEYA" makas derse:
    if secenek == "Taş" or secenek == "Kağıt" or secenek == "Makas":
        bilgisayar_hamlesi = random.randint(1, 3)
        if bilgisayar_hamlesi == 1:
            bilgisayar_hamlesi = "Taş"
        elif bilgisayar_hamlesi == 2:
            bilgisayar_hamlesi = "Kağıt"
        else:
            bilgisayar_hamlesi = "Makas"

        if secenek == bilgisayar_hamlesi:
            print("Beraberlik")

        elif secenek == "Taş" and bilgisayar_hamlesi == "Makas":
            OyuncuPuani += 1
            print("Oyuncu kazandı!")

        elif secenek == "Makas" and bilgisayar_hamlesi == "Kağıt":
            OyuncuPuani += 1
            print("Oyuncu kazandı!")

        elif secenek == "Kağıt" and bilgisayar_hamlesi == "Taş":
            OyuncuPuani += 1
            print("Oyuncu kazandı!")

        else:
            BilgisayarPuani += 1
            print("Bilgisayar kazandı!")
            

        print("Bilgisayar puanı:", BilgisayarPuani)
        print("Oyuncu puanı:", OyuncuPuani)
        
        time.sleep(3)
    else:
        print("Bir daha seçiniz")
        
