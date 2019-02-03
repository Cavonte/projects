stack1 = [1, 3, 8, 4, 2, 3, 0]
stack2 = []

while stack1:
    current = stack1.pop()
    print(current)
    while stack2:
        top = stack2.pop()
        if top < current:
            stack1.append(top)

    stack2.append(current)

print(stack1)

