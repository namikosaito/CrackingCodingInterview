/****
 1_1 重複のない文字列
 ある文字列が全て固有（重複する文字が無い）かどうかを判定する
****/

#include <stdio.h>
#include <string>
#include <vector>
#include <iostream>
using namespace std;

bool isUniqueChar(string str){
    if(str.length() > 128)return false;

    vector<bool> char_set(128);
    for (int i = 0; i < str.length(); i++){
        int val = str[i];
        if (char_set[val]){
            return false;
        }
        char_set[val] = true;
    }
    return true;
}


int main() {

    cout << isUniqueChar("abcd") << endl;
    cout << isUniqueChar("hello") << endl;

    return 0;
}