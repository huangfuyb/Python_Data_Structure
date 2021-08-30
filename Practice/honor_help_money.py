'''
https://www.cnblogs.com/hcw110/p/9851371.html
'''


def solution(n, k, m):
    array = [i for i in range(1, n+1)]
    start_a = n-1  # 刚开始时倒退一步想，下一步就是index为0
    start_b = 0  # 刚开始时倒退一步想，下一步就是index为n-1
    count = n
    while count > 0:
        start_a = go(start_a, 1, k, n, array)
        start_b = go(start_b, -1, m, n, array)
        if start_a == start_b:
            print('{:3}'.format(start_a+1), end='')
            count -= 1
        else:
            print('{:3}{:3}'.format(start_a+1, start_b+1), end='')
            count -= 2
        array[start_a] = 0
        array[start_b] = 0
        if count > 0:
            print(',', end='')


def go(start, t, m, n, array):
    while m > 0:
        m -= 1
        start = (start + t + n) % n
        while array[start] == 0:
            start = (start + t + n) % n
    return start


if __name__ == '__main__':
    print('{:8}'.format(6))
    n, k, m = map(int, input().split())
    solution(n, k, m)
