---
title: "[Programmers] 더 맵게 - Python"
date: 2024-11-15 16:00:00 +0900
categories: [Algorithm]
tags: [Python, Algorithm]
---

## 풀이

모든 음식의 스코빌지수가 K 이상이 되도록 "섞기" 반복

1. 스코빌지수들을 heap 자료구조로 표현
2. 최소힙 자료구조로, 0번째 원소가 가장 작은 원소
3. 0번째 원소가 K 이상이 되면 모든 음식의 스코빌지수 > K 이므로 0번째 원소를 조건으로 "섞기" 반복
4. 섞기 : 가장 작은 값, 두 번째로 작은 값을 각각 `heappop`, 계산 결과 값을 다시 `heappush`
5. 모든 원소가 K 이상으로 만들 수 없을 때: 
	"섞기"를 반복하면 2개의 값을 더해 1개의 값으로 변환,
    원소의 개수가 줄어들기 때문에 결국 1개의 값이 남을 때 반복이 종료되고 1개의 값이 K 이상이 아닌 경우가 됨


## 코드
```python
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) == 1:
            answer = -1
            break
        heapq.heappush(scoville, heapq.heappop(scoville) + 2*heapq.heappop(scoville))
        answer += 1
    return answer
```

> 출처: 프로그래머스 코딩 테스트 연습
> https://school.programmers.co.kr/learn/courses/30/lessons/42626
