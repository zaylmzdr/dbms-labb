import xml.etree.ElementTree as ET

# xml dosyasını okuma dom kullanımı

tree = ET.parse("library.xml")
root = tree.getroot()

#kitap bilgilerini yazdırma 

print("kütüphane kitap bilgisi: ")
for kitap in root.findall("Kitap"):
    baslık = kitap.find("Başlık").text
    yazar = kitap.find("Yazar").text
    yıl = kitap.find("Yıl").text
    print(f'{baslık} , {yıl} - {yazar}')
    