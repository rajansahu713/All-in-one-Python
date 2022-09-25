def create_stack():
    stack = []
    return stack

def check_empty(stack):
    return len(stack) == 0


def push(stack, item):
    stack.append(item)
    print("pushed item:" , item)



def pop(stack):
    if (check_empty(stack)):
        return "stack is empty"

    return stack.pop()


stack = create_stack()
print(pop(stack))
push(stack, 1)
push(stack, 2)
push(stack, '555')
push(stack, "vgg")
print("popped item: ", pop(stack))
print("stack after popping an element: ", stack)