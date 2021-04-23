class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 这里注意是用的栈的思想，层序遍历那用的队列思想
    def pre_order_norec(self, root):
        if not root:
            return []
        cur = root
        stack = []
        result = []
        while cur or stack:
            while cur:
                result.append(cur.val)
                stack.append(cur)
                cur = cur.left
            tmp = stack.pop()
            cur = tmp.right
        return result

    def in_order_norec(self, root):
        if not root:
            return []
        cur = root
        stack = []
        result = []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            tmp = stack.pop()
            result.append(tmp.val)
            cur = tmp.right
        return result

    def post_order_norec(self, root):
        if not root:
            return []
        stack, res = [(0, root)], []
        while stack:
            flag, node = stack.pop()
            if not node:
                continue
            if flag == 1:
                res.append(node.val)
            else:
                stack.append((1, node))
                stack.append((0, node.right))
                stack.append((0, node.left))
        return res


if __name__ == '__main__':
    string = ['j', '1']
    print(type('.'.join(string)))
    for i, index in enumerate(range(3), 1):

        print(i, index)

