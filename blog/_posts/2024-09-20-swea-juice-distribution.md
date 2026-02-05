---
title: "[SWEA] 5601. [Professional] 쥬스 나누기 - Python"
date: 2024-09-20 16:00:00 +0900
categories: [Algorithm]
tags: [Python, Algorithm]
description: "SWEA '5601. [Professional] 쥬스 나누기' 문제 풀이를 정리했습니다."
---

## 풀이
**내가 정한 양의 주스를 내가 못 마실 수도 있다.**
를 고려하면 최대한의 쥬스를 마시기 위해 균등하게 **1/N** 잔으로 분배해야 함을 알 수 있다.


## 코드
```python
# 5601
# [Professional] 쥬스 나누기

T = int(input())

for test_case in range(1,T+1):
    juice = int(input())
    result = ["1"+"/"+str(juice) for _ in range(juice)]
    print(f"#{test_case} ", end="")
    print(*result)
```
> 출처: SWEA
> https://swexpertacademy.com/main/main.do