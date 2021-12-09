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

