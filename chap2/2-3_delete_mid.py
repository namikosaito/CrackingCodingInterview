# coding: utf-8
"""
連結リストにおいて、間の要素が与えられて、それだけ削除する
"""

def del_mid(lis, mid):
    answer = []
    mid_num = len(mid)
    
    for i in range(len(lis)):
        
        if lis[i] == mid[0]:
            mid_num -= 1
        elif 0 != mid_num != len(mid):
            mid_num -= 1
        else:
            answer.append(lis[i])
    return answer


if __name__ == "__main__":
    test_cases = (
    # list, delete, expected
    (("a", "b", "c", "d", "e"), ("c"), ("a", "b", "d", "e")),
    (("a", "b", "c", "d", "e"), ("c", "d"), ("a", "b", "e")),
    (("a", "b", "c", "d", "e"), ("c", "d", "e"), ("a", "b")),
    )
    
    for [lis, mid, ground_truth] in test_cases:
        print("answer: ", del_mid(lis, mid), " ground_truth:", ground_truth)