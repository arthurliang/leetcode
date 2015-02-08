# Given preorder and inorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from utility.BinTree import TreeNode

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        # iterative solution
        if not preorder:
            return None

        head = TreeNode(preorder[0])

        curNode = head
        flagRight = False
        stack = [head]
        i = 1
        j = 0
        while i < len(preorder):
            if stack and stack[-1].val == inorder[j]:
                curNode = stack.pop()
                j += 1
                flagRight = True
            elif flagRight:
                curNode.right = TreeNode(preorder[i])
                curNode = curNode.right
                stack.append(curNode)
                i += 1
                flagRight = False
            else:
                curNode.left = TreeNode(preorder[i])
                curNode = curNode.left
                stack.append(curNode)
                i += 1

        return head

#         # recursive solution
#         if not preorder:
#             return None
#
#         pos = inorder.index(preorder[0])
#
#         head = TreeNode(preorder[0])
#         head.left = self.buildTree(preorder[1:pos + 1], inorder[0: pos])
#         head.right = self.buildTree(preorder[pos + 1:len(preorder)], inorder[pos + 1: len(inorder)])
#
#         return head

