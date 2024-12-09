# 문자열 뒤집기

## Information
- **link**: https://leetcode.com/problems/reverse-string/description/
- **category**: Two Pointers, String
- **reference**: 『파이썬 알고리즘 인터뷰(박상길)』 - 6장 문자열 조작
- **description**: 문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라.
- **to remember**: 


## Solution 1
### Intuition
- 리턴 없이 리스트 내부를 조작해야 하므로 `s[::-1]` 형식의 슬라이싱은 사용할 수 없음
- `for`문 이용해 하나씩 직접 바꿔주자: "Two Pointer를 이용한 Swap"

### Approach
1. 리스트를 절반만큼 나눈다
2. 대응되는 문자열 서로 바꿔서 저장

### Complexity
- Time complexity: $O(N)$
- Space complexity: $O(1)$

### Code
```python
def reverseString(self, s: List[str]) -> None:
    iters = len(s)//2
    for i in range(iters):
        s_i = s[i]
        s_i_reverse = s[-(i+1)]
        s[i] = s_i_reverse
        s[-(i+1)] = s_i

# 동일한 idea, 더 깔끔한 코드
def reverseString(self, s: List[str]) -> None:
    left, right = 0, len(s)-1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
```

## Solution 2. Pythonic Way
### Intuition
- `reverse()` 사용

### Approach
- `reverse()` 사용

### Complexity
- Time complexity: $O(N)$
- Space complexity: $O(1)$

### Code
```python
def reverseString(self, s: List[str]) -> None:
    s.reverse()
```