# 링크드 리스트 끝에서 K 번째 값 출력하기


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    # 1차
    def get_kth_node_from_last(self, k):
        length = 1  # 시작 노드의 길이를 세기 위해 1부터 시작합니다
        cur = self.head

        while cur.next is not None:
            cur = cur.next
            length += 1
        end_length = length - k
        cur = self.head

        for i in range(end_length):
            cur = cur.next
        return cur

    # 2차
    def get_kth_node_from_last(self, k):
        slow = self.head
        fast = self.head

        for i in range(k):
            fast = fast.next

        while fast is not None:
            slow = slow.next
            fast = fast.next

        return slow

linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)

# 1차나 2차나 시간복잡도 측면에서는 결국 끝까지 가야하므로 똑같음.