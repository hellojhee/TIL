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


