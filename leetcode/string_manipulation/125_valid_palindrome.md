# 유효한 팰린드롬

## Information
- **link**: https://leetcode.com/problems/valid-palindrome/
- **category**: Two Pointers, String
- **reference**: 『파이썬 알고리즘 인터뷰(박상길)』 - 6장 문자열 조작
- **description**: 주어진 문자열이 팰린드롬인지 확인한다. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.
- **to remember**: 대부분의 문자열 작업은 슬라이싱으로 처리하는 편이 가장 빠름

## Solution 1
### Intuition
- 리스트로 변환, 슬라이싱 사용

### Approach
1. alphanumeric 문자열만을 추출해 소문자로 변환 후 리스트에 저장
   - `char.isalnum()`, `char.lower()`
2. 리스트를 공백 없이 하나의 문자열로 결합
3. 2의 문자열 뒤집어서 팰린드롬 판별

### Complexity
- Time complexity: $O(N)$
- Space complexity: $O(N)$

### Code
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # alphanumeric 문자열만을 추출해 소문자로 변환 후 리스트에 저장
        alnum_list = []
        for i in range(len(s)):
            if s[i].isalnum():
                alnum_list.append(s[i].lower())

        # 결합
        alnum = "".join(alnum_list)

        # palindrome 판별
        if alnum == alnum[::-1]:
            return True
        else:
            return False
```


## Solution 2
### Intuition
- 정규표현식, 슬라이싱

### Approach
1. 정규표현식으로 불필요한 문자열 필터링
   - `[^0-9a-z]`: 0-9 및 a-z를 제외한 문자
   - 정규표현식 참고: https://hamait.tistory.com/342
2. 1의 문자열 뒤집어서 팰린드롬 판별

### Complexity
- Time complexity: $O(N)$
- Space complexity: $O(N)$

### Code
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 정규표현식으로 불필요한 문자열 필터링
        s = s.lower()  # 소문자로 변환
        s_cleaned = re.sub("[^0-9a-z]","",s)

        # 결과 반환
        return s_cleaned == s_cleaned[::-1]
```