# 스택과 큐

## 스택 자료구조

- 먼저 들어온 자료가 나중에 나가는 형식 (선입후출)
- 입구와 출구가 동일

```python
stack = []

stack.append(5)  # 삽입
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()  # 삭제
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1])  # 최상단 원소부터 출력
print(stack)  # 최하단 원소부터 출력

# 실행결과
[1, 3, 2, 5]
[5, 2, 3, 1]
```



## 큐 자료구조

- 먼저 들어온 데이터가 먼저 나가는 형식 (선입선출)
- 큐는 입구와 출구가 모두 뚫려있는 터널과 같은 형태

```python
from collections import deque

queue = deque()

queue.append(5)  # 삽입
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()  # 삭제
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)  # 먼저 들어온 순서대로 출력
queue.reverse()  # 역순
print(queue)  # 나중에 들어온 원소부터 출력

# 실행결과
deque([3, 7, 1, 4])
deque([4, 1, 7, 3])
```



# 우선순위에 따른 자료구조

## 우선순위 큐

- 우선순위 큐는 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조
- 우선순위 큐는 데이터를 우선순위에 따라 처리하고 싶을때 사용

| 자료구조                    | 추출되는 데이터             |
| --------------------------- | --------------------------- |
| 스택(Stack)                 | 가장 나중에 삽입된 데이터   |
| 큐(Queue)                   | 가장 먼저 삽입된 데이터     |
| 우선순위 큐(Priority Queue) | 가장 우선순위가 높은 데이터 |

- 우선순위 큐 구현 방법

1. 리스트를 이용하여
2. 힙(heap)을 이용하여

- 데이터의 개수가 N개 일때, 구현방식에 따른 복잡도

| 우선순위 큐 구현 방식 | 삽입 시간 | 삭제 시간 |
| --------------------- | --------- | --------- |
| 리스트                | O(1)      | O(N)      |
| 힙                    | O(logN)   | O(logN)   |

- 단순히 N개의 데이터를 힙에 넣었다가 모두 꺼내는 작업은 정렬과 동일(힙 정렬)
  - 이 경우 시간 복잡도 : O(NlogN)



## 힙의 특징

- 힙은 완전 이진 트리 자료구조의 일종
- 힙에서는 항상 루트 노드(root node)를 제거
- 최소 힙(min heap)
  - 루트 노드가 가장 작은 값을 가짐
  - 따라서 값이 작은 데이터가 우선적으로 제거
- 최대 힙(max heap)
  - 루트 노드가 가장 큰 값을 가짐
  - 따라서 값이 큰 데이터가 우선적으로 제거



## 완전 이진 트리

- Complete Binary Tree
- 완전 이진 트리란 루트 노드부터 시작하여 왼쪽 자식 노드, 오른쪽 자식 노드 순서대로 데이터가 차례대로 삽입되는 트리



## 최소 힙 구성 함수

`Min-Heapify()`

- 부모 노드로 거슬러 올라가며, 부모보다 자신의 값이 더 작은 경우에 위치를 교체

- 힙에 새로운 원소가 삽입
  -  O(logN)의 시간 복잡도로 힙 성질을 유지하도록 할수있다
- 힙에서 원소가 제거
  - O(logN)의 시간 복잡도로 힙 성질을 유지하도록 할수있다
  - 이후에 루트 노드에서부터 하향식으로 `Heapify()`진행



## 우선순위 큐 라이브러리

```python
import sys
import heapq
input = sys.stdin.readline

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))
  
res = heapsort(arr)

for i in range(n):
    print(res[i])
```



# 트리 자료구조

## 트리

- 가계도와 같은 계층적인 구조
  - 루트 노드(root node)  : 부모가 없는 최상위 노드
  - 단말 노드(leaf node) : 자식이 없는 노드
  - 크기(size) : 트리에 포함된 모든 노드의 개수
  - 깊이(depth) : 루트 노드부터의 거리
  - 높이(height) : 깊이 중 최댓값
  - 차수(degredd) : 각 노드의 자식 방향 간선 개수
- 기본적으로 트리의 크기가 N일때, 전체 간선의 개수는 N-1개



## 이진 탐색 트리

- 이진 탐색이 동작할 수 있도록 고안된 효율적인 탐색이 가능한 자료구조의 일종
- 특징 : 왼쪽 자식 노드 < 부모 노드 < 오른쪽 자식 노드
  - 찾고자 하는 원소가 현재 노드보다 큰 경우 오른쪽으로



## 트리의 순회

- 트리 자료구조에 포함된 노드를 특정한 방법으로 한번씩 방문하는 방법
  - 트리의 정보를 시각적으로 확인 가능
- 대표적인 트리 순회 방법
  - 전위 순회 : 루트 먼저 방문
  - 중위 순회 : 왼쪽 자식을 방문한 뒤 루트 방문
  - 후위 순회 : 오른쪽 자식을 방문한 뒤 루트 방문

