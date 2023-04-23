# coding: utf-8

"""
一方の文字列を順番そのままで一部を組み替えると、もう一方の文字列になっているか。
"""

def string_rotation(text_1, text_2):
    if len(text_1) == len(text_2) != 0:
        return text_1 in text_2 * 2
    return False

if __name__ == "__main__":
    test_cases = [
        ("waterbottle", "erbottlewat", True),
        ("abcd", "amkmk", False),
        ("aaa", "aaa", True),
    ]

    for [text_1, text_2, ground_truth] in test_cases:
        print("answer: ", string_rotation(text_1, text_2), " ground_truth:", ground_truth)