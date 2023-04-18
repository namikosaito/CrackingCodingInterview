# coding: utf_8

"""
入力された文字列が回分ができるものならTrueを返す
"""

def Palindrome(string):
    count = [0 for _ in range(ord("z") - ord("a") + 1)]
    odd_num = 0
    for c in string:
        check_num = char_num(c)
        if check_num != -1:
            count[check_num] += 1
            if count[check_num] % 2:
                odd_num += 1
            else:
                odd_num -= 1
    return odd_num < 1

def char_num(c):
    a = ord("a")
    z = ord("z")
    val = ord(c)
    
    if a <= val <= z:
        return val - a
    
    return -1

if __name__ == "__main__":
    print(Palindrome("countcount"))
    print(Palindrome("countcount2"))
    print(Palindrome("countcountw2"))