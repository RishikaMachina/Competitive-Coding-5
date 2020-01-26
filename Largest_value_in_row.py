# Runs on Leetcode
    # runtime - O(n) where n is # of elements in tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    import collections
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        final = []
        queue = collections.deque([root])
        while queue:
            m = float('-inf')
            size = len(queue)
            for i in range(size):
                popped = queue.popleft()
                m = max(m, popped.val)
                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)
            final.append(m)
        return final
