# coding: utf-8
import random
"""
深さのリスト
二分探索木が与えられたとき、同じ深さのノード同士の連結リストを作るアルゴリズム
"""

map = {}

class Node:
    def __init__(self, data):
        self.data = data
        self.right:Node = None
        self.left:Node = None
        
class BinaryTree:
    def __init__(self, root=None):
        self.root:Node = root
        
    def print_node(self, n:Node):
        if n!= None:
            self.print_node(n.left)
            print(n.data)
            self.print_node(n.right)
            
    def print_tree(self):
        self.print_node(self.root)
        
def create_minimal_bst(arr, start, end):
    if start > end:
        return None
    mid = int((start+end)/2)
    n = Node(data = arr[mid])
    n.left = create_minimal_bst(arr, start, mid-1)
    n.right = create_minimal_bst(arr, mid+1, end)
    return n

def get_depth(root:Node):
    if root == None:
        return 0
    val = 1 + max(get_depth(root.right), get_depth(root.left))
    if map.get(val) == None:
        map[val] = [root.data]
    else:
        map[val].append(root.data)
    return val
    

if __name__ == "__main__":
    arr = [random.randint(0,100) for _ in range(17)]
    arr.sort()
    n = create_minimal_bst(arr,0,len(arr)-1)
    print(get_depth(n))
    print(map)
    tree = BinaryTree(root=n)