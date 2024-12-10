# 가장 흔한 단어

## Information
- **link**: https://leetcode.com/problems/most-common-word/description/
- **category**: Array, Hash Table, String, Counting
- **reference**: 『파이썬 알고리즘 인터뷰(박상길)』 - 6장 문자열 조작
- **description**: 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며, 구두점(마침표, 쉼표 등) 또한 무시한다.
- **to remember**: 


## Solution
### Intuition
- `collections.Counter()`를 이용해 딕셔너리로 변환해 최빈 단어 도출한다.

### Approach
1. 영문자만 남기고 모두 소문자로 변환한다
2. 금지된 단어를 `""`으로 바꾸고, 띄어쓰기 기준으로 split해 리스트로 변환한다
3. 해당 리스트를 `collections.Counter()`를 이용해 딕셔너리로 변환해 최빈 단어 도출한다.

### Code
```python
def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    paragraph = paragraph.lower()
    paragraph = re.sub("[^a-z]", " ", paragraph)
    for ban_word in banned:
        paragraph = paragraph.replace(ban_word + " ", "")
    bow = paragraph.split()

    bow_counter = collections.Counter(bow)
    max_value = max(list(bow_counter.values()))
    frequent_word = [key for key, value in bow_counter.items() if bow_counter[key] == max_value]
    return frequent_word[0]

# 동일 로직, 더 간단한 풀이
def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    words = [word.lower() for word in re.sub("[^\w]", " ", paragraph).split() if word.lower() not in banned]
    words_dict = collections.Counter(words)
    return words_dict.most_common(1)[0][0]
    # return max(words_dict, key=words_dict.get)  # get: argmax의 기능
```
