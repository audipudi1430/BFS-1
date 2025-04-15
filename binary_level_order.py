# Approach:
# 1. Use a queue (BFS) to traverse the tree level by level starting from the root.
# 2. For each level, process all nodes in the queue, store their values in a list, 
#    and enqueue their left and right children for the next level.
# 3. Append the list of each level's node values to the final result list.

# Time Complexity: O(N) - where N is the number of nodes in the tree (each node is visited once)
# Space Complexity: O(N) - for storing the queue and the result list

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque()
        result = []
        q.append(root)

        while q:
            qlen = len(q)
            level = []
            for i in range(qlen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                result.append(level)
        return result