```python
class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node
     
# 전위 순회
def pre_order(node):
    print(node.data, end=' ')
    if node.left_node != None:
        pre_order(tree[node.left_node])
    if node.right_node != None:
        pre_order(tree[node.right_node])
        
# 중위 순회
def in_order(node):
    print(node.data, end=' ')
    if node.left_node != None:
        in_order(tree[node.left_node])
    if node.right_node != None:
        in_order(tree[node.right_node])
        
# 후위 순회
def post_order(node):
    print(node.data, end=' ')
    if node.left_node != None:
        post_order(tree[node.left_node])
    if node.right_node != None:
        post_order(tree[node.right_node])
        
n = int(input())
tree = {}

for i in range(n):
    data, left_node, right_node = input().split()
    if left_node == 'None':
        left_node = None
    if right_node == 'None':
        right_node = None
    tree[data] = Node(data, left_node, right_node)
    
pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])
```



# 바이너리 인덱스 트리

## 구간 합

- 데이터가 계속 바뀌는 상황에서 구간 합



## 바이너리 인덱스 트리

- 2진법 인덱스 구조를 활용해 구간 합 문제를 효과적으로 해결해줄 수 있는 자료구조

  - 펜윅 트리(fenwick tree)라고도 함

- 정수에 따른 2진수 표기

  | 정수 | 2진수 표기                         |
  | ---- | ---------------------------------- |
  | 7    | 00000000 00000000 00000000 0000111 |
  | -7   | 11111111 11111111 11111111 1111001 |

- 0이 아닌 마지막 비트를 찾는 방법

  - 특정한 숫자 K의 0이 아닌 마지막 비트를 찾기위해 K & -K를 계산하면 됨

  - K & -K 계산 결과 예시

    | 정수 K | 2진수 표기                          | K & -K |
    | ------ | ----------------------------------- | ------ |
    | 0      | 00000000 00000000 00000000 00000000 | 0      |
    | 1      | 00000000 00000000 00000000 00000001 | 1      |
    | 2      | 00000000 00000000 00000000 00000010 | 2      |
    | 3      | 00000000 00000000 00000000 00000011 | 1      |
    | 4      | 00000000 00000000 00000000 00000100 | 4      |
    | 5      | 00000000 00000000 00000000 00000101 | 1      |
    | 6      | 00000000 00000000 00000000 00000110 | 2      |
    | 7      | 00000000 00000000 00000000 00000111 | 1      |
    | 8      | 00000000 00000000 00000000 00001000 | 8      |

    ```python
    n = 8
    for i in range(n +1):
        print(i, '의 마지막 비트:', (i & -i))
    ```



- 트리구조 만들기
  - 0이 아닌 마지막 비트 = 내가 저장하고 있는 값들의 개수
- 업데이트
  - 특정 값 변경
    - 0이 아닌 마지막 비트만큼 더하면서 구간들의 값을 변경
- 누적 합
  - 1부터 N까지의 누적 합 구하기
    - ㅇ0이 아닌 마지막 비트만큼 빼면서 구간들의 값의 합 계산

```python
import sys
input = sys.stdin.readline

# 데이터의 개수(n), 변경 횟수(m), 구간 합 계산 횟수(k)
n, m, k = map(int, input().split())

# 전체 데이터의 개수는 최대 1,000,000개
arr = [0] * (n + 1)
tree = [0] * (n + 1)

# i번째 수까지의 누적 합을 계산하는 함수
def prefix_sum(i):
    result = 0
    while i > 0:
        result += tree[i]
        # 0이 아닌 마지막 비트만큼 빼가면서 이동
        i -= (i & -i)
    return result

# i번째 수를 dif만큼 더하는 함수
def update(i, dif):
    while i <= n:
        tree[i] += dif
        i += (i & -i)

# start부터 end까지의 구간 합을 계산하는 함수
def interval_sum(start, end):
    return prefix_sum(end) - prefix_sum(start - 1)

for i in rnage(1, n+1):
    x = int(input())
    arr[i] = x
    update(i, x)
    
for i in range(m+k):
    a, b, c = map(int, input().split())
    # 업데이트 연산인 경우
    if a == 1:
        update(b, c - arr[b])  # 바뀐 크기(dif)만큼 적용
        arr[b] = c
    # 구간 합 연산인 경우
    else:
        print(interval_sum(b, c))
```


# 선택 정렬과 삽입 정렬

## 정렬 알고리즘

- 정렬이란 데이터를 특정한 기준에 따라 순서대로 나열하는 것
- 일반적으로 문제 상황에 따라서 적잘한 정렬 알고리즘이 공식처럼 사용된다

## 선택 정렬

- 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복
- 이중 반복문을 통해 선택 정렬 가능하다

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i  # 가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]  # 스와프

print(array)

# 실행결과
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## 선택 정렬의 시간 복잡도

- 선택 정렬은 N번 만큼 가장 작은 수를 찾아서 맨 앞으로 보내야한다
- 구현 방식에 따라서 사소한 오차가 있을수있지만, 전체 연산 횟수는 다음과 같다

`N + (N - 1) + (N - 2) + ... + 2`

- 이는 `(N^2 + N - 2) / 2`로 표현할 수 있는데, 빅오 표기법에 따라서 O(N^2)이라고 작성

## 삽입 정렬

