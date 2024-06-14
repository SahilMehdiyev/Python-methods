import requests
import json

api_key = '33d962541739574c973b9e1b'
api_url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/'

bozulan_doviz = input('Bozulan doviz turu: ') 
alinan_doviz = input('Alinan doviz turu: ') 
miktar = input(f'Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz: ')

sonuc = requests.get(api_url + bozulan_doviz)

sonuc_json = json.loads(sonuc.text)

# print(sonuc_json['conversion_rates'][alinan_doviz])

print('1 {0} = {1} {2}'.format(bozulan_doviz,sonuc_json['conversion_rates'][alinan_doviz],alinan_doviz))

