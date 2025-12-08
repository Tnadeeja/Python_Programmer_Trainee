# Function to push (add) a value to the stack
def push(stack, value):
    stack.append(value)   # append() adds the value to the end (top of stack)

# Function to pop (remove) the last value from the stack
def pop(stack):
    return stack.pop()    # pop() removes and returns the last item

# Create an empty stack (a list)
myStack = []

# Add items to the stack
push(myStack, 'a')
push(myStack, 'b')
push(myStack, 'c')
push(myStack, 'd')

print(myStack)  # Show the full stack → ['a', 'b', 'c', 'd']

# Remove the last pushed item (LIFO)
pop(myStack)

print(myStack)  # After popping, → ['a', 'b', 'c']
