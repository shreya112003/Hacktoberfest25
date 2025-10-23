class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")

    def size(self):
        return len(self.items)

# Example usage of the custom Stack class
my_stack = Stack()
my_stack.push("apple")
my_stack.push("banana")
print(f"Stack after pushes (using class): {my_stack.items}")

print(f"Top element (using class): {my_stack.peek()}")

popped_item = my_stack.pop()
print(f"Popped item (using class): {popped_item}")
print(f"Stack after pop (using class): {my_stack.items}")
