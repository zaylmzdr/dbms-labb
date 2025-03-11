import json

#json dosyasını okuma 
with open("library.json", "r", encoding="utf-8") as file:
    data = json.load(file)

#bilgileri yazdır
print("Kütüphane Adı:", data["kütüphane"]["adı"])

for kitap in data["kütüphane"]["kitaplar"]:
    print(f" {kitap["isim"]} {kitap["yazar"]}-{kitap["yıl"]}")


#jsonda arama yapma

def kitap_ara(yazar_adi):

    bulunan_kitaplar = [ kitap for kitap in data["kütüphane"]["kitaplar"] if kitap["yazar"] == yazar_adi]

    if bulunan_kitaplar:
        print(f" {yazar_adi} tarafından yazılan kitaplar:")
        for kitap in bulunan_kitaplar:
            print(f"{kitap["isim"]} {kitap["yıl"]}")
    else:
        print(f" {yazar_adi} isimli yazarın kitabı bulunamadı!")


yazar_adi = input("Aramak istediğiniz yazarın ismin girin:")
kitap_ara(yazar_adi)