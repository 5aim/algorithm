# node 만들기
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# linked list node
class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    # 노드 추가하기
    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    # 모든 노드 프린트하기
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    # 노드 찾기
    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    # 노드 더하기
    def add_node(self, index, value):
        new_node = Node(value) # [6]
        if index == 0:
            new_node.next = self.head
            self.head = new_node # head -> [6] -> [5]
            return

        node = self.get_node(index - 1) # [5]
        next_node = node.next # [12]
        node.next = new_node # [5] = [6]
        new_node.next = next_node # [6] -> [12]
        return

    # 노드 삭제하기
    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return
        
        node = self.get_node(index -1)
        node.next = node.next.next


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.add_node(0, 3) # 0번째 node에 3을 추가
linked_list.print_all() # -> 5를 들고 있는 노드를 반환해야 합니다!
linked_list.delete_node(0) # -> 5를 들고 있는 노드를 반환해야 합니다!
linked_list.print_all() # -> 5를 들고 있는 노드를 반환해야 합니다!

