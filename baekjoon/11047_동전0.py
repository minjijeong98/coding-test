####################################################
#                   문제 요구사항 요약                  #
####################################################

# 필요한 동전 개수의 최솟값 구하기



####################################################
#                     작성한 풀이                     #
####################################################

import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
inputs = [int(a.rstrip()) for a in sys.stdin.readlines()]    # 또는 다음 줄처럼도 가능
# inputs = [int(a) for a in sys.stdin.read().splitlines()]   # 위와 동일한 기능
inputs.sort()
coin = 0
while K > 0:
    val = inputs.pop()
    cnt_tmp = K // val
    coin += cnt_tmp
    K -= cnt_tmp * val
print(coin)



####################################################
#                    기억해둘 부분                    #
####################################################

# 첫번째 줄에서 rstrip() 안써도 문제 없었다: int() 적용 시 개행문자 자동으로 탈락되기 떄문. 예를 들어, int('3\n')은 int('3')과 동일하게 3의 결과 낸다.
# stdin에서 문자열을 읽어오는 다양한 방법 존재한다. 이 중 문제 상황에 가장 적합한 것 사용하자. 여기에서는 굳이 for문 써서 한줄씩 읽을 필요 없을 것 같아 readlines 사용했다.
    # sys.stdin.readline(): 개행문자 '\n' 포함해서, 한 줄만 입력받음
    # sys.stdin.readlines(): 각 줄에 개행문자 '\n' 포함되어, 끝까지 모든 줄 입력받음. 각 줄은 리스트 형태로 저장
    # sys.stdin.read(): 파일 끝까지 한번에 읽어옴
# split()과 splitlines() 차이
    # split()은 delimiter, 즉 특정한 구분자(공백 등)를 기준으로 나누는데 사용되고
    # splitlines()는 개행 문자를 기준으로 나눔 (줄바꿈 기준)

# 참고: https://velog.io/@nang_zz/Python-sys.stdin.readline-readlines-read-%EC%B0%A8%EC%9D%B4
