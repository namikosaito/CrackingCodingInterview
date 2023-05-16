# coding:utf-8
"""
ある整数があり、その中の１ビットだけ０から１に反転することができる。
１の並びが最も長くなる時の長さは？
"""

def flip(num):
    num_str = bin(num)[2:]
    max_cnt, cnt, cnt0 = 0, 0, 0
    i = len(num_str)
    
    while i:
        # もし１なら
        if int(num_str[i-1]):
            cnt += 1
        # もし０なら
        else:
            # 0が出てくるのが初回だったら
            if cnt0 == 0:
                temp_i = i
                cnt0 = 1
            # 0が出てくるのが２回目連続以降なら、
            else:
                max_cnt = max(cnt, max_cnt)
                i = temp_i
                cnt0 = 0
                cnt = 0
        i -= 1
        
    max_cnt = max(cnt, max_cnt)
    
    return max_cnt + 1
    

if __name__ == "__main__":
    test_cases = [
    (0b0, 1),
    (0b111, 4),
    (0b10011100111, 4),
    (0b10110110111, 6),
    (0b11011101111, 8),
    ]
    for num, ground_truth in test_cases:
        print("answer: ", flip(num), ", ground truth: ", ground_truth)