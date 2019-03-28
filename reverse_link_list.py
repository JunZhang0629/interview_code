class link_node:
    def __init__(self):
        self.data = 0
        self.next = None

def RecursiveReverse(head):
    if head is None or head.next is None:
        return head
    else:
        newhead = RecursiveReverse(head.next)
        head.next.next = head
        head.next = None
    return newhead

def reverse(head):
    if head is None:
        return
    first_node = head.next
    newnode = RecursiveReverse(first_node)
    head.next = newnode
    return newnode

if __name__ == "__main__":
    i = 1
    head = link_node()
    head.next = None
    tmp = None
    ptr = head

    while i<8:
        tmp = link_node()
        tmp.data = i
        tmp.next = None
        ptr.next = tmp
        ptr = tmp
        i += 1

    print("逆序前：")
    ptr = head.next
    while ptr !=  None:
        print(ptr.data)
        ptr = ptr.next

    print("\n逆序后：")
    newnode=reverse(head)

    ptr = head.next
    while ptr != None:
        print(ptr.data)
        ptr = ptr.next
