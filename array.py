queue = []
front = -1
rear = -1


def is_empty():
    return front == -1 and rear == -1


def enqueue(item):
    global front, rear
    if is_empty():
        front = 0
    rear += 1
    queue.append(item)


def dequeue():
    global front, rear
    if is_empty():
        return -1

    # Get the front element
    item = queue[front]

    # If this was the last element, reset queue indices
    if front == rear:
        front = rear = -1
    else:
        front += 1

    return item


# Enqueue items
# Enter the number of elements to enqueue
n = int(input())
arr = list(map(int, input().split()))[:n]
for i in range(n):
    enqueue(arr[i])

# Dequeue items
while not is_empty():
    print(dequeue())
