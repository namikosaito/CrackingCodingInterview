# coding: utf-8
"""
リストの最後からk個目を出力
"""

def Klast(lis, k):
    return lis[len(lis)-k]

if __name__ == "__main__":
    test_cases = (
    # list, k, expected
    ((10, 20, 30, 40, 50), 1, 50),
    ((10, 20, 30, 40, 50), 5, 10),
    )
    
    for [lis, k, ground_truth] in test_cases:
        print("answer: ", Klast(lis, k), " ground_truth:", ground_truth)