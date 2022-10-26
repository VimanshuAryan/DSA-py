# 70 climbing stairs 
# DP / memoization

def climb(n):

    one, two = 1, 1

    for i in range(n-1) :

        temp = one
        one = one + two
        two = temp

    return one

print(climb(5))
