# https://leetcode.com/problems/binary-tree-preorder-traversal/

class Node:
    # Classic binary tree
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(nodes, f):
    """this function builds a tree from input; you don't have to modify it"""
    val = next(nodes)
    if val == "x":
        return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)


def preorder(root):
    def dfs(node, res):
        if node is not None:
            res.append(node.val)
            dfs(node.left, res)
            dfs(node.right, res)
        return res

    return dfs(root, [])


root = build_tree(iter('1 2 3 4 5 x 8 x x 6 7 9'.split()), int)
print(preorder(root))
