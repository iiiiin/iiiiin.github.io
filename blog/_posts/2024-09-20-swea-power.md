---
title: "[SWEA] 1217. [S/W 문제해결 기본] 4일차 - 거듭 제곱 - Python"
date: 2024-09-20 16:00:00 +0900
categories: [Algorithm]
tags: [Python, Algorithm]
---

## 풀이
재귀함수를 사용하여 계산을 수행한다.
밑과 지수(거듭제곱 횟수)가 입력되므로, 
재귀함수의 종료조건에서 거듭제곱 횟수를 제한하여 입력된 만큼 거듭제곱을 반복하도록 한다.
거듭제곱을 실행한 값과 실행한 횟수를 다시 입력으로 재귀함수를 실행한다.


## 코드
```python
# 1217
# [S/W 문제해결 기본] 4일차 - 거듭제곱

def power(x, y, p, cnt):
    # 종료조건
    if p <= cnt:
        return y
    y *= x
    cnt += 1

    # 재귀함수 실행
    return power(x, y, p, cnt)

for test_case in range(10):
    test = int(input())
    n, m = map(int, input().split())
    result = power(n, n, m, 1)
    print(f"#{test} {result}")
```
> 출처: SWEA
> https://swexpertacademy.com/main/main.do