n=int(input())
for i in range(n+1):
    print('Квадрат числа', i, 'равен', i**2)


    n=int(input())
for i in range(n):
    print((n-i)*'*')


    m, p, n=int(input()), int(input()), int(input())
for i in range(n):
    print(i+1, m*(p/100+1)**i)





m = int(input())
n = int(input())

if m > n:
    # в порядке убывания
    for i in range(m, n - 1, -1):
        print(i)
else:
    # в порядке возрастания
    for i in range(m, n + 1):
        print(i)



m = int(input())
n = int(input())

for i in range(m, n - 1, -1):
    if i%2!=0:
        print(i)




m = int(input())
n = int(input())

for i in range(m, n+1):
    if (i%17==0) or (i%10==9) or (i%3==0 and i%5==0):
        print(i)



n = int(input())

for i in range(10):
    print(n, 'x', i+1, '=', n*(i+1))
