---
title: "[SWEA] 1215. [S/W 문제해결 기본] 3일차 - 회문1 - Python"
date: 2024-09-25 16:00:00 +0900
categories: [Algorithm]
tags: [Python, Algorithm]
---

## 풀이
배열을 순회하면서, 주어진 길이의 문자열을 찾아 회문인지 확인한다.
배열을 전치시켜 행과 열을 뒤집고 다시 배열을 순회하며 회문 조건을 만족하는 지 확인한다.

**`list(zip(*arr))`**

1. `*` 연산자를 사용하여 배열(arr)을 언패킹(unpacking)한다.
    ```python
    # 예)
    arr = ["ABC",
        "DEF",
        "GHI"]

    print(*arr) # ABC DEF GHI
    ```
2. `zip()` 을 통해 각 원소의 동일한 위치(인덱스)끼리 묶어준다. (`zip()`은 iterable(반복가능, 순차접근가능)한 객체에 사용가능하므로, string으로 이루어진 배열에 적용했다.)

3. zip 객체인 상태에서 `list()` 를 사용하여 리스트로 변환, 배열이 전치된 형태로 반환된다.
    ```python
    # 예) 
    zip(*arr) # zip 객체, list 변환 필요
    list(zip(*arr))
    # [("A","D","G"),
    #  ("B","E","H"),
    #  ("C","F","I")]
    ```



## 코드
```python
# 1215
# [S/W 문제해결 기본] 3일차 - 회문1

for test_case in range(1,11):
    n = int(input())
    arr = [input() for _ in range(8)]
    result = 0
    for i in range(8):
        for j in range(8-n+1):
            if arr[i][j:j+n] == arr[i][j:j+n][::-1]:
                result += 1
    t_arr = list(zip(*arr))
    for i in range(8):
        for j in range(8-n+1):
            if t_arr[i][j:j+n] == t_arr[i][j:j+n][::-1]:
                result += 1
    print(f"#{test_case} {result}")

```
> 출처: SWEA
> https://swexpertacademy.com/main/main.do