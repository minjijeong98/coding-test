# [Bronze 5] 2741 N찍기
- 문제 링크: https://www.acmicpc.net/problem/10951
- 분류: 수학, 구현, 사칙연산

## 문제 설명
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

## 입력
입력은 여러 개의 테스트 케이스로 이루어져 있다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

## 출력
각 테스트 케이스마다 A+B를 출력한다.

## 알게 된 점
```python
import sys
input = sys.stdin.readline()  # 한 줄만 읽어온다. 개행문자(\n) 포함됨
input = sys.stdin.readlines()  # 파일의 끝까지 한번에 읽어온다. 각 줄이 개행문자(\n)가 포함되어 리스트로 저장됨
input = sys.stdin.read() # 파일의 끝까지 한번에 읽어온다.
input = sys.stdin.read().splitlines()  # 파일의 끝까지 한번에 읽어오고 개행문자를 제외해 리스트로 읽음
```