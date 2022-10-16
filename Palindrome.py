#9 Palindrome
x = 121

rev = 0
temp = x

while temp > 0:
    y = temp%10
    rev = rev*10 + y
    temp = temp//10

    if rev==x:
        print (True)
