from LinkedQueue import LinkedQueue as Queue
from LinkedDeque import LinkedDeque as Deque
from LinkedStack import LinkedStack as Stack

Q = Queue()
D = Deque()
S= Stack()

D.insert_last(1)
D.insert_last(2)
D.insert_last(3)
D.insert_last(4)
D.insert_last(5)
D.insert_last(6)
D.insert_last(7)
D.insert_last(8)

Q.enqueue(D.delete_first())
Q.enqueue(D.delete_first())
Q.enqueue(D.delete_first())
D.insert_last(D.delete_first())
Q.enqueue(D.delete_first())
Q.enqueue(D.delete_last())
Q.enqueue(D.delete_first())
Q.enqueue(D.delete_first())
Q.enqueue(D.delete_first())

D.insert_last(Q.dequeue())
D.insert_last(Q.dequeue())
D.insert_last(Q.dequeue())
D.insert_last(Q.dequeue())
D.insert_last(Q.dequeue())
D.insert_last(Q.dequeue())
D.insert_last(Q.dequeue())
D.insert_last(Q.dequeue())


print (" Q = ")
print(" D = ", end = "")
while not D.is_empty():
    print(D.delete_first(),end =" ")

D.insert_last(1)
D.insert_last(2)
D.insert_last(3)
D.insert_last(4)
D.insert_last(5)
D.insert_last(6)
D.insert_last(7)
D.insert_last(8)

print("\n S = ", end="")
while not S.is_empty():
    print(S.pop(), end=" ")

S.push(D.delete_first())
S.push(D.delete_first())
S.push(D.delete_first())
S.push(D.delete_last())
S.push(D.delete_last())
S.push(D.delete_last())
S.push(D.delete_first())
S.push(D.delete_first())

D.insert_last(S.pop())
D.insert_last(S.pop())
D.insert_last(S.pop())
D.insert_last(S.pop())
D.insert_last(S.pop())
D.insert_first(S.pop())
D.insert_first(S.pop())
D.insert_first(S.pop())

print("\n D = ", end="")
while not D.is_empty():
    print(D.delete_first(), end=" ")