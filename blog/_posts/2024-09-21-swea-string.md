---
title: "[SWEA] 1213. [S/W 문제해결 기본] 3일차 - String - Python"
date: 2024-09-21 16:00:00 +0900
categories: [Algorithm]
tags: [Python, Algorithm]
---

## 풀이
`count()` 메서드를 사용하여 간단하게 특정 문자열의 개수를 구한다. 


## 코드
```python
# 1213
# [S/W 문제해결 기본] 3일차 - String

for test_case in range(1,11):
    n = int(input())
    s_find = input()
    s = input()
    result = s.count(s_find)
    print(f"#{n} {result}")
```
> 출처: SWEA
> https://swexpertacademy.com/main/main.do