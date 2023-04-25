# coding: utf-8
"""
1の位、10の位、100の位の順番に二つのリストが入力される。
1の位、10の位、100の位の順番に和をリストで返す。
"""

def list_sum(lis_1, lis_2):
    lis_sum = lis_1[0] + lis_2[0] + lis_1[1] * 10 + lis_2[1] * 10 + lis_1[2] * 100 + lis_2[2] * 100
    ans_100 = lis_sum // 100
    ans_100_left = lis_sum % 100
    ans_10 = ans_100_left // 10
    ans_1 = ans_100_left % 10
    return [ans_1, ans_10, ans_100]

def list_sum_sol2(lis_1, lis_2):
    ans_1 = (lis_1[0] + lis_2[0])
    if ans_1 >= 10:    
        ans_10 = (1+ lis_1[1] + lis_2[1])
    else:
        ans_10 = (lis_1[1] + lis_2[1])
    if ans_10 >= 10:
        ans_100 = (1+ lis_1[2] + lis_2[2])
    else:
        ans_100 = (lis_1[2] + lis_2[2])
    return [ans_1 % 10, ans_10 % 10, ans_100]
    
        
    

if __name__ =="__main__":
    test_cases = (
    # all values can either be list of integer or integers
    # a, b, expected_sum
    ([7, 1, 6], [5, 9, 2], [2, 1, 9]),
    ([3, 2, 1], [3, 2, 1], [6, 4, 2]),
    )
    
    for [lis_1, lis_2, ground_truth] in test_cases:
        print("answer: ", list_sum(lis_1, lis_2), " ground truth: ", ground_truth)
        print("answer_sol2: ", list_sum_sol2(lis_1, lis_2), " ground truth: ", ground_truth)