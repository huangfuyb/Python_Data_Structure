def turn_on(is_on, index, connect):
    if is_on[index]:  # 如果已经开启了，不需要管了
        return
    is_on[index] = True
    global res
    res += 1
    for i in range(len(connect[index])):
        turn_on(is_on, connect[index][i], connect)


def turn_off(is_on, index, shut):
    if not is_on[index]:  # 如果已经关闭了，不需要管了
        return
    is_on[index] = False
    global res
    res -= 1
    for i in range(len(shut[index])):
        turn_off(is_on, shut[index][i], shut)


def input_func():
    n, q = map(int, input().split())
    is_on = [False] * (n + 1)
    connect = [[] for i in range(n+1)]
    shut = [[] for i in range(n+1)]

    for i in range(n):
        num = int(input())  # 开启几个相关联的服务
        for j in range(num):
            connect_num = int(input())  # 相关联的服务的序号
            connect[i + 1].append(connect_num)  # 开启i+1时，相关联的connect number加入到其相应位置
            shut[connect_num].append(i + 1)  # 而关闭connect_num时，将其开启时关联的数记录到其相应位置
    # print(connect,shut)
    for j in range(q):
        op, index = map(int, input().split())
        if op == 1:
            turn_on(is_on, index, connect)
            print(res)
        else:
            turn_off(is_on, index, shut)
            print(res)


if __name__ == '__main__':
    res = 0
    input_func()
