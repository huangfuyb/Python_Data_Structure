from collections import deque

gragh = {"A": ["B", "C"],
         "B": ["A", "C", "D"],
         "C": ["A", "B", "D", "E"],
         "D": ["B", "C", "E", "F"],
         "E": ["C", "D"],
         "F": ["D"]}


def DFS(gragh, root):

    stack = []
    stack.append(root)
    s = set()
    s.add(root)

    while len(stack) > 0:
        key = stack.pop()
        node = gragh[key]
        for i in node:
            if i not in s:
                s.add(i)
                stack.append(i)

        print(key)

# 当以A为root，走ABDECF时，上述的DFS会输出：ABDEFC
# 原因是 上述的dfs 是标记邻节点的方法，C在B遍历完后已经被压入栈了，所以C会后打印。每pop一次才会print。
# 改正的这个dfs，标记的是弹出节点，只有弹出了，才算放到set里，但这样会导致栈中有大量重复节点。print是放在if下面，只有不在set里的才print。
# 只有极个别例子会出现这个问题。

def DFS_fix(gragh, root):

    stack = []
    stack.append(root)
    s = set()
    while len(stack) > 0:

        key = stack.pop()
        if key not in s:
            s.add(key)
            node = gragh[key]
            for i in node:
                if i not in s:
                    stack.append(i)
            print(key)


if __name__ == '__main__':

    DFS(gragh, 'A')
    print('\t')
    DFS_fix(gragh, 'A')
