def array_resort(array):
    '''

    :param array: 输入一个数组，怎么重新排列使得最终相邻数组之间做差的和最大[1,5,2,2,2]->[2,1,5,2,2]
    :return: 最大相邻序列差的和,8
    '''
    array.sort()
    mid = len(array)//2
    low = array[:mid]
    high = array[mid:]
    temp = 2*(sum(high)-sum(low))
    # 如果为奇数，大小大小大，temp相当于大的部分(high)的数多加了两个
    if len(array) % 2:
        ans = temp-high[0]-high[1]  # 要想最终值最大,减去多加的最小的前两个数
    else:

        # 如果为偶数，大小大小，temp相当于多减了一个小的部分(low)的数,多加了一个大的部分(high)的数

        ans = temp - high[0] + low[-1]  # 要想最终值最大，减去多加的最小的数，加上少加的最大的数
    return ans
