#print('Hello, world!')
# print("Hayrli \"heee\" tong!")
# print("""olma,
#       gilos,
#       olcha""")
# print("bir \nikki \nuch")
# print(15//5)
# print(2**5)

# ism ='ali'
# familiya = 'valiyev'
# ism_sharf = f"{ism} {familiya}"
# print(ism_sharf.upper())
# print(ism_sharf.title()) #bosh harflar katta, qolganlari kichik
# print(ism_sharf.capitalize())
# print(ism_sharf.strip()) #boshi va oxiridagi bo'shliqni olib tashlaydi

# ism = input("Ismingiz nima? ")
# print("Salom, " + ism.title() + "!")
# a=20
# b=5.5
# temp=36.6
# print(type(b))

# PI = 3.14159 #o'zgarmas qiymat 
# t_yil = int(input("Tug'ilgan yilingizni kiriting: "))
# yosh = 2026 - t_yil
# print(f"Siz {yosh} yoshdasiz.")

# mevalar = ['olma', 'olcha', 'gilos', 'shaftoli', 'nok', 'anjir', 'behi', 'o\'rik']
# print(mevalar[0])
# mevalar[0]='uzum'
# mevalar.append('tarvuz')
# print(mevalar)
# mevalar.insert(1,'qovun')
# print(mevalar)
# del mevalar[2]
# print(mevalar)
# mevalar.remove('uzum')
# print(mevalar)
# mahsulot = mevalar.pop(1)
# print(mahsulot)
# print(mevalar)
# mevalar.pop() #oxirgi elementni o'chiradi

# mevalar.sort() #alfavit tartibida saralaydi
# print(mevalar)
# mevalar.sort(reverse=True) #teskari tartibda saralaydi
# print(mevalar)

# print(sorted(mevalar)) #mevalar ro'yxatini o'zgartirmasdan, alifbo tartibida saralaydi

# sonlar = [10, 5, 3, 8, 2,-1]
# sonlar.sort()
# print(sonlar)
# sonlar.sort(reverse=True)
# print(sonlar)

# mevalar.reverse() #ro'yxatni teskari tartibda chiqaradi
# print(mevalar)
# print(len(sonlar)) #ro'yxatdagi elementlar soni

# sonlar = list(range(0, 21)) # 0 dan 20 gacha bo'lgan sonlar
# print(sonlar)

# toq_sonlar = list(range(1,20,2)) # 1 dan 20 gacha bo'lgan toq sonlar
# print(toq_sonlar)
# juft_sonlar = list(range(0,20,2)) # 0 dan 20 gacha bo'lgan juft sonlar
# print(juft_sonlar)

# max_qiymat = max(sonlar)
# min_qiymat = min(sonlar)
# print(max_qiymat)
# print(min_qiymat)
# print(sum(sonlar))

# print(mevalar[0:3]) # ikki indeks orasidagi elementlarni chiqaradi
# print(mevalar[:4]) # 0 dan 3 indeksgacha bo'lgan elementlarni chiqaradi
# print(mevalar[4:]) # 4 indeksdan oxirigacha bo'lgan elementlarni chiqaradi
# print(mevalar[-3:]) # oxirgi 3 elementni chiqaradi
# print(mevalar[:-3]) # oxirgi 3 elementdan oldingi elementlarni chiqaradi            

# cars = ['bmw', 'damas', 'nexia', 'mers', 'audi', 'volvo', 'ferrari', 'lamborghini', 'porsche', 'tesla']
# my_cars = cars #nusxa olish emas, ro'yxatga yangi nom berish
# my_cars = cars[:] #ro'yxatni kesish orqali nusxa olish
# print(my_cars)

# my_cars.remove('damas')
# print(my_cars)

# my_cars[0] = 'tico'
# print(my_cars)
# print(cars)


# toys = ('car', 'doll', 'ball', 'puzzle',) #o'zgarmas ro'yxat    
# print(toys[3])

# toys = list(toys)
# toys.append('lego')
# toys = tuple(toys)
# print(toys)

# mehmonlar = {'Ali', 'Vali', 'Hasan', 'Husan'}
# for mehmon in mehmonlar:
#     print("salom ", mehmon)

# sonlar = list(range(1,11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng")

# sonlar = list(range(11))
# sonlar_kvadratlar = []
# for son in sonlar:
#     sonlar_kvadratlar.append(son**2)
# print(sonlar_kvadratlar)

# dostlar =[]
# for n in range(5):
#     dostlar.append(input(f'{n+1}-do\'stingizning ismini kiriting: '))
# print(dostlar)


# avtolar = ['audi', 'bmw', 'toyota', 'honda', 'nissan']
# for avto in avtolar:
#     if avto == 'bmw':
#         print(avto.upper())
#     else:
#         print(avto.title())


# ism = input("Ismingiz nima? ")
# if ism.lower() == 'ali':
#     print('Salom Ali!')
# else:    print(f"salom {ism.title()}!")


# yosh = int(input('yoshingizni kiritng: '))
# if yosh <=65: print('Siz pensiyaga chiqmagansiz')

# x, y = 25, 50
# print('x>y') if x>y else print('x<y')
  

# yosh = int(input('yoshingiz nechida? '))
# if yosh <= 4:
#     print('Sizga kirish bepul!')
# elif yosh <= 12:
#     print('Sizga kirish 5000 so\'m!')
# elif yosh <= 18:
#     print('Sizga kirish 8000 so\'m!')
# else:    print('Sizga kirish 10000 so\'m!')
 

# menu = ['osh', 'shashlik', 'somsa', 'lag\'mon', 'manti']
# ovqat = input('Nima ovqat yeysiz? ')
# if ovqat.lower()  in menu: # not in ni ishlatib, menyuda yo'qmi tekshirish mumkin
#     print("Buyurtmangiz qabul qilindi")
# else:    print("Kechirasiz, bizda yo\'q!")


menu = ['qozon kabob', 'shashlik', 'somsa', 'lag\'mon', 'manti']
buyurtmalar = ['shashlik', 'somsa', 'manti', 'osh']
if buyurtmalar: # ro'yxatda element bor yoki yo'qligini tekshirish
    print("Buyurtmalar qabul qilindi")      
    for buyurtma in buyurtmalar:
        if buyurtma in menu:
            print(f"menuda {buyurtma} bor")
        else: 
            print(f"menuda {buyurtma} yo\'q")
else:
    print('savatcha bo\'sh!')