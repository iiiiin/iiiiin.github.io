---
title: "[SWEA] 5603. [Professional] 건초더미 - Python"
date: 2024-09-25 16:00:00 +0900
categories: [Algorithm]
tags: [Python, Algorithm]
description: "SWEA '5603. [Professional] 건초더미' 문제 풀이를 정리했습니다."
---

## 풀이
건초더미 1을 옮기는 데 1회의 움직임이 발생한다.
원래는 모두 같은 크기의 건초더미였으므로 원래 크기는 모든 건초더미의 평균임을 알 수 있다.
평균보다 큰 건초더미에서 평균보다 큰 만큼의 건초더미를 옮기면 된다.

## 코드
```python
# 5603
# [Professional] 건초더미

T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    result = 0
    dummy = [int(input()) for _ in range(n)]
    mean_dummy = sum(dummy)/n
    for i in range(n):
        if mean_dummy < dummy[i]:
            result += dummy[i] - mean_dummy
    print(f"#{test_case} {int(result)}")

```
> 출처: SWEA
> https://swexpertacademy.com/main/main.do