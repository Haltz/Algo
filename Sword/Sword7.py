# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def indexof(self, target: int, arr: list):
        return arr.index()

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None

        if len(preorder) == 1:
            return TreeNode(inorder[0])

        root = TreeNode(preorder[0])
        left_inorder = inorder[0: inorder.index(preorder[0])]
        left_preorder = preorder[1:len(left_inorder)+1]
        print(left_preorder, left_inorder)
        root.left = self.buildTree(left_preorder, left_inorder)
        right_inorder = inorder[inorder.index(preorder[0])+1:]
        right_preorder = preorder[len(left_preorder)+1:]
        print(right_inorder, right_preorder)

        root.right = self.buildTree(right_preorder, right_inorder)
        return root
