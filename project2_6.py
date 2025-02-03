num = int(input())

last_digit = num % 10    # последняя цифра числа  7
first_digit = num // 10  # первая цифра числ

if last_digit == first_digit:
    print('ДА')  
else:
    print('НЕТ')


a=int(input())
n=a%2
if n==0:
    print('Четное')
else:
    print('Нечетное')




a, b, c, d=int(input()), int(input()), int(input()), int(input()) 
if a<b:
    min_ab=a
else:
    min_ab=b
if c<d:
    min_cd=c
else:
    min_cd=d  
if min_ab<min_cd:
    print(min_ab)
else:
    print(min_cd)



    a=int(input())
if a<=13:
    print('детство')
if 14<=a<=24:
    print('молодость')
if 25<=a<=59:
    print('зрелость')
if a>=60:
    print('старость')



a, b, c=int(input()), int(input()), int(input())
sum=0
if a>=0:
    sum=sum+a
if b>=0:
    sum=sum+b
if c>=0:
    sum=sum+c
print(sum)


a = int(input())

if a >= 2 and a <= 17:
    b = 3
    p = a * a + b * b
else:
    b = 5

p = (a + b) * (a + b)
print(p)



x=int(input())
if -1<=x<=17:
    print('Принадлежит')
else:
    print('Не принадлежит')


x=int(input())
if -3<x<7:
    print('Не принадлежит')
else:
    print('Принадлежит')



n=int(input())
if 999<n<9999 and ((n%17==0) or (n%7==0)):
    print('YES')
else:
    print('NO')



a, b, c=int(input()), int(input()), int(input())
if (a+b>c) and (a+c>b) and (b+c>a):
    print('YES')
else:
    print('NO')


n=int(input())
if n%4==0 and n%100>=1 or n%400==0:  
    print('YES')
else:
    print('NO')


x1, y1, x2, y2=int(input()), int(input()), int(input()), int(input())
if x1==x2 or y1==y2:
    print('YES')
else:
    print('NO')

x1, y1, x2, y2=int(input()), int(input()), int(input()), int(input())
if (x1+1==x2 or x1-1==x2) and (y1+1==y2 or y1-1==y2):
    print('YES')
else:
    print('NO')



a, b, c, d = int(input()), int(input()), int(input()), int(input())
if (-1 <= a - c <= 1) and (-1 <= b - d <= 1):
    print('YES')
else:
    print('NO')



