#739 Daily Temperature
# stack 
# easy: do it yourself
# hint monotonically dec stack

temp = [30,40,50,60]
res = []

for i in range(len(temp)-1):
    j = i + 1
    while temp[i] > temp[j] and 3 > j :
        j+=1
    res.append(j-i)
res.append(0)
print(res)

class Solution:
    def dailyTemperatures(self, temperatures):
        res = [0]*len(temperatures)
        stack = []

        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append([t,i])
        return res