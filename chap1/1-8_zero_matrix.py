# coding: utf-8
"""
MxNの行列について、要素が０であれば、その行と列の全てを０にする。
"""

def zero_matrix(mat):
    r = len(mat)
    c = len(mat[0])
    row = set()
    col = set()
    
    for x in range(r):
        for y in range(c):
            if mat[x][y] == 0:
                row.add(x)
                col.add(y)
    
    for x in range(r):
        for y in range(c):
            if (x in row) or (y in col):
                mat[x][y] = 0
                
    return mat

if __name__ == "__main__":
    test_cases = [
        (
            [
                [1, 2, 3, 4, 0],
                [6, 0, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 0, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [11, 0, 13, 14, 0],
                [0, 0, 0, 0, 0],
                [21, 0, 23, 24, 0],
            ],
        )
    ]
    
    for [mat, ground_truth] in test_cases:
        print("answer: ", zero_matrix(mat), " ground_truth: ", ground_truth)