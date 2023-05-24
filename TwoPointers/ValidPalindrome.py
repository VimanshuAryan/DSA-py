# 125. valid palindrome
# 2 pointers basic question

s = "A man, a plan, a canal: Panama"

def palindrome (s):
    L, R = 0, len(s) - 1

    while L < R: 
        while L < R and not alphanum(s[L]): # alphanum becomes self.alphanum in leetcode editor
            L += 1
        while L < R and not alphanum(s[R]):
            R -= 1
        if s[L].lower() != s[R].lower():
            return False
        L, R = L + 1, R - 1
    return True

# function to check if char is alphanumeric or not
def alphanum (c): # add parameter self in leetcode editor
    return ((ord('A') <= ord(c) <= ord('Z')) or
            (ord('a') <= ord(c) <= ord('z')) or 
            (ord('0') <= ord(c) <= ord('9')))

print(palindrome(s))