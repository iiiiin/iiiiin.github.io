---
title: "[SWEA] 6485. 삼성시의 버스 노선 - Python"
date: 2024-11-06 16:00:00 +0900
categories: [Algorithm]
tags: [Python, Algorithm]
---

## 풀이

버스 정류장 번호를 인덱스로 하는 리스트 생성
노선 구간에 정류장이 속할 경우 +1 반복

## 코드

```python
# 6485
# 삼성시의 버스 노선

T = int(input())
result = []

for test_case in range(1,T+1):
    n = int(input())
    bus = [0]*5001
    for _ in range(n):
        a, b = map(int, input().split())
        for i in range(a,b+1):
            bus[i] += 1
    p = int(input())
    temp = [bus[int(input())] for x in range(p)]
    result.append(temp)

for j in range(1,T+1):
    print(f"#{j}", end=" ")
    print(*result[j-1])
```
    
> 출처: SWEA
> https://swexpertacademy.com/main/main.do