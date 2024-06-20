# import requests
# import json

# api_key = '33d962541739574c973b9e1b'
# api_url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/'

# bozulan_doviz = input('Bozulan doviz turu: ') 
# alinan_doviz = input('Alinan doviz turu: ') 
# miktar = input(f'Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz: ')

# sonuc = requests.get(api_url + bozulan_doviz)

# sonuc_json = json.loads(sonuc.text)

# # print(sonuc_json['conversion_rates'][alinan_doviz])

# print('1 {0} = {1} {2}'.format(bozulan_doviz,sonuc_json['conversion_rates'][alinan_doviz],alinan_doviz))


# Web Scraper

# import requests
# from bs4 import BeautifulSoup

# # Veri toplanacak web sayfasının URL'si
# url = 'https://www.example.com'

# response = requests.get(url)

# soup = BeautifulSoup(response.text, 'html.parser')

# basliklar = soup.find_all('h1')

# for baslik in basliklar:
#     print(baslik.text)

import requests
from bs4 import BeautifulSoup

# Web sayfasına istek gönderin
url = "http://sahilmehdiyev.com.tr"  # İstediğiniz web sayfasının URL'sini buraya yazın
response = requests.get(url)

# İstek başarılı oldu mu kontrol edin
if response.status_code == 200:
    # HTML içeriğini ayrıştırın
    soup = BeautifulSoup(response.content, 'lxml')
    
    # Sayfadaki tüm metinleri alın
    page_text = soup.get_text()
    
    # Hedef kelimeyi arayın
    target_word = "sahil"  # Aradığınız kelimeyi buraya yazın
    if target_word in page_text:
        print(f"'{target_word}' kelimesi sayfada bulundu.")
    else:
        print(f"'{target_word}' kelimesi sayfada bulunamadı.")
else:
    print(f"İstek başarısız oldu, durum kodu: {response.status_code}")

# Ekstra: Hedef kelimeyi içeren metinleri bulma
texts_containing_word = [sentence for sentence in page_text.split() if target_word in sentence]
print(f"'{target_word}' kelimesini içeren metinler: {texts_containing_word}")


