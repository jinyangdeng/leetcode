"""
Original question: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal
"""

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        stack = [TreeNode(preorder[0])]

        def dfs(stack, idx):
            if idx == len(preorder):
                return

            curr = preorder[idx]
            currNode = TreeNode(curr)
            while postorder.index(stack[-1].val) < postorder.index(curr):
                stack.pop()

            if stack[-1].left is None:
                stack[-1].left = currNode
            else:
                stack[-1].right = currNode
            
            stack.append(currNode)   
            dfs(stack, idx + 1)         

        dfs(stack, 1)

        return stack[0]