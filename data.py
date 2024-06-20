import requests
from bs4 import BeautifulSoup

url = 'https://turbo.az/'

response = requests.get(url)


if response.status_code == 200:
   
    
    soup = BeautifulSoup(response.content, 'lxml')
    
    car_list = soup.find_all('div', class_='products-i vipped featured')
    
    for car in car_list:
        
        name = car.find('div', class_='products-i__name products-i__bottom-text').get_text(strip=True)
        
        price = car.find('div', class_='products-i__price products-i__bottom-text').get_text(strip=True)
        
        description = car.find('div', class_='products-i__attributes products-i__bottom-text').get_text(strip=True)
        
        print(f'Car name: {name}')
        print(f'Price: {price}')
        print(f'Description: {description}')
        print('-' * 30)
else:
    print(f'Request failed, status code: {response.status_code}')        
        

    