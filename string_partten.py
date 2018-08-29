def regular_expression(s, partten):
    pass


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def move_nth_node(start_node, n):
    if n == 0:
        return start_node
    pre_node = None
    tb_removed = start_node
    cursor = start_node
    for cnt in range(n - 1):
        cursor = cursor.next
    if cursor is None:
        return start_node
    while True:
        if cursor.next is not None:
            # moving pointer
            pre_node = tb_removed
            tb_removed = tb_removed.next
            cursor = cursor.next

        else:
            if pre_node is None:
                return tb_removed.next
            else:
                pre_node.next = tb_removed.next
                return start_node


def generate(l):
    start = ListNode(l[0])
    next_node = start
    for i in range(1, len(l)):
        next_node.next = ListNode(l[i])
        next_node = next_node.next
    return start


def main():
    test = generate([1, 2, 3, 4, 5])
    move_nth_node(test, 2)


if __name__ == '__main__':
    main()
