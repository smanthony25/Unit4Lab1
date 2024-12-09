# Sean A
# Stack Class
# Using our new knowledge of docs and other stuff, make a stack class

class ArrayStack():
    def __init__(self):
        self.__stack = []
        self.__size = 0

    def push(self, item):
        """Add an item to the top of the stack"""
        self.__stack.append(item)
        self.__size += 1

    def pop(self):
        """Remove and return the top item from the stack"""
        if not self.__is_empty():
            element = self.__stack[-1]
            self.__size -= 1
            del self.__stack[-1]
            return element
        else:
            raise IndexError('Stack is empty')

    def top(self):
        """Return the top item from the stack"""
        return self.__stack[-1]

    def __is_empty(self):
        """Check if the stack is empty"""
        return self.__size == 0

    def __len__(self):
        """Return the size of the stack"""
        return self.__size

    def __str__(self):
        """Display contents of the stack"""
        out = ""
        for ele in self.__stack:
            out += str(ele) + ' '

        out += "<TOP"
        return out

