#Recursive Approach
def pre_order_traversal(node):
    if node:
        print(node.value)  # Or perform any action
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)

#Iterative Approach
def pre_order_iterative(root):
    if root is None:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.value, end=' ')
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