- 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입
- 선택 정렬에 비해 구현 난이도가 높은 편이지만, 일반적으로 더 효율적으로 동작

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):  # 인덱스 i부터 1까지 1씩 감소하며 반복
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:  # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break
            
print(array)

# 실행결과
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## 삽입 정렬의 시간 복잡도

- 삽입 정렬의 시간 복잡도는 O(N^2)이며, 선택 정렬과 마찬가지로 반복문이 두 번 중첩되어 사용
- 삽입 정렬은 현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작
  - 최선의 경우 O(N)의 시간 복잡도를 가짐
  - 이미 정렬되있는 상태에서 다시 삽입 정렬을 수행하면?
    - 왼쪽 데이터와 비교해서 본인이 더 크기 때문에 탐색과정이 바로 멈춤



# 퀵 정렬과 계수 정렬

## 퀵 정렬

- 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
- 일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘 중 하나
- 병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘
- 가장 기본적인 퀵 정렬은 첫번째 데이터를 기준 데이터(Pivot)로 설정
- 퀵 정렬을 하다보면 피벗을 기준으로 왼쪽은 작은값, 오른쪽은 큰값으로 나뉘는데, 이처럼 데이터 묶음을 나누는 작업을 분할(Divide)이라고 한다
- 왼쪽 데이터 정렬하고, 오른쪽 데이터 정렬

## 퀵 정렬이 빠른 이유

- 이상적인 경우 반할이 절반식 일어난다면 전체 연산 횟수로 O(NlogN)를 기대할수있다
  - 너비 * 높이 = N * logN = NlogN

## 퀵 정렬의 시간 복잡도

- 퀵 정령은 평균의 경우 O(NlogN)의 시간 복잡도를 가진다
- 하지만 최악의 경우 O(N^2)의 시간 복잡도를 가진다
  - 첫번째 원소를 피벗으로 삼을때 이미 정렬된 배열에 대해서 퀵 정렬을 수행하면
    - 피벗의 위치에서 본인의 위치로 가기때문에 분할이 이루어질때마다 오른쪽 부분만 존재하는거랑 마찬가지

```python
# 일반적인 방식

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:  # 원소가 한개인 경우 종료
        return
    pivot = start
    left = start + 1
    right = end
    while (left <= right):
        # 피벗보다 큰 데이터를 찾을때까지 반복
        while (left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을때까지 반복
        while (right > start and array[right] >= array[pivot]):
            right -= 1
        if (left > right):  # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:  # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right, array[left]
                                              
     quick_sort(array, start, right - 1)
     quick_sort(array, right + 1, end)
                                              
quick_sort(array, 0, len(array)-1)
print(array)
            
# 실행결과
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

```python
# 간단한 방식

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return aray
    pivot = array[0]  # 피벗은 첫번째 원소
    tail = array[1:]  # 피벗을 제외한 리스트
    
    left_side = [x for x in tail if x <= pivot]  #분할 왼쪽
    right_side = [x for x in tail if x > pivot]  #분할 오른쪽
   # 분할 후 왼쪽과 오른쪽 각각 정렬 수행하고, 전체 리스트 반환
	return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))

# 실행결과
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## 계수 정렬

- 특정한 조건이 부합할때만 사용할 수 있지만 매우 빠르게 동작하는 정렬 알고리즘
  - 계수 정렬은 데이터의 크기 범위가 제한되어 정수 형태로 표현할수있을때 사용 가능
- 데이터의 개수가 N, 데이터(양수) 중 최댓값이 K일때 최악의 경우에도 수행시간이 O(N+K)를 보장

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# 모든 범위를 포함하는 리스트 선언
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1  # 각 데이터에 해당하는 인덱스 값 증가
for i in range(len(count)):
    for j in range(len(count[i])):
        print(i, end=' ')
        
# 실행 결과
0, 0, 1, 1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9
```

## 계수 정렬의 시간 복잡도

- 계수 정렬의 시간 복잡도와 공간 복잡도는 모두 O(N+K)
- 계수 정렬은 때에 따라서 심각한 비효율성을 초래할수있다
- 계수정렬은 동일한 값을 가지는 데이터가 여러개 등장할때 효과적



# 정렬 알고리즘 비교

| 정렬 알고리즘 | 평균 시간 복잡도 | 공간 복잡도 | 특징                                                         |
| ------------- | ---------------- | ----------- | ------------------------------------------------------------ |
| 선택 정렬     | O(N^2)           | O(N)        | 아이디어가 매우 간단                                         |
| 삽입 정렬     | O(N^2)           | O(N)        | 데이터가 거의 정렬돼있을때 가장 빠름                         |
| 퀵 정렬       | O(NlogN)         | O(N)        | 대부분의 경우에 가장 적합하고 충분히 빠름                    |
| 계수 정렬     | O(N+K)           | O(N+K)      | 데이터 크기가 한정돼있는 경우만 사용가능하지만 매우 빠르게 동작 |

## 문제 : 두 배열 원소 교체

- N개의 원소로 구성된 두 배열 A, B를 최대 K번의 바꿔치 연산을 수행하여, 배열 A의 모든 원소의 합의 최댓값 출력

```python
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse = True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))
```

