class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def genTree(li):
    if not li:
        return None
    else:
        from collections import deque
        queue = deque()
        i = 0
        root = TreeNode(li[i])
        queue.append(root)
        while queue and i < len(li):
            node = queue.popleft()
            i += 1
            if i < len(li) and li[i] is not None:
                node.left = TreeNode(li[i])
                queue.append(node.left)
            i += 1
            if i < len(li) and li[i] is not None:
                node.right = TreeNode(li[i])
                queue.append(node.right)
        return root


def inOrderPrintTree(node):
    if not node:
        return
    print(node.val, end=',')
    inOrderPrintTree(node.left)
    inOrderPrintTree(node.right)


def frontOrderPrintTree(node):
    if not node:
        return
    frontOrderPrintTree(node.left)
    print(node.val, end=',')
    frontOrderPrintTree(node.right)


if __name__ == '__main__':
    tree = [1, 2, 3, None, None, 4, 5]
    tree = genTree(tree)
    inOrderPrintTree(tree)
    print('\n')
    frontOrderPrintTree(tree)