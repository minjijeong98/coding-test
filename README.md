# Coding-Test Study
- 알고리즘과 자료구조 학습 및 코딩테스트 문제 풀이 기록을 위한 저장소입니다.
- 꾸준한 문제 풀이를 목표로 합니다.
- **언어**: Python
- **기간**: 2024.10.31 ~ ongoing
- **참고자료**
    - 책: [파이썬 알고리즘 인터뷰](https://github.com/onlybooks/python-algorithm-interview) | [알고리즘 문제 해결 전략](https://product.kyobobook.co.kr/detail/S000001032946)
    - 사이트: [백준](https://solved.ac/) | [LeetCode](https://leetcode.com/) | [Programmers](https://programmers.co.kr/)

## Naming Convention

1. **폴더 생성**: `{난이도}_{문제번호}_{문제명}`
   - 예시: `S4_11047_동전0`
2. **문제별 README** (`README.md`)
    - 포함 내용: 문제 링크, 분류, 문제 설명, 입력, 출력, 풀이 접근법, 알게 된 점
3. **풀이 파일**: `{난이도}_{문제번호}_{문제명}.py`
    - 예시: `S4_11047_동전0.py` 

```text
# 예시 구조
baekjoon
└── S4_11047_동전0
    ├── README.md
    └── S4_11047_동전0.py
```

## Commit Convention

- 커밋 메시지 형식
    - 제목: `[문제출처] 난이도 | 문제명 | 소요시간`
    - 본문: `문제 링크`
- 문제 출처 약어
	- `[BOJ]`: 백준
	- `[PGS]`: 프로그래머스
	- `[LTC]`: 리트코드
	- `[CFS]`: 코드포스
	- `[SEA]`: 삼성SW Expert Academy
	- `[ETC]`: 그 외

```bash
# 커밋 예시
git commit -m "[BOJ] S4 | 동전0 | 5분" -m "https://www.acmicpc.net/problem/11047"
```

## Reference
- [challenge100-codingtest-study](https://github.com/ellynhan/challenge100-codingtest-study)
- [coding-test](https://github.com/wogkr810/coding-test)
