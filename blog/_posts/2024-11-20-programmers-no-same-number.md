---
title: "[Programmers] 같은 숫자는 싫어 - Python"
date: 2024-11-20 16:00:00 +0900
categories: [Algorithm]
tags: [Python, Algorithm]
description: "Programmers '같은 숫자는 싫어' 문제 풀이를 정리했습니다."
---


## 풀이
연속하는 숫자는 하나만 남기되 
입력받은 배열 원소들의 순서를 유지해야 하므로, 
배열을 순회하며 **현재 원소와 이전 원소를 비교**하고, 다를 경우 반환 리스트에 추가하는 방법으로 해결했다.




## 코드
```python
def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1,len(arr)):
        if arr[i-1] != arr[i]:
            answer.append(arr[i])
    return answer
```

> 출처: 프로그래머스 코딩 테스트 연습
> https://school.programmers.co.kr/learn/courses/30/lessons/12906