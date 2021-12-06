# 6003
print("hello \nworld")

# 6007
print('"C:\\Download\\\'hello\'.py"')

# 6008
print('print("Hello\\nWorld")')

# 6009
aa = input()
print(aa)

# 6010
n = int(input())
print(n)

# 6011
n = float(input())
print(n)

# 6012
a = int(input())
b = int(input())
print(a)
print(b)

# 6013
a = input()
b = input()
print(b)
print(a)

# 6014
a = float(input())
print(a)
print(a)
print(a)

# 6015
# 정수로 변환해서 분할한뒤 출력 -> map(int, input())
a, b = map(int, input().split())
print(a)
print(b)

# 6016
a, b = input().split()
print(b, a)

# 6017
a = input()
print(a, a, a)

# 6018
a, b = input().split(':')
print(a, b,  sep=':')

# 6019
y, m, d = input().split('.')
print(d, m, y, sep='-')

# 6020
a, b = input().split('-')
print(a, b, sep='')

# 6021
a = input()
for i in range(len(a)):
  print(a[i])

# 6022
a = input()
print(a[0:2], a[2:4], a[4:6])

# 6023
h, m, s = input().split(':')
print(m)

# 6024
a, b = input().split()
print(a, b, sep='')

# 6025
a, b = map(int, input().split())
print(a + b)

# 6026
a = float(input())
b = float(input())
print(a + b)

# 6027 # hex()함수
a = hex(int(input()))
print(a[2:])

'{:x}'.format(255)
f'{255:x}'

a = int(input())
print('%x'%a)

# 6028
a = int(input())
print('%X'%a)

f'{int(input()):X}'

# 6029
a = int(input(), 16)
print('%o'%a)

print(f'{int(input(), 16):o}')

# 6030
# 아스키 코드 ord()
a = ord(input())
print(a)

# 6031
a = int(input())
print(chr(a))

# 6032
a = int(input())
print(-a)

# 6033
a = input()
print(chr(ord(a)+1))

# 6034
a, b = map(int, input().split())
print(a - b)

# 6035
a, b = map(float, input().split())
print(a * b)

# 6036
a, b = input().split()
print(a * int(b))

# 6037
a = int(input())
b = input()
print(a * b)

# 6038
a, b = map(int, input().split())
print(a**b)

# 6039
a, b = map(float, input().split())
print(a**b)

# 6040
a, b = map(int, input().split())
print(a//b)

# 6041
a, b = map(int, input().split())
print(a%b)

# 6042
a = float(input())
print(round(a, 2))

format(3.141595, ".2f")

# 6043
a, b = map(float, input().split())
print(format(a/b, '.3f'))

# 6044
a, b = map(int, input().split())
print(a+b, a-b, a*b, a//b, a%b, format(a/b, '.2f'), sep='\n')

# 6045
a, b, c = map(int, input().split())
summ = a+b+c
aver = summ/3
print(summ, format(aver, '.2f'))

