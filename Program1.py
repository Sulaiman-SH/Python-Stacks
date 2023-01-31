#Create a stack
def create_Stack():
    stack_init = []
    return stack_init
#Check if the stack empty
def check_ifEmpty(StackCheckE):
    return StackCheckE == 0
#Check if the stack full
def check_ifFull(StackCheckF):
    return StackCheckF == 5
#Push items to the stack
def Push(StackPush, item):
    if check_ifFull(len(StackPush)):
        return "Full stack"
    StackPush.append(item)
    return StackPush
#Pop an item from stack
def pop(StackPop):
    if check_ifEmpty(len(StackPop)):
        return "Empty stack"
    
    return StackPop.pop()

stack = []
stack = create_Stack()
print("value pushed: ",Push(stack, '5'))
print("value pushed: ",Push(stack, '3'))
print("value pushed: ",Push(stack, '2'))
print("value pushed: ",Push(stack, '0'))
print("value pushed: ",Push(stack, '2'))
print("value pushed: ",Push(stack, '2'))

print(stack)
print("Pop item: " ,pop(stack))
print(stack)