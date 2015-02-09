# Given a binary tree
#
#     struct TreeLinkNode {
#       TreeLinkNode *left;
#       TreeLinkNode *right;
#       TreeLinkNode *next;
#     }
# Populate each next pointer to point to its next right node. If there is no next right node,
# the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
# Note:
#
# You may only use constant extra space.
# You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and
# every parent has two children).
# For example,
# Given the following perfect binary tree,
#          1
#        /  \
#       2    3
#      / \  / \
#     4  5  6  7
# After calling your function, the tree should look like:
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \  / \
#     4->5->6->7 -> NULL

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        self.linklevel(root)
        self.breakTailofLevel(root)

    def linklevel(self, root):
        def enqueue(tail, x):
            if x:
                tail.next = x
                return x
            else:
                return tail

        if root is None:
            return
        head = tail = root
        head.next = head.left
        while head.next:
            tail = enqueue(tail, head.left)
            tail = enqueue(tail, head.right)
            head = head.next

    def breakTailofLevel(self, root):
        (i, m) = (0, 1)
        prev = root
        while root:
            (prev, root) = (root, root.next)
            i += 1
            if i == m:
                prev.next = None
                (i, m) = (0, 2 * m)


#         # Brute-Force but not use constant extra space
#         if root is None:
#             return
#
#         cq = [root]
#         nq = []
#
#         while cq:
#             node = cq.pop(0)
#             node.next = cq[0] if cq else None
#
#             if node.left is None:
#                 continue
#
#             nq.append(node.left)
#             nq.append(node.right)
#
#             if not cq:
#                 t = cq
#                 cq = nq
#                 nq = t
#                 continue
