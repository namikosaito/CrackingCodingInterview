/****
 1_2 順列チェック
 二つの文字列が与えられた時に片方がもう片方の並び替えになっているかを判断
****/

#include <stdio.h>
#include <string>
#include <vector>
#include <iostream>
using namespace std;

bool OrderCheck(string &str1, string &str2){
    int n1 = str1.length();
    int n2 = str2.length();

    //同じ文字数ではなかったら
    if (n1 != n2)return false;

    sort(str1.begin(), str1.end());
    sort(str2.begin(), str2.end());

    for(int i = 0; i < n1; i++){
        if(str1[i] != str2[i])return false; 
    }
    return true;
}


int main() {

    string str1 = "testtest";
    string str2 = "ttsetset";

    if (OrderCheck(str1, str2)){
        cout << "Permutation!" <<endl;
    }
    else{
        cout << "NO" <<endl;
    }
    return 0;
}