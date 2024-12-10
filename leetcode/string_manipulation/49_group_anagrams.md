# 그룹 애너그램

## Information
- **link**: https://leetcode.com/problems/group-anagrams/description/
- **category**: Array, Hash Table, String, Sorting
- **reference**: 『파이썬 알고리즘 인터뷰(박상길)』 - 6장 문자열 조작
- **description**: 문자열 배열을 받아 애너그램 단위로 그룹핑하라.
- **to remember**: 


## Solution
### Intuition
- 딕셔너리 객체로 만들고 value 값을 반환한다.

### Approach
1. 문자열 각각을 오름차순 정렬해 unique한 문자열을 남기고, 이를 딕셔너리 Key로 설정한다
2. for문으로 애너그램들을 모은다 (`append`)
3. 딕셔너리의 value 값들을 모아 리스트로 반환한다.

### Code
```python
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    str_unique = set(["".join(sorted(string, reverse=False)) for string in strs])
    anagrams = {key:[] for key in str_unique}  # defaultdict를 사용할 수도 있음
    for string in strs:
        key = "".join(sorted(string, reverse=False))
        anagrams[key].append(string)
    return list(anagrams.values())
```
