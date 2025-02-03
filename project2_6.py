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