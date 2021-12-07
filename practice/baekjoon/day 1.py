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
n = int(input())
for i in range(1, n+1):
  print('*'*i)

# 백준 2439
n = int(input())
for i in range(1, n+1):
  print(' ' * (n - i), '*' * i, sep='')

# 백준 2440
n = int(input())
for i in range(1, n+1):
  print('*' * (n - i + 1))

