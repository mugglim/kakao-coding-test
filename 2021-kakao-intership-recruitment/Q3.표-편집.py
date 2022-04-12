class Node:
    def __init__(self, value):
        self.value = value
        self.prev = self.next = None


class DoublyLinkedList:
    def __init__(self, n):
        self.size = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.curr = self.head
        self.checked = ["O"] * n

    def isEmpty(self): return self.size == 0
    def isLastNode(self): return self.curr.next == self.tail

    def move(self, opt, i):
        if opt == "L":
            for _ in range(i):
                self.curr = self.curr.prev
        else:
            for _ in range(i):
                self.curr = self.curr.next

    def linkNode(self, prevNode, newNode, nextNode):
        newNode.prev, newNode.next = prevNode, nextNode
        prevNode.next, nextNode.prev = newNode, newNode
        self.size += 1

    def unlinkNode(self, deletedNode=None):
        if self.isEmpty() or not deletedNode:
            return False
        prevNode, nextNode = deletedNode.prev, deletedNode.next
        prevNode.next, nextNode.prev = nextNode, prevNode
        self.size -= 1

    def append(self, x):
        prevNode, nextNode = self.tail.prev, self.tail
        newNode = Node(x)
        self.linkNode(prevNode, newNode, nextNode)

    def restore(self, deletedNode):
        self.linkNode(deletedNode.prev, deletedNode, deletedNode.next)
        self.checked[deletedNode.value] = "O"

    def remove(self):
        deletedNode = self.curr
        newCurr = self.curr.prev if self.isLastNode() else self.curr.next
        self.checked[deletedNode.value] = "X"
        self.unlinkNode(deletedNode)
        return [deletedNode, newCurr]


def solution(n, k, cmd):
    stack = []
    dl = DoublyLinkedList(n)

    for i in range(n):
        dl.append(i)
    dl.move("R", k+1)

    for l in cmd:
        opt, *v = l.split(" ")
        v = int(v[0]) if v else v

        if opt == "U":
            dl.move("L", v)
        if opt == "D":
            dl.move("R", v)
        if opt == "C":
            deletedNode, newCurr = dl.remove()
            stack.append(deletedNode)
            dl.curr = newCurr
        if opt == "Z":
            dl.restore(stack.pop())

    return ''.join(dl.checked)
