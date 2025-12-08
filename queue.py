# Function to add (enqueue) a value to the queue
def enqueue(queue, value):
    queue.append(value)   # Add to the end (tail)

# Function to remove (dequeue) the first value from the queue
def dequeue(queue):
    return queue.pop(0)   # Remove from the front (head)


# --- Using the Queue ---
my_queue = []

# Add items to the queue
enqueue(my_queue, 'a')
enqueue(my_queue, 'b')
enqueue(my_queue, 'c')

print(my_queue)   # Output: ['a', 'b', 'c']

# Remove items from the queue
print(dequeue(my_queue))  # Output: 'a'
print(dequeue(my_queue))  # Output: 'b'

print(my_queue)   # Remaining queue: ['c']
