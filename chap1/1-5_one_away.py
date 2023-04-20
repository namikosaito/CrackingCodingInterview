# coding: utf_8

"""
文字列に対して、文字の挿入、削除、置き換えだけでもう一方の文字列に変換できるかどうか
"""

def check(text_1, text_2):
    if len(text_1) == len(text_2):
        return replace(text_1, text_2)
    elif len(text_1) + 1 == len(text_2):
        return insert_delete(text_1, text_2)
    elif len(text_1) - 1 == len(text_2):
        return insert_delete(text_2, text_1)

def replace(text_1, text_2):
    answer = False
    for t1, t2 in zip(text_1, text_2):
        if t1 != t2:
            if answer:
                return False
            answer = True
    return True

def insert_delete(text_1, text_2):
    answer = False
    i, j = 0, 0
    while i < len(text_1) and j < len(text_2):
        if text_1[i] != text_2[j]:
            if answer:
                return False
            answer = True
            j += 1
        else:
            i += 1
            j += 1
    return True

if __name__ == "__main__":
    test_cases = [
        # no changes
        ("pale", "pale", True),
        ("", "", True),
        # one insert
        ("pale", "ple", True),
        ("ple", "pale", True),
        # one replace
        ("pale", "bale", True),
        ("a", "b", True),
        # multiple replace
        ("pale", "bake", False),
        # insert and replace
        ("pale", "pse", False),
        # permutation with insert shouldn't match
        ("ale", "elas", False),
    ]
    
    for [text_1, text_2, ground_truth] in test_cases:
        print("answer:", check(text_1, text_2), "   ground truth:", ground_truth)
            