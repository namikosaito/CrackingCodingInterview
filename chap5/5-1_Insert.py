# coding:utf-8
"""
最大32ビットの整数NとM、ビットの位置を指す値iとjが与えられている。
この時、Nのjビット目からiビット目をMを挿入する
ただし、jとiの幅はMのビット数と一致している。
例) 
入力 N=10000000000, M=10011, i=2, j=6
出力 N=10001001100
"""

def insert(n, m, i, j):
    # Nと同じ大きさで、j〜iだけ０で他が１のマスクをNに被せて、その後にMと合体
    
    #全てが１のビット列を
    ones_left = -1 << (j + 1)
    ones_right = (i << i) -1
    print("left, right=", bin(ones_left), bin(ones_right))
    mask = ones_left | ones_right
    cleared = n & mask
    print("mask, clear = ",bin(mask),bin(cleared))
    moved_m = m << i
    return bin(cleared | moved_m)

if __name__ == "__main__":
    test_cases = [
    ((int("10000000000", 2), int("10011", 2), 2, 6), int("10001001100", 2)),
    ((int("11111111111", 2), int("10011", 2), 2, 6), int("11111001111", 2)),
    ]
    
    for [(n, m, i, j), ground_truth] in test_cases:
        print("answer: ", insert(n, m, i, j), "ground truth: ", bin(ground_truth))
        
