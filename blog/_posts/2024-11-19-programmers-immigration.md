---
title: "[Programmers] 입국심사 - Python"
date: 2024-11-19 16:00:00 +0900
categories: [Algorithm]
tags: [Python, Algorithm]
---

## 풀이

시간이 기준이 아니라, 사람 수가 기준
사람 수(n)를 만족하는 시간의 최솟값 찾기

가능한 시간의 범위에서 이진 탐색,
끝 값은 가장 오래 걸리는 심사관이 모든 인원을 심사하는 경우

- `passenger += mid // x`
	통과하는 사람 수:  최대한 심사관이 계속 심사하는 경우, 시간을 추가하면서 가능한 심사관을 고려하지 않고, 시간을 줄이면서 가능한 사람 수를 고려
- `passenger >= n`
	사람 수 n을 만족하면서, 최솟값이 아닐 수 있으므로 계속 범위를 좁혀주기

## 코드

```python
def solution(n, times):
    # 심사시간 정렬
    times.sort()
    answer = 0
    # 시작, 끝 값 설정
    start = 1
    end = n*times[-1]
    # 조건에 맞는 값 찾기 (이진탐색)
    while start <= end:
        mid = (start + end) // 2
        passenger = 0
        for x in times:
            passenger += mid // x
            # 반복 중 조건 불만족 시 반복 중지
            if passenger > n:
                break
        if passenger >= n:
            answer = mid
            end = mid-1
        else:
            start = mid+1
    return answer
```

> 출처: 프로그래머스 코딩 테스트 연습
> https://school.programmers.co.kr/learn/courses/30/lessons/43238