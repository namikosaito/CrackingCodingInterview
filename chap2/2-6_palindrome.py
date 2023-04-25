# coding: utf-8
"""
回文かどうかをチェックする
"""

def palindrome(lis):
    answer = True
    for i in range(len(lis)//2):
        if lis[i] != lis[len(lis) - 1 - i]:
            answer = False
    return answer

if __name__ == "__main__":
    test_cases = [
    ([1, 2, 3, 4, 3, 2, 1], True),
    ([1], True),
    (["a", "a"], True),
    ("aba", True),
    ([], True),
    ([1, 2, 3, 4, 5], False),
    ([1, 2], False),
    ]
    
    for [lis, ground_truth] in test_cases:
        print("answer: ", palindrome(lis), " gound_truth: ", ground_truth)