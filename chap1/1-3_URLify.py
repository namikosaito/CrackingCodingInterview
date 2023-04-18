# coding: utf_8

"""
文字列の空白を"%20"に置き換える。
入力は文字列と、空白を除いた文字の数。
ただし、元の文字列の後尾に十分なスペースがあるとする。

入力："Mr John Smith       ", 13
出力："Mr%20John%20Smith   "
"""

def urlify(string, length):
    char_list = list(string)
    index = len(char_list)
    
    for i in reversed(range(length)):
       if char_list[i] == " ":
            char_list[index - 3 : index] = "%20"
            index -= 3
       else:
           char_list[index - 1] = char_list[i]
           index -= 1       
            
    return "".join(char_list[index:])

if __name__ == "__main__":
    print(urlify("Mr John Smith       ", 13))