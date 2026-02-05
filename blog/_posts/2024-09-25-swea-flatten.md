---
title: "[SWEA] 1208. [S/W 문제해결 기본] 1일차 - Flatten - Python"
date: 2024-09-25 16:00:00 +0900
categories: [Algorithm]
tags: [Python, Algorithm]
description: "SWEA '1208. [S/W 문제해결 기본] 1일차' 문제 풀이를 정리했습니다."
---

## 풀이
덤프를 주어진 횟수만큼 수행한다.
index 메서드로 최고점과 최저점의 위치를 찾아 1씩 옮긴다.


## 코드
```python
# 1208
# [S/W 문제해결 기본] 1일차 - Flatten

for test_case in range(1,11):
    dump = int(input())
    box = list(map(int, input().split()))
    for i in range(dump):
        box[box.index(max(box))] -= 1
        box[box.index(min(box))] += 1
    result = max(box) - min(box)
    print(f"#{test_case} {result}")
```
> 출처: SWEA
> https://swexpertacademy.com/main/main.do