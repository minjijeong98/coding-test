# 가장 긴 팰린드롬 부분 문자열

## Information
- **link**: https://leetcode.com/problems/longest-palindromic-substring/
- **category**: Two Pointers, String, Dynamic Programming
- **reference**: 『파이썬 알고리즘 인터뷰(박상길)』 - 6장 문자열 조작
- **description**: 가장 긴 팰린드롬 부분 문자열을 출력하라.
- **to remember**
    - Longest Common Substring 문제는 DP의 전형적인 예시이다.
    - 이 문제는 DP로 풀 수 있지만, two-pointer로 푸는게 더 간단하다


## Solution 1 -> 시간 초과
### Intuition
- 뒤집어서 겹치는 부분 찾기

### Approach
1. 뒤집어서 겹치는 부분을 찾는다
2. 이들 중 팰린드롬만을 남긴다
3. 가장 길이가 긴 팰린드롬을 반환한다

### Code
```python
# 시간 제한 초과..
def longestPalindrome(self, s: str) -> str:
    s_inverse = s[::-1]
    candidates = []
    for i in range(len(s)):
        for j in range(len(s_inverse)):
            candi = ""
            i2, j2 = i, j
            while s[i2] == s_inverse[j2]:
                candi += s[i2]
                if candi not in candidates:
                    candidates.append(candi)
                i2+=1
                j2+=1
                if (i2 == len(s)) or (j2 == len(s)):
                    break
            
    # 팰린드롬 찾기
    palindrome = [word for word in candidates if word == word[::-1]]
    
    # 가장 긴 팰린드롬 반환
    palindrome.sort(key=len, reverse=True)
    return palindrome[0]
```

- two pointer 기반 문제 풀이 방식 추가 필요