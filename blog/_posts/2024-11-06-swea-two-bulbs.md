---
title: "[SWEA] 12741. 두 전구 - Python"
date: 2024-11-06 16:00:00 +0900
categories: [Algorithm]
tags: [Python, Algorithm]
description: "SWEA '12741. 두 전구' 문제 풀이를 정리했습니다."
---

## 풀이

1. 경우에 따라 조건 설정, 규칙 찾기
2. a,c중 큰 값에서 b,d 중 작은 값을 뺀 것

## 코드

```python
# 12741
# 두 전구

T = int(input())
answer = []

for test_case in range(1,T+1):
    a,b,c,d = map(int, input().split())
    result = min(b,d) - max(a,c)
    if result < 0:
        answer.append("#"+str(test_case)+" "+"0")
    else:
        answer.append("#"+str(test_case)+" "+str(result))
for x in answer:
    print(x)
```

> 출처: SWEA
> https://swexpertacademy.com/main/main.do
