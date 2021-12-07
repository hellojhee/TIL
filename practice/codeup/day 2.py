# 소수점 처리
'''
import math
- 버림
print( int(12.5656565656) )
print( math.trunc(12.5656565656) )
- 올림
print( math.ceil(12.12121212) )
- digit = 2 # 소수점 이하 2자리
- 자릿수 올림
print( math.ceil(12.5656565656 * 10 ** digit) / 10 ** digit )
- 자릿수 버림
print( math.floor(12.5656565656 * 10 ** digit) / 10 ** digit )
- 반올림
print( round(12.565656565656, 2) )
'''

import math
print(math.trunc(3.141592))
print(math.ceil(3.141592))
print(round(3.141592))
f'{3.141592:.2f}'


# 6048
a, b = map(int, input().split())
print(a < b)

# 6049
a, b = map(int, input().split())
print(a == b)

# 6050
a, b = map(int, input().split())
print(a <= b)

# 6051
a, b = map(int, input().split())
print(a != b)

# 6052
n = int(input())
print(bool(n))

# 6053
n = bool(int(input()))
print(not n)

# 6054
a, b = map(int, input().split())
print(bool(a and b))

# 6055
a, b = map(int, input().split())
print(bool(a or b))

# 6056
# 두 값의 True / False 값이 서로 다를 경우만 True 를 출력하고, 그 외의 경우에는 False 를 출력한다
a, b = map(int, input().split())
print(bool((a and (not b)) or ((not a) and b)))

# 6057
# 두 값의 True / False 값이 서로 같을 경우만 True 를 출력하고, 그 외의 경우에는 False 를 출력한다.
a, b = map(int, input().split())
print(bool(((not a) and (not b)) or (a and b)))

# 6058
# 두 값의 True / False 값이 모두 False 일 때만 True 를 출력하고, 그 외의 경우에는 False 를 출력한다.
a, b = map(int, input().split())
print(bool(not (a or b)))

# 6065
# 3개의 정수가 공백으로 입력받아 짝수만 줄을 바꿔 출력
num = map(int, input().split())
for i in num:
  if i % 2 == 0:
    print(i)

# 6066
# 정수 3개 입력받아 짝/홀 출력
num = map(int, input().split())
for i in num:
  if i % 2 == 0:
    print('even')
  else:
    print('odd')

# 6067
a = int(input())
if a < 0:
  if a % 2 == 0:
    print('A')
  else:
    print('B')
elif a > 0:
  if a % 2 == 0:
    print('C')
  else :
    print('D')

# 6068
score = int(input())
if (90 <= score):
  print('A')
elif (70 <= score):
  print('B')
elif (40 <= score):
  print('C')
else:
  print('D')

# 6069
test = input()
if test == 'A':
  print('best!!!')
elif test == 'B':
  print('good!!')
elif test == 'C':
  print('run!')
elif test == 'D':
  print('slowly~')
else:
  print('what?')

