#Recursive Approach
def in_order_recursive(root):
    if root:
        in_order_recursive(root.left)
        print(root.value, end=' ')
        in_order_recursive(root.right)


#Iterative Approach (using a stack)
def in_order_iterative(root):
    stack = []
    current = root
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        print(current.value, end=' ')
        current = current.right
