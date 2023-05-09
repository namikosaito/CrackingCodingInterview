# coding: utf-8
"""
平衡チェック：二分木が平衡かどうかを調べる関数を実装する
平衡木とは、全てのノードが持つ二つの部分木について、その高さの差が１であるような木
"""
import random

class Node:
    def __init__(self, data):
        self.data = data
        self.right:Node = None
        self.left:Node = None
        
class BinaryTree:
    def __init__(self, root = None):
        self.root:Node = root
        
    def print_node(self, n:Node):
        if n != None:
            self.print_node(n.left)
            print(n.data)
            self.print_node(n.right)
            
    def print_tree(self):
        self.print_node(self.root)


def get_depth(root:Node):
    if root == None:
        return True
    
    if abs(get_depth(root.left) - get_depth(root.right)) > 1:
        return False
    
    else:
        return is_equilibrium(root.right) and is_equilibrium(root.left)

def is_equilibrium(root:Node):
    if root == None:
        return True
    
    if abs(get_depth(root.left) - get_depth(root.right)) > 1:
        return False
    else:
        return is_equilibrium(root.right) and is_equilibrium(root.left)
  
def create_minimal_bst(test, start, end):
    if start > end:
        return None
    mid = int((start + end) / 2)
    n = Node(data = test[mid])
    n.left = create_minimal_bst(test, start, mid-1)
    n.right = create_minimal_bst(test, mid+1, end)
    return n


if __name__ == "__main__":
    test = [random.randint(0,100) for _ in range(11)]
    test.sort()
    n = create_minimal_bst(test, 0, len(test)-1)
    tree = BinaryTree(root = n)
    print(is_equilibrium(n))