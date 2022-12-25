# 167 Two sum 2 
numbers = [2,7,11,15]
target = 9

def twosum(numbers,target):
    l = 0
    r = len(numbers) - 1

    while l < r:
        curSum = numbers[l] + numbers[r]

        if curSum > target:
            r -= 1
        elif curSum < target:
            l += 1
        else:
            return [l+1, r+1]