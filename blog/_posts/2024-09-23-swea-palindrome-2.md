---
title: "[SWEA] 1216. [S/W 문제해결 기본] 3일차 - 회문2 - Python"
date: 2024-09-23 16:00:00 +0900
categories: [Algorithm]
tags: [Python, Algorithm]
---

## 풀이
배열에서 슬라이딩윈도우처럼 시작점을 이동하며 특정 길이 j인 문자열이 회문인지 확인하고, 회문을 찾으면 그 길이를 리스트에 담는다.
배열을 전치 후에 다시 반복하여 회문을 찾아 그 길이를 리스트에 담는다. 이후 리스트의 최댓값, 즉 회문 길이의 최댓값을 찾는다.


## 코드
```python
# 1216
# [S/W 문제해결 기본] 3일차 - 회문2

for test_case in range(1,11):
    n = int(input())
    s = [input() for _ in range(100)]
    temp = []
    
    for i in range(100):
        flag = 0
        for j in range(100,-1,-1):
            for k in range(100-j+1):
                if s[i][k:k+j] == s[i][k:k+j][::-1]:
                    temp.append(j)
                    flag = 1
                    break
            if flag == 1:
                break

    s = list(zip(*s))

    for i in range(100):
        flag = 0
        for j in range(100,-1,-1):
            for k in range(100-j+1):
                if "".join(s[i][k:k+j]) == "".join(s[i][k:k+j])[::-1]:
                    temp.append(j)
                    flag = 1
                    break
            if flag == 1:
                break
   
    result = max(temp)
    print(f"#{n} {result}")
```

> 출처: SWEA
> https://swexpertacademy.com/main/main.do