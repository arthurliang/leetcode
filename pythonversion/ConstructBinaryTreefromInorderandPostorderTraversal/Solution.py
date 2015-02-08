# Given inorder and postorder traversal of a tree, construct the binary tree.
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
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        # iterative solution
        if not inorder:
            return None

        head = TreeNode(postorder[-1])

        curNode = head
        flagLeft = False
        stack = [head]
        i = -2
        j = -1
        while i >= -len(postorder):
            if stack and stack[-1].val == inorder[j]:
                curNode = stack.pop()
                j -= 1
                flagLeft = True
            elif flagLeft:
                curNode.left = TreeNode(postorder[i])
                curNode = curNode.left
                stack.append(curNode)
                i -= 1
                flagLeft = False
            else:
                curNode.right = TreeNode(postorder[i])
                curNode = curNode.right
                stack.append(curNode)
                i -= 1

        return head


#         # recursive solution
#         if not inorder:
#             return None
#
#         pos = inorder.index(postorder[-1])
#
#         head = TreeNode(postorder[-1])
#         head.left = self.buildTree(inorder[0 : pos], postorder[0 : pos])
#         head.right = self.buildTree(inorder[pos + 1 : len(inorder)], postorder[pos : len(postorder) - 1])
#
#         return head
