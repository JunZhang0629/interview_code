class link_node:
    def __init__(self):
        self.data = 0
        self.next = None

def remove_Duplink_node(head):
    if head == None or head.next == None:
        return
    Outner = head.next
    inner = None
    prener = None
    while Outner != None:
        inner = Outner.next
        prener = Outner
        while inner != None:
            if Outner.data == inner.data:
                prener.next = inner.next
                inner = inner.next
            else:
                prener = inner
                inner = inner.next
        Outner = Outner.next

'''
递归法：
def removeDupRecursion(head.next):
    if head.next is None:
        return head
    pointer = None
    cur = head
    head.next = removeDupRecursion(head.next)
    pointer = head.next
    while pointer is not None:
        if head.data == pointer.data:
            cur.next = pointer.next
            pointer = cur.next
        else:
            pointer = pointer.next
            cur = cur.next
    return head
'''


if __name__ == "__main__":
    i = 1
    head = link_node()
    head.next = None
    ptr = head
    tmp = None
    while i < 8:
        tmp = link_node()
        if i % 2 == 0:
            tmp.data = i+1
        if i % 3 == 0:
            tmp.data = i-2
        else:
            tmp.data = i

        tmp.next = None
        ptr.next = tmp
        ptr = tmp
        i += 1
    print("before delete node:")
    ptr =head.next
    while ptr!= None:
        print(ptr.data)
        ptr =ptr.next
    remove_Duplink_node(head)
    print("\nafd")
    ptr = head.next
    while ptr!= None:
        print(ptr.data)
        ptr = ptr.next
