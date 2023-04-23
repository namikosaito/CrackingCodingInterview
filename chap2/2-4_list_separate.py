# coding: utf-8
"""
リストの分割。リストと数字が与えられて、数字より小さい要素は前半、大きい要素は後半に来るように並べ替える。
"""

def list_separate(lis, k):
    former = []
    latter = []
    for i in range(len(lis)):
        if lis[i] < k:
            former.append(lis[i])
        else:
            latter.append(lis[i])
    former += latter
    return former

if __name__ == "__main__":
    test_cases = (
        ([3, 5, 8, 5, 10, 2, 1], 5, [3, 2, 1, 5, 8, 5, 10]),
        ([3, 5, 8, 5, 10, 2, 1], 2, [1, 3, 5, 8, 5, 10, 2]),
    )
    
    for [lis, k, answer] in test_cases:
        print("answer: ", list_separate(lis, k), " sample answer: ", answer)