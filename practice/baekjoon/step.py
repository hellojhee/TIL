# 백준 10950
t = int(input())
for i in range(t):
  a, b = map(int, input().split())
  print(a + b)


# 백준 10951
while True:
  try:
    a, b = map(int, input().split())
  except Exception:
    break
  print(a + b)


# 백준 10952
while True:
  a, b = map(int, input().split())
  if a == 0 and b == 0:
    break
  print(a + b)


# 백준 10953
t = int(input())
for i in range(t):
  a, b = map(int, input().split(','))
  print(a + b)


# 백준 11021
t = int(input())
for i in range(1, t+1):
  a, b = map(int, input().split())
  print('Case #{}: {}'.format(i, a + b))


# 백준 11022
t = int(input())
for i in range(1, t+1):
  a, b = map(int, input().split())
  print('Case #{}: {} + {} = {}'.format(i, a, b, a + b))


# 백준 2438
# 별찍기 1
n = int(input())
for i in range(1, n+1):
  print('*'*i)

# 2438 중첩루프로 풀어보기
n = int(input())
for i in range(1, n + 1):
  for j in range(i):
    print('*', end='')
  print()


# 백준 2439
# 별찍기 2
n = int(input())
for i in range(1, n + 1):
  print(' ' * (n - i), '*' * i, sep='')

n = int(input())  # 루프
for i in range(1, n+1):
  for j in range(n-i):
    print(' ', end='')
  for j in range(i):
    print('*', end='')
  print()


# 백준 2440
# 별찍기 3
n = int(input())
for i in range(1, n + 1):
  print('*' * (n - i + 1))

n = int(input())
for i in range(1, n+1):
  for j in range(n-i+1):
    print('*', end='')
  for k in range(i-1):
    print(' ', end='')
  print()

n = int(input())
for i in range(n, 0, -1):
  for j in range(i):
    print('*', end='')
  print()


# 백준 2441
# 별찍기 4
n = int(input())
for i in range(1, n + 1):
  print(' ' * (i - 1) + '*' * (n - i + 1))

n = int(input())
for i in range(1, n+1):
  for j in range(i-1):
    print(' ', end='')
  for k in range(n-i+1):
    print('*', end='')
  print()

n = int(input())
for i in range(n, 0, -1):
  for j in range(n-i):
    print(' ', end='')
  for k in range(i):
    print('*', end='')
  print()


# 백준 2442
# 별찍기 5
n = int(input())
for i in range(1, n + 1):
  print(' ' * (n - i) + '*' * ((2 * i) - 1))

n = int(input())
for i in range(1, n+1):
    for j in range(n-i):
        print(' ', end='')
    for k in range((2*i)-1):
        print('*', end='')
    print()


# 백준 2443
# 별찍기 6
n = int(input())
for i in range(1, n + 1):
  print(' ' * (i - 1) + '*' * ((2 * n)-((2 * i) - 1)))

n = int(input())
for i in range(1, n+1):
    for j in range(i-1):
        print(' ', end='')
    for k in range((2 * n)-((2 * i) - 1)):
        print('*', end='')
    print()

n = int(input())
for i in range(n, 0, -1):
    for j in range(n-i):
        print(' ', end='')
    for k in range((2 * i) - 1):
        print('*', end='')
    print()


# 백준 2444
# 별찍기 7
n = int(input())
for i in range(1, n+1):
  print(' ' * (n - i) + '*' * ((2 * i) - 1))
for j in range(n-1, 0, -1):
  print(' ' * (n-j) + '*' * ((2*j)-1))


# 백준 2445
# 별찍기 8
n = int(input())
for i in range(1, n+1):
  print('*'*i + ' ' * (2*(n-i)) + '*'*i)
for j in range(n-1, 0, -1):
  print('*'*j + ' ' * (2*(n-j)) + '*'*j)


# 백준 2446
# 별찍기 9
n = int(input())
for i in range(n, 0, -1):
  print(' ' * (n-i) + '*' * ((2*i)-1))
for j in range(2, n+1):
  print(' ' * (n - j) + '*' * ((2 * j) - 1))


# 백준 10818
# 최솟값과 최댓값을 구하는 프로그램을 작성
n = int(input())
num = list(map(int, input().split()))
mini = num[0]
maxi = num[0]
for i in range(n):
  if num[i] < mini:
    mini = num[i]
  elif num[i] > maxi:
    maxi = num[i]
print(mini, maxi, sep=' ')


# 백준 2577
# 숫자의 개수
a = int(input())
b = int(input())
c = int(input())
xxx = list(map(int, str(a * b * c)))  # 문자열을 숫자로 map()
xlist = [0]*10
for i in range(len(xxx)):
  xlist[xxx[i]] += 1
for j in range(len(xlist)):
  print(xlist[j])


# 3052
# 나머지를 계산하고 나머지가 다른 숫자의 개수
ans = [0] * 42
for i in range(10):
  a = int(input())
  b = a % 42
  ans[b] = 1
print(sum(ans))


# 2562
# 최댓값과 최댓값의 위치 

maxi = 0  # 최댓값
whmaxi = 0 # 최댓값 위치
for i in range(1, 10):
  n = int(input())
  if maxi < n:
    maxi = n
    whmaxi = i
print(maxi, whmaxi, sep='\n')


## 별찍기 2차원 리스트로

# 1
n = int(input())
a = [[' '] * n for _ in range(n)]

for i in range(n):
    for j in range(i+1):
        #print('a[{}][{}]'.format(i, j))
        a[i][j] = '*'
for i in range(n):
    for j in range(n):
        print(a[i][j], end='')
    print()


# 2
n = int(input())
a = [[' '] * n for _ in range(n)]

for i in range(n):
    for j in range(n-1, n-i-2, -1):
        a[i][j] = '*'
for i in range(n):
    for j in range(n):
        print(a[i][j], end='')
    print()


# 3
n = int(input())
a = [[' '] * n for _ in range(n)]

for i in range(n):
    for j in range(n-i):
        a[i][j] = '*'
for i in range(n):
    for j in range(n):
        print(a[i][j], end='')
    print()


# 4
n = int(input())
a = [[' '] * n for _ in range(n)]

for i in range(n):
    for j in range(i, n):
        a[i][j] = '*'
for i in range(n):
    for j in range(n):
        print(a[i][j], end='')
    print()


