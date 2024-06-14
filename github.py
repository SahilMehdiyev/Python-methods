import requests

class Github:
    
    def __init__(self):
        self.api_url = 'https://api.github.com/'
        
    def getUser(self,username):
        response = requests.get(self.api_url+'/users/'+username)
        return response.json()
    
    def getRepository(self,username):
        response = requests.get(self.api_url+'/users/'+username+'/repos/')
        return response.json()
        
github = Github()
        

while True:
    secim = input('1- Find User\n2- Get Repository\n3-Create Repository\n4-Exit\n Secim: \n')
    
    if secim == '4':
        break
    
    else:
        if secim == '1':
            username = input('Username: ')
            result = github.getUser(username)
            print(f" name: {result['name']} public repos: {result['public_repos']} follower: {result['followers']}")
            
        elif secim == '2':
            username = input('username: ')
            result = github.getRepository(username)
            for repo in result:
                print(repo['name'])
            
        elif secim == '3':
            pass
        else:
            print('Yanlis secim')
        
    
    