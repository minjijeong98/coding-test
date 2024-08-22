####################################################
#                   문제 요구사항 요약                  #
####################################################
# 출처: https://www.acmicpc.net/problem/17219


####################################################
#                     작성한 풀이                     #
####################################################
import sys

N, M = map(int, input().split())
passwords = dict()
for i in range(N):
    key, val = sys.stdin.readline().rstrip().split()
    passwords[key] = val
for i in range(M):
    site_name = sys.stdin.readline().rstrip()
    print(passwords[site_name])

####################################################
#                    기억해둘 부분                    #
####################################################
