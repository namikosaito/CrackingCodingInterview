# coding: utf-8

"""
行列の回転。
NxNの行列に描かれた１つのピクセルが４biteの画像がある。この画像を90度回転させるには？
NxNの外側からロールケーキのように処理していく・・
"""

def rotate_matrix(mat):
    n = len(mat)
    
    for layer in range(n//2):
        first, last = layer, n-layer-1
        for i in range(first, last):
            # save top
            top = mat[layer][i]
            
            # left->top
            mat[layer][i] = mat[-i-1][layer]
            
            # bottom->left
            mat[-i-1][layer] = mat[-layer-1][-i-1]
            
            # right->bottom
            mat[-layer-1][-i-1] = mat[i][-layer-1]
            
            # top->right
            mat[i][-layer-1] = top
            
    return mat

if __name__ == "__main__":
    test_cases = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
        (
            [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [21, 16, 11, 6, 1],
                [22, 17, 12, 7, 2],
                [23, 18, 13, 8, 3],
                [24, 19, 14, 9, 4],
                [25, 20, 15, 10, 5],
            ],
        ),
    ]
    
    for [mat, ground_truth] in test_cases:
        print("answer: ", rotate_matrix(mat), " gound truth: ", ground_truth)