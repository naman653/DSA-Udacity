class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def even_after_odd(head):
    """
    :param - head - head of linked list
    return - updated list with all even elements are odd elements
    """
    if head is None:
        return head

    even = None
    odd = None
    even_tail = None
    odd_tail = None

    while head:
        next_node = head.next

        if head.data % 2 == 0:
            if even is None:
                even = head
                even_tail = even
            else:
                even_tail.next = head
                even_tail = even_tail.next
        else:
            if odd is None:
                odd = head
                odd_tail = odd
            else:
                odd_tail.next = head
                odd_tail = odd_tail.next

    if odd is None:
        return even
        
    odd_tail.next = even
    return odd
