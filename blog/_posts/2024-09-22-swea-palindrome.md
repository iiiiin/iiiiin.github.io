---
title: "[SWEA] 19003. 팰린드롬 문제 - Python"
date: 2024-09-22 16:00:00 +0900
categories: [Algorithm]
tags: [Python, Algorithm]
---

## 풀이

같은 길이의 서로 다른 문자열을 조합해서 
최대 길이의 팰린드롬이 되려면,
**A-B-C-...-팰린드롬-...-C역순-B역순-A역순** 이 되어야 한다.

따라서,

1. 팰린드롬은 1개 이상 있는지 확인: + 1개의 길이
(flag로 1번만 확인)
2. 각 문자열의 역순 문자열을 찾아 확인: + x * 2개의 길이 (문자열 + 역순문자열)

중복 방지를 위해 빈 문자열 처리, 이후 조건 1에 ""이 아닌 경우도 포함

## 코드
```python
# 19003
# 팰린드롬 문제

T = int(input())

for test_case in range(1,T+1):
    result = 0
    flag = 0
    n,m = map(int, input().split())
    s = [input() for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if s[i][::-1] == s[j] and i != j:
                result += 2*m
                s[i] = ""
            elif s[i] == s[i][::-1] and flag == 0 and s[i] != "":
                result += m
                flag = 1
    print(f"#{test_case} {result}")
```
> 출처: SWEA
> https://swexpertacademy.com/main/main.do