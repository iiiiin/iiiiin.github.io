---
title: "[SWEA] 16002. 합성수 방정식 - Python"
date: 2024-11-06 16:00:00 +0900
categories: [Algorithm]
tags: [Python, Algorithm]
description: "SWEA '16002. 합성수 방정식' 문제 풀이를 정리했습니다."
---

## 풀이

입력받은 n에 대해
x, x+n 이 합성수 인지 판별하는 함수 생성
만족할 경우 반복문 중지

* 합성수 판별 함수
	수의 제곱근까지만 확인하여
	약수가 있는지 확인
    **제곱근을 기준으로 약수들이 대칭이기 때문에 제곱근까지만 확인**

## 코드

```python
# 16002
# 합성수 방정식

# x, y가 합성수인지 확인하는 함수
def chk(num):
    for i in range(2,int(num**(0.5))+1):
        if num % i == 0:
            return True
    return False

T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    x = 4
    # x, x+n을 만족하는 x 값을 확인
    # x, y(x+n)의 함수가 모두 True 일 때, 반복문 중단
    while True:
        if chk(x) and chk(x+n):
            break
        x += 1
    print(f"#{test_case} {x+n} {x}")
```

> 출처: SWEA
> https://swexpertacademy.com/main/main.do