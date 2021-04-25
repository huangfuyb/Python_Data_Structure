from collections import deque
gragh = {"A": ["B", "C"],
         "B": ["A", "C", "D"],
         "C": ["A", "B", "D", "E"],
         "D": ["B", "C", "E", "F"],
         "E": ["C", "D"],
         "F": ["D"]}


def BFS(gragh, root):

    queue = deque()
    queue.append(root)
    s = set()
    s.add(root)

    while len(queue) > 0:
        key = queue.popleft()
        node = gragh[key]
        for i in node:
            if i not in s:
                s.add(i)
                queue.append(i)

        print(key)


def BFS_With_Path(gragh, root):
    queue = deque()
    queue.append(root)
    s = set()
    s.add(root)
    parent = {root: None}  # 记录节点的前一个节点
    while len(queue) > 0:
        key = queue.popleft()
        node = gragh[key]
        for i in node:
            if i not in s:
                s.add(i)
                queue.append(i)
                # 展开的点i一定是key从过来
                parent[i] = key

        # print(key)
    return parent


if __name__ == '__main__':

    BFS(gragh, 'A')
    parent = BFS_With_Path(gragh, 'A')
    for key in parent:
        print(key, parent[key])
    # 从A到E的最短路径：
    node = 'E'
    while node:
        print(node)
        node = parent[node]

