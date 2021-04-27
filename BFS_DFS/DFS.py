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


def DFS_fix(gragh,root):

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
