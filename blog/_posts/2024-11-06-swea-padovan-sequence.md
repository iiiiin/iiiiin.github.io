---
title: "[SWEA] 3376. 파도반 수열 - Python"
date: 2024-11-06 16:00:00 +0900
categories: [Algorithm]
tags: [Python, Algorithm]
description: "SWEA '3376. 파도반 수열' 문제 풀이를 정리했습니다."
---

## 풀이

<span style="color: red">1</span> 1 1 (1+1) <span style="color: red">(1+1)</span> <span style="color: red">(1+(1+1))</span> (1+(1+(1+1))) 
(1+(1+(1+(1+1)))) ((1+1)+(1+(1+(1+(1+1))))) 
((1+(1+1))+((1+1)+(1+(1+(1+(1+1))))))


수열 나열 후 규칙 찾기
점화식: **d[i] = d[i-1] + d[i-5]
**

## 코드

```python
# 3376
# 파도반 수열

T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    seq = [1,1,1,2,2]
    if n > 5:
        i = 5
        while i <= n:
            seq.append(seq[i-1]+seq[i-5])
            i += 1
    result = seq[n-1]
    print(f"#{test_case} {result}")
```

> 출처: SWEA
> https://swexpertacademy.com/main/main.do
