class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def genListNode(li):
    ''' the head node is li[0], new node is inserted to the tail of current node '''
    head = ListNode(li[0])
    tail = head
    for i in li[1:]:
        tail.next = ListNode(i)
        tail = tail.next
    return head


def genListNode2(li):
    ''' the head node is li[-1], new node is inserted to the head of current'''
    head = ListNode(li[0])
    for i in li[1:]:
        node = ListNode(i)
        node.next = head
        head = node
    return head


def printListNode(node):
    while node:
        print(node.val, end=',')
        node = node.next
    print('\n')


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    head1 = genListNode(nums)
    head2 = genListNode2(nums)
    printListNode(head1)
    printListNode(head2)