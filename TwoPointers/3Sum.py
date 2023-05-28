# 15 3sum 2 pointer question

nums = [-1,0,1,2,-1,-4]

def sum(nums):
    nums.sort()
    res = []

    for i, a in enumerate(nums):

        # l and r need to be defined locally and not globally
        l,r = i+1, len(nums) - 1

        # if curr value a is same the prev value a then continue with the next iteration of the loop
        # because we don't want duplicates
        if i > 0 and nums[i-1] == a:
            continue

        while l<r:
            threeSum = a + nums[l] + nums[r]
            if threeSum > 0:
                r-=1
                print('>')
            elif threeSum < 0:
                l+=1
                print('<')
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                print('perfect')
                # we don't want duplicate 2 sum solution so if the value after shifting the ptr is same, we shift it again.
                while nums[l] == nums[l-1] and l<r:
                    l+=1
    return res

print(sum(nums))