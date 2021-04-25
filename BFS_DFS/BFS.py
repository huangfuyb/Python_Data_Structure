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


if __name__ == '__main__':

    BFS(gragh, 'A')
