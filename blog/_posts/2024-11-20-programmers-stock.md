---
title: "[Programmers] 주식가격 - Python"
date: 2024-11-20 16:00:00 +0900
categories: [Algorithm]
tags: [Python, Algorithm]
---

## 풀이

배열을 순회하여 각 원소에 대해 원소보다 작은 값이 나타나면
값이 떨어진 것이므로, 작은 값이 나타나기 전까지의 시간을 저장한다.

## 코드

```python
def solution(prices):
    answer = []
    for i in range(len(prices)):
        sec = 0
        for j in range(i+1,len(prices)):
            sec += 1
            if prices[i] > prices[j]:
                break       
        answer.append(sec)
    return answer
```

> 출처: 프로그래머스 코딩 테스트 연습
> https://school.programmers.co.kr/learn/courses/30/lessons/42584
