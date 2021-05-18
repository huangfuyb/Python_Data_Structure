class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.parent = None


class BST:
    def __init__(self, li=None):
        self.root = None
        if li:
            for val in li:
                self.insert_no_rec(val)  # creat a BST
                self.root = self.insert_rec(self.root, val) # creat a BST recursion

    def insert_no_rec(self, val):
        p = self.root
        if not p:
            self.root = BiTreeNode(val)
            return
        while True:
            if val > p.data:
                if not p.rchild:
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
                    return
                else:
                    p = p.rchild
            elif val < p.data:
                if not p.lchild:
                    p.lchild = BiTreeNode(val)
                    p.lchild.parent = p
                    return
                else:
                    p = p.lchild
            else:
                return

    def insert_rec(self, node, val):
        if not node:
            node = BiTreeNode(val)
        elif val > node.data:
            node.rchild = self.insert_rec(node.rchild, val)
            node.rchild.parent = node
        elif val < node.data:
            node.lchild = self.insert_rec(node.lchild, val)
            node.lchild.parent = node
        return node

    def query_no_rec(self, val):
        p = self.root
        while p:
            if val > p.data:
                p = p.rchild
            elif val < p.data:
                p = p.lchild
            else:
                return p
        return None

    def query_rec(self, node, val):
        if not node:
            return None
        elif val > node.data:
            return self.query_rec(node.rchild, val)
        elif val < node.data:
            return self.query_rec(node.lchild, val)
        else:
            return node

    def pre_order(self, root):
        if root:
            print(root.data, end=',')
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    def pre_order_no_rec(self, root):
        if not root:
            return
        temp = root
        stack = []
        while temp or stack:
            while temp:
                stack.append(temp)
                print(temp.data, end=',')
                temp = temp.lchild
            if stack:
                temp = stack.pop()
                temp = temp.rchild

    def in_order(self, root):
        if root:
            self.in_order(root.lchild)
            print(root.data, end=',')
            self.in_order(root.rchild)

    def post_order(self, root):
        if root:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.data, end='')


if __name__ == '__main__':
    # tree = BST([4, 6, 7, 9, 2, 1, 3, 5, 8])
    tree = BST([8, 6, 10, 5, 5, 7, 9, 11])
    tree.pre_order(tree.root)
    print('')
    tree.pre_order_no_rec(tree.root)
    print('')
    tree.in_order(tree.root)