# 6070
month = int(input())
if (month // 3) == 1:
  print('spring')
elif (month // 3) == 2:
  print('summer')
elif (month // 3) == 3:
  print('fall')
elif (month == 12) or (month == 1) or (month == 2):
  print('winter')
else:
  pass

# 6071
# 입력된 정수를 줄을 바꿔 하나씩 출력하는데, 0이 입력되면 종료한다(0은 출력하지 않는다)

n = int(input())
while n != 0:
  print(n)
  n = int(input())

while True:
  n = int(input())
  if (n == 0):
    break
  print(n)

# 6072
# 1만큼씩 줄이면서 한 줄에 1개씩 카운트다운 수를 출력한다.
n = int(input())
while True:
  print(n)
  n -= 1
  if n == 0:
    break

n = int(input())
while True:
  if n != 0:
    print(n)
  else:
    break
  n -= 1

# 6073
# 1만큼씩 줄이면서 카운트다운 수가 0이 될 때까지 한 줄에 1개씩 출력한다
n = int(input())
while True:
  n -= 1
  print(n)
  if n == 0:
    break

# 6074
# a부터 입력한 문자까지 순서대로 공백을 두고 한 줄로 출력한다.
strs = ord(input())
start = ord('a')
while start <= strs:
  print(chr(start), end=' ')
  start += 1

# 6075
# 0부터 그 수까지 줄을 바꿔 한 개씩 출력한다
n = int(input())
st = 0
while st <= n:
  print(st)
  st += 1

# 6076
n = int(input())
for i in range(n+1):
  print(i)

# 6077
# 1부터 그 수까지 짝수만 합해 출력한다
n = int(input())
s = 0
for i in range(n+1):
  if (i % 2) == 0:
    s += i
print(s)

# 6078
# 영문 소문자 'q'가 입력될 때까지 입력한 문자를 계속 출력한다
while True:
  a = input()
  if a == 'q':
    print(a)
    break
  print(a)

# 6079
# 1, 2, 3, 4, 5 ... 를 순서대로 계속 더해 합을 만들어가다가,
# 입력된 정수와 같거나 커졌을 때, 마지막에 더한 정수를 출력한다.
n = int(input())
s = 0
for i in range(n):
  s += i
  if s >= n:
    break
print(i)

# 6080
# 서로 다른 주사위 2개의 면의 개수 n, m이 공백을 두고 입력
# 첫 번째 수는 n, 두 번째 수는 m으로 고정해 1부터 오름차순 순서로 출력
n, m = map(int, input().split())
for i in range(1, n+1):
  for j in range(1, m+1):
    print(i, j)

# 6081
# 입력된 16진수에 1~F까지 순서대로 곱한, 16진수 구구단을 줄을 바꿔 출력한다.
# 계산 결과도 16진수로 출력해야 한다.
a = int(input(), 16)
for i in range(1, 16):
  print('{:X}*{:X}={:X}'.format(a, i, a*i))

# 입력값도 16진수로 받고, i도 16진수로 받아서 곱한 결과도 16진수
# {:X}.format(a)


# 6082
# 369게임
# 1 부터 그 수까지 순서대로 공백을 두고 수를 출력하는데,
# 3 또는 6 또는 9가 포함 되어있는 수인 경우, 그 수 대신 영문 대문자 X 를 출력한다.
n = int(input())
for i in range(1, n+1):
  if (i % 10 == 3) or (i % 10 == 6) or (i % 10 == 9):
    print('X', end=" ")
  else:
    print(i, end=" ")

# 6083
# 빛 섞어 색 만들기
r, g, b = map(int, input().split())
n = 0
for i in range(r):
  for j in range(g):
    for k in range(b):
      print(i, j, k)
      n += 1
print(n)

# 6084 
# 계산된 값은 bit
# 8bit로 나누면 byte가 되고, 1024byte로 나누면 KB, 1024KB로 나누면 MB
h, b, c, s = map(int, input().split())
mb = h * b * c * s / 8 / 1024 / 1024
print('{:.1f} MB'.format(mb))

# 6085
# 필요한 저장 공간을 MB 단위로 바꾸어 출력한다.
# 단, 소수점 셋째 자리에서 반올림하여 둘째 자리까지 출력한다.
w, h, b = map(int, input().split())
bit = w * h * b
byte = bit / 8
kb = byte / 1024
mb = kb / 1024
print(f'{mb:.2f}', 'MB')

# 6086
# 1, 2, 3, 4, 5 ... 순서대로 계속 더해가다가, 그 합이 입력된 정수보다 커지거나 같아지는 경우,
# 그때까지의 합을 출력한다.
n = int(input())
s = 0
for i in range(1, n+1):
  s += i
  if s >= n:
    break
print(s)

# 6087
# 1부터 입력한 정수까지 1씩 증가시켜 출력하는 프로그램을 작성하되,
# 3의 배수인 경우는 출력하지 않도록 만들어보자.

n = int(input())
for i in range(1, n+1):
  if i % 3 == 0:
    pass
  else:
    print(i, end=' ')

# 6088
# 시작 값(a), 등차의 값(d), 몇 번째 수 인지를 의미하는 정수(n)가
# 공백을 두고 입력된다.(모두 0 ~ 100)
a, d, n = map(int, input().split())
start = a
for i in range(n-1):
  start += d
print(start)

a, d, n = map(int, input().split())
print(a + d * (n-1))

# 6089
# 등비수열
a, r, n = map(int, input().split())
for i in range(n-1):
  a *= r
print(a)

# 6090
a, m, d, n = map(int, input().split())
for i in range(n-1):
  a = a * m + d
print(a)

# 6091
# 3개의 수의 최소공배수
# 3개의 수로 나눈 나머지가 모두 0이어야함
a, b, c = map(int, input().split())
day = 0
while True:
  day += 1
  if (day % a == 0) and (day % b == 0) and (day % c == 0):
    print(day)
    break


# 6092
# 이상한 출석 번호
# 첫 번째 줄에 출석 번호를 부른 횟수인 정수 n이 입력된다. (1 ~ 10000)
# 두 번째 줄에는 무작위로 부른 n개의 번호(1 ~ 23)가 공백을 두고 순서대로 입력된다.

n = int(input())
num = list(map(int, input().split()))  # 출석번호 저장할 리스트
checklist = [0] * 24  # 빈 리스트에 각 번호가 몇번씩 불렸는지 저장
for i in range(n):
  checklist[num[i]] += 1  # num[0]=1이라면, checklist[1]자리에 숫자+1
for j in range(1, len(checklist)):
  print(checklist[j], sep=' ')


# 6093
# 출석을 부른 번호 순서를 바꾸어 공백을 두고 출력한다.

n = int(input())
num = list(map(int, input().split()))
for i in range(n-1, -1, -1):
  print(num[i], end=' ')


# 6094
# 출석을 부른 번호 중에 가장 빠른 번호를 출력한다.

n = int(input())
num = list(map(int, input().split()))
mini = num[0]
for i in range(n):
    if num[i] < mini:
        mini = num[i]
print(mini)


