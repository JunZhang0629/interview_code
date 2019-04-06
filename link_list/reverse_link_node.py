'''
实现链表的逆序，共有三种方法
1：就地逆序
   初始化三个变量，记录 前驱结点、当前节点、后继节点 的位置，让当前节点的指针从原来指向后继节点改为指向前驱结点实现逆序。
2：递归逆序
    先逆序除第一个结点以外的子链表，接着把节点添加到逆序的子链表的后面
3：插入法
'''


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
