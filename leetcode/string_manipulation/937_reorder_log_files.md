# 로그 파일 재정렬

## Information
- **link**: https://leetcode.com/problems/reorder-data-in-log-files/description/
- **category**: Array, String, Sorting
- **reference**: 『파이썬 알고리즘 인터뷰(박상길)』 - 6장 문자열 조작
- **description**: 로그를 재정렬하라. 기준은 다음과 같다.
    1. 로그의 가장 앞 부분은 식별자다
    2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다
    3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다
    4. 숫자 로그는 입력 순서대로 한다 
- **to remember**: sort 시 후순위 정렬 기준은 튜플로 함께 넣어줄 수 있다


## Solution
### Intuition
- 식별자와 나머지 부분을 분리하고 if문을 이용해 조건에 따라 처리한다

### Approach
1. digit과 letter 로그를 분리한다
2. sort() 함수를 이용해 정렬하고 결과를 합친다

### Code
```python
def reorderLogFiles(self, logs: List[str]) -> List[str]:
    digits, letters = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    result = letters + digits
    return result
```
