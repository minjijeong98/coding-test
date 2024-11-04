nums = list(map(int, input().split()))
result = 0
for i in range(len(nums)):
    num = nums[i] % 10
    result += (num*num % 10)
print(result % 10)