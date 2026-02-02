---
title: "[SWEA] 20934. 방울 마술 - Python"
date: 2024-11-06 16:00:00 +0900
categories: [Algorithm]
tags: [Python, Algorithm]
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
# 20934
# 방울 마술

T = int(input())

for test_case in range(1,T+1):
    s, k = input().split()
    s = list(s)
    bell = s.index("o")
    for i in range(int(k)):
        if bell == 0:
            bell += 1
        else:
            bell -= 1
    result = bell
    print(f"#{test_case} {result}")
```

> 출처: SWEA
> https://swexpertacademy.com/main/main.do