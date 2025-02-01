print("Hello, World!")
print("Hello, World!")
print("Hello, World!")
print("Hello, World!")
print("Hello, World!")
print("Hello, World!")
print("Hello, World!")
print("Hello, World!")


a = 82 // 3**2 % 7
print(a)

b1, q, n=int(input()), int(input()), int(input()),
bn=b1*(q**(n-1))
print(bn)

sh, m=int(input()),int(input())
print(m//sh, m%sh, sep='\n')




n=int(input())
print(n, 'мин - это', n//60, 'час',n%60, 'минут.')

a=int(input())
b=a//4
print(-b)

n=int(input())
a=n//100 #1 число
b=(n//10)%10 #2 число
c=(n%100)%10 #3 число
print(a*100+b*10+c)
print(a*100+c*10+b)
print(b*100+a*10+c)
print(b*100+c*10+a)
print(c*100+a*10+b)
print(c*100+b*10+a)



n=int(input())
a=n//1000  #1е
b=(n//100)%10 #2е  
c=((n//10)%100)%10 #3е   456
d=(n//10)%10) #4е


print('Цифра в позиции тысяч равна', a)
print('Цифра в позиции сотен равна', b)
print('Цифра в позиции десятков равна', c)
print('Цифра в позиции единиц равна', d)


n = int(input())

d1 = (n // 10 ** 3) % 10
d2 = (n // 10 ** 2) % 10
d3 = (n // 10 ** 1) % 10
d4 = (n // 10 ** 0) % 10