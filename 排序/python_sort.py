
li = [[2, 3], [1, 3]]
li.sort(key=lambda x: x[0])
print(li)
li = ['test_2', 'test_1', 'test_3', 'test_89', 'test_34']
li.sort(key=lambda x: x[3:])
print(li)