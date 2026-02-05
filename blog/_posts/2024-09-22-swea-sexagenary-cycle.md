---
title: "[SWEA] 19185. 육십갑자 - Python"
date: 2024-09-22 16:00:00 +0900
categories: [Algorithm]
tags: [Python, Algorithm]
description: "SWEA '19185. 육십갑자' 문제 풀이를 정리했습니다."
---

## 풀이

현재 방울이 있을 확률이 가장 높은 컵의 위치
(단, 그러한 컵이 여러 개 있다면 그 중 가장 왼쪽 위치)

최대한 왼쪽 위치에 방울이 있는 경우 고려

1. o..
	시작 위치가 .o.인 경우, 왼쪽으로 이동
    시작 위치가 ..o인 경우, 왼쪽으로 계속 이동
2. .o.
	시작 위치가 o..인 경우, 오른쪽으로 이동
    시작 위치가 ..o인 경우, 왼쪽으로 이동
3. ..o
	K=0 인 경우, 이동하지 않았을 때만 가능

시작 위치 0인 경우 오른쪽으로 이동
그 외의 경우 모두 왼쪽으로 이동

## 코드
```python
# 19185
# 육십갑자

T = int(input())

for test_case in range():
    n,m = map(int, input().split())
    s = list(input().split())
    t = list(input().split())
    q = int(input())
    result = []
    for _ in range(q):
        k = int(input())
        result.append("".join([s[k%n-1],t[k%m-1]]))
    print(f"#{test_case} ", end="")
    print(*result)
```

> 출처: SWEA
> https://swexpertacademy.com/main/main.do