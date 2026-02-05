---
title: "[SWEA] 22795. 일곱 부하의 평균 - Python"
date: 2025-01-13 16:00:00 +0900
categories: [Algorithm]
tags: [Python, Algorithm]
description: "SWEA '22795. 일곱 부하의 평균' 문제 풀이를 정리했습니다."
---

## 풀이

조건을 잘 확인해야 한다.
입력된 여섯 부하보다 큰 값을 가지고, 모든 부하의 키의 평균이 양의 <span style="color:red">**정수**</span>라는 것이다.
따라서, **(모든 키 값의 합) % 7 == 0** 이어야 된다는 것을 알 수 있다.

여섯 부하의 키 값 중 가장 큰 값을 기준으로 1 씩 증가시키며 조건을 만족하는지 확인한다.


## 코드

```python
# 22795
# 일곱 부하의 평균

T = int(input())

for test_case in range(1,T+1):
    height = list(map(int, input().split()))
    max_height = max(height)
    result = max(height)
    total = sum(height)
    while True:
        result += 1
        if (total+result) % 7 == 0:
            break
    print(result)
   
```


> 출처: SWEA
> https://swexpertacademy.com/main/main.do