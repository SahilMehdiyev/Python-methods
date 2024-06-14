
# def usalma(number):
    
#     def inner(power):
#         return number ** power
    
#     return inner

# two = usalma(2)
# three = usalma(3)
# print(two(3))
# print(three(4))


# def yetki_sorgula(page):
    
#     def inner(role):
#         if role == 'Admin':
#             return '{0} rolu {1} sayfasina ulasabilir'.format(role,page)
#         else:
#             return '{0} rolu {1} sayfasina ulasamaz'.format(role,page)
#     return inner

# user1 = yetki_sorgula('Product Edit')
# print(user1('Admin'))
# print(user1('User'))
        
        


def islem(islem_adi):
    
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam
    
    def carpma(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return carpim
    
    
    if islem_adi == 'toplama':
        return toplam
    else:
        return carpma
    
    
toplama = islem('toplama')    
carpma = islem('carpma')

print(carpma(1,3,4,6))
print(toplama(1,2,3,5,7))             
            
        