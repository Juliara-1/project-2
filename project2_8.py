a, b=float(input()), float(input())
s=0.5*a*b
print(float(s))


s, v1, v2=float(input()), float(input()), float(input())
v=v1+v2
t=s/v
print(float(t))



n=float(input())
if n!=0:
    print(n**-1)
else: 
    print('Обратного числа не существует')


n=float(input())
t=5/9*(n-32)
print(t)



n=float(input())
if 0<n<=2:
    print(n*10.5)
elif n>2:
    print((2*10.5)+n*4-8)



n=float(input())
n1=n*10%10//1
print(int(n1))


n=float(input())
n1=n%1
print(n1)



a, b, c, d, e=int(input()), int(input()), int(input()), int(input()), int(input())
min1=min(a, b, c, d, e)
max1=max(a, b, c, d, e)
print('Наименьшее число =', min1)
print('Наибольшее число =', max1)



a, b, c=int(input()), int(input()), int(input())
max1=max(a, b, c)
min1=min(a, b, c)
s=(a+b+c)-(max1+min1)
print(max1)
print(s)
print(min1)



n=int(input())
a1=n//100
b1=n//10%10
c1=n//1%10
max1=max(a1, b1, c1)
min1=min(a1, b1, c1)
if max1-min1==a1 or max1-min1==b1 or max1-min1==c1:
    print('Число интересное')
else:
    print('Число неинтересное')


a1, a2, a3, a4, a5=float(input()), float(input()), float(input()), float(input()), float(input())
b1=abs(a1)
b2=abs(a2)
b3=abs(a3)
b4=abs(a4)
b5=abs(a5)
print(b1+b2+b3+b4+b5)


p1, p2 = int(input()), int(input())
q1, q2 = int(input()), int(input())

print(abs(p1-q1)+abs(p2-q2))