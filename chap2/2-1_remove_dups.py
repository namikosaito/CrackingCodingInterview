# coding: utf-8
"""
ソートされていない連結リストから、重複する要素を削除するコードを書く
[発展]一時的なバッファを使わない
""" 

# 計算時間　O(N)
def remove_dups(lis):
    seen = set()
    
    for x in lis:
        if x in seen:
            pass
        else:
            seen.add(x)
    return seen

# 消費メモリO(1), 計算時間 O(N^2)
def remove_dups_sol2(lis):
    seen = set()
    for i in range(len(lis)):
        seen_flag = False
        for j in range(len(lis) - i - 1):
            #print(lis[i], lis[j])
            if lis[i] == lis[i + j + 1]:
                seen_flag = True
        if seen_flag == False:
            seen.add(lis[i])
    return seen


if __name__ == "__main__":
    test_cases = (
    ([], []),
    ([1, 1, 1, 1, 1, 1], [1]),
    ([1, 2, 3, 2], [1, 2, 3]),
    ([1, 1, 2, 3], [1, 2, 3]),
    ([1, 2, 3], [1, 2, 3]),
    )
    
    for [lis, ground_truth] in test_cases:
        print("answer: ", remove_dups(lis), "ground truth: ", ground_truth)
        print("answer_sol2: ", remove_dups_sol2(lis), "ground truth: ", ground_truth)
        
