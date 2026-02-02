---
title: "[SWEA] 20728. 공평한 분배 2 - Python"
date: 2024-11-16 16:00:00 +0900
categories: [Algorithm]
tags: [Python, Algorithm]
---

## 풀이
**슬라이딩 윈도우**를 사용하여 풀어보았다.
먼저 원소 값 간 차이를 최소화 하기 위해 배열을 오름차순으로 정렬한다.
그리고 배열에서 선택하는 주머니 개수 만큼 범위를 지정하여
0번째 인덱스부터 차례로 순회한다.

예) \[1,2,3,4,4,5], 주머니 2개
\[`1,2`,3,4,4,5], 최솟값 : 1, 최댓값 : 2
\[1,`2,3`,4,4,5], 최솟값 : 2, 최댓값 : 3
\[1,2,`3,4`,4,5], 최솟값 : 3, 최댓값 : 4
\[1,2,3,`4,4`,5], 최솟값 : 4, 최댓값 : 4
\[1,2,3,4,`4,5`], 최솟값 : 4, 최댓값 : 5

범위 내에서 (최댓값 - 최솟값)을 찾아 이전 결과 값과 비교하여 업데이트한다.

## 코드
```python
T = int(input())

for test_case in range(1, T + 1):

    # 입력받기
    n, k = map(int, input().split())
    pocket = list(map(int, input().split()))
    
    # 오름차순 정렬
    pocket.sort()
    
    # 결과값 : 원소 범위가 1 이상이므로 원소의 최댓값이 차이가 될 수 없으므로 초기화
    result = pocket[-1]
    
    # 반복문 순회하며 조건을 만족하는 값 업데이트
    for i in range(n-k+1):    
        temp = pocket[i:i+k]
        result = min(result, max(temp)-min(temp))
    
    print(f"#{test_case} {result}")
    
```

> 출처: SWEA
> https://swexpertacademy.com/main/main.do