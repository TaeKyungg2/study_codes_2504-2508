import math


def solution(nums):
    answer = 0
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if isPrime(nums[i] + nums[j] + nums[k]):
                    answer += 1

    return answer


def isPrime(num):
    if num < 2:
        return False
    for i in range(2, math.ceil(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


print(solution([1, 2, 7, 6, 4]))
