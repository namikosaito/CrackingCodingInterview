# coding:utf-8
"""
how many bit is needed to exchange int A->B?
"""

def bit_change(A:int, B:int):
    count, c = 0, A ^ B
    while c:
        print(bin(c), bin(c-1))
        count, c = count + 1, c & (c-1)
    return count

def bit_change2(A:int, B:int):
    count, c = 0, A ^ B
    while c:
        print(bin(c))
        c = c >> 1
        count += c & 1
    return count

if __name__ == "__main__":
    a = 0b11101 # 29
    b = 0b01111 # 15
    print("answer: ", bit_change(a, b))
    print("answer: ", bit_change2(a, b))