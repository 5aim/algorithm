# 노드 만들기
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# linked list node
class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

# linked list를 10진수로 배열
def _get_linked_list_sum(linked_list):
    sum = 0
    head = linked_list.head
    while head is not None:
        sum = sum * 10 + head.data
        head = head.next
    return sum

# 위에서 만들어진 두개의 linked list를 더함.
def get_linked_list_sum(linked_list_1, linked_list_2):
    sum_1 = _get_linked_list_sum(linked_list_1)
    sum_2 = _get_linked_list_sum(linked_list_2)

    print(sum_1)
    print(sum_2)
    
    return sum_1 + sum_2

# linked list [6], [7], [8]
linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

# linked list [3], [5], [4]
linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))