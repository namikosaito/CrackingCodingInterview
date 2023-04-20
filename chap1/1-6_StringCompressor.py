# coding: utf_8

"""
文字の連続する文字列を数字を使って短縮して表現する
例
aabcccccaaならa2b1c5a2

ただし、もし数字を使った圧縮の方が長くなってしまうなら、元の文を返す
"""

def compress(string):
    answer = []
    counter = 0
    
    for i in range(len(string)):
        if i != 0 and string[i] != string[i-1]:
            answer.append(string[i-1] + str(counter))
            counter = 0
        counter += 1
        
    #最後の文字
    if counter:
        answer.append(string[-1] + str(counter))
        
    #短い方を返す
    return min(string, "".join(answer), key=len)

if __name__ == "__main__":
    test_cases = [
        ("aabcccccaaa", "a2b1c5a3"),
        ("abcdef", "abcdef"),
        ("aabb", "aabb"),
        ("aaa", "a3"),
        ("a", "a"),
        ("", ""),
    ]
    
    for [string, ground_truth] in test_cases:
        print("answer:", compress(string), "   ground truth:", ground_truth)
            