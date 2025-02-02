s = 13
k = -5  
d = s + 2  # d = 15
s = d  # s = 15
k = 2 * s  # k = 30
print(s + k + d)  # 15 + 30 + 15 = 60



a = 17 // (23 % 7)  # a = 17 // 2 = 8
b = 34 % a * 5 - 29 % 4 * 3  # b = 34 % 8 * 5 - 29 % 4 * 3 = 2 * 5 - 1 * 3 = 10 - 3 = 7
print(a * b)  # 8 * 7 = 56

s='*'
print(s*17)
print(s, s, sep=' '*15)
print(s, s, sep=' '*15)
print(s*17)




n=int(input())
print((n*100+(n*10)+n)+(n*10+n)+n)
