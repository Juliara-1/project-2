n,k=int(input()), int(input())
if n<k:
    print('YES')
elif n>k:
    print('NO')
elif n==k:
    print("Don't know")



a, b, c=int(input()), int(input()), int(input())
if a==b==c:
    print('Равносторонний')
elif a==b or b==c or a==c:
    print('Равнобедренный')
elif a!=b or b!=c or a!=c:
    print('Разносторонний')




a, b, c=int(input()), int(input()), int(input())
if a<b<c or c<b<a:
    print(b)
elif b<a<c or c<a<b:
    print(a)
elif a<c<b or b<c<a:
    print(c)




n=int(input())
if n==2:
    print('28')
elif n==4 or n==6 or n==9 or n==11:
    print('30')
else:
    print('31')



n=int(input())
if n<60:
    print('Легкий вес')
elif 60<=n<64:
    print('Первый полусредний вес')
elif 64<=n<69:
    print('Полусредний вес')


a, b = int(input()), int(input())
c = input()  # Получаем операцию как строку

# Проверяем операцию и выполняем соответствующее действие
if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '/':
    if b != 0:  # Проверяем деление на ноль
        print(a / b)
    else:
        print('На ноль делить нельзя!')
else:
    print('Неверная операция')




    a, b=input(), input()
if (a=='красный' and b=='синий') or (b=='красный' and a=='синий'):   print('фиолетовый')
elif (a=='красный' and b=='красный'):   print('красный')
elif (a=='красный' and b=='желтый') or (b=='красный' and a=='желтый'):   print('оранжевый')
elif (a=='желтый' and b=='желтый'):   print('желтый')
elif (a=='синий' and b=='желтый') or (b=='желтый' and a=='синий'):   print('зеленый')
elif (a == 'синий' or a == 'красный' or a == 'желтый') and a == b:  print(a)
else:   print('ошибка цвета')



n=int(input())
if 1<=n<=10 and n%2!=0:
    print('красный')
elif 1<=n<=10 and n%2==0:   
    print('черный')  
elif n==0:
    print('зеленый') 
elif 11<=n<=18 and n%2!=0:
    print('черный')
elif 11<=n<=18 and n%2==0:
    print('красный')  
elif 19<=n<=28 and n%2!=0:
    print('красный')
elif 19<=n<=28 and n%2==0:
    print('черный')  
if 29<=n<=36 and n%2!=0:
    print('черный')
if 29<=n<=36 and n%2==0:
    print('красный')  
elif n>36 or n<0:
    print('ошибка ввода') 


a1, b1, a2, b2=int(input()), int(input()), int(input()), int(input())
if a2<b1 or a1<b2:
    print(a2, b1)
elif a2==b1 or a1==a2:
    print(a2)
elif b2==b1 or a1==b2
    print(b2)
elif (a2!=b1 and a2>b1) or (a1<a2 and b1<b2) or (a1>a2 and b1>b2):
    print('пустое множество')



n=int(input())
if n//100>0 and n%10==0 and n%100==0:
    print('YES')
else:
    print('NO')


    x1, y1, x2, y2=int(input()), int(input()), int(input()), int(input()) 
if (x1+x2+y1+y2)%2==0:
    print('YES')
else:
    print('NO')



n, a= int(input()), input()
if 10<=n<=15 and a=='f':
    print('YES')
else:
    print('NO')



    n= int(input())
if n%2>0 or (6<=n<=20 and n%2==0):
    print('YES')
else:
    print('NO')



if x1==4 and y1==4 or x2==4 and y2==4:
    print('YES')
else:
    print('NO')


x1, y1, x2, y2=int(input()), int(input()), int(input()), int(input())
min=x1-x2
if min<0:
   min=min*(-1)
min2=y1-y2
if min2<0:
   min2=min2*(-1)
if min == min2:
    print('YES')
else:
    print('NO')





# Получаем координаты двух клеток
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

# Вычисляем разницы координат
dx = x1 - x2
dy = y1 - y2

# Делаем разницы положительными
if dx < 0:
    dx = dx * (-1)
if dy < 0:
    dy = dy * (-1)

# Проверяем ход ферзя:
# 1. По диагонали (dx == dy)
# 2. По горизонтали (dx == 0)
# 3. По вертикали (dy == 0)
if dx == dy or dx == 0 or dy == 0:
    print('YES')
else:
    print('NO')