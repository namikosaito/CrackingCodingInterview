# coding: utf-8
"""
0から1までのdoubleの実数を二進数で表記する
32文字以内で表記できない時はERRORと出力
"""

def bin_to_string(num):
    bit_str = "."
    if num > 1.0 or num < 0.0:
        return "ERROR"
        
    while num > 0:
        if len(bit_str) > 32:
            return bit_str
        
        # 2倍して１以上になるか
        twice = num * 2
        if twice >= 1:
            bit_str += "1"
            num = twice    
        else:
            bit_str += "0"
            num = twice 
    # 0で埋める
    return bit_str.ljust(33, "0")
         
    

if __name__ == "__main__":
    for num in [0.625, 0, 0.1, 0.101, 0.2, 0.5, 1, 2]:
        bit_str = bin_to_string(num)
        response = bit_str if len(bit_str) <= 33 else "ERROR"
        print(f"Input:{num}, Binary:{response}")