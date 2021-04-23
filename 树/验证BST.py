class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = 0
        self.left = left
        self.right = right


class solution:
    def isValidBST(self, root):
        stack = []
        cur = root
        last = float('-inf')
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            temp = stack.pop()
            if temp.val < last:
                return False
            last = temp.val
            cur = temp.right
        return True
