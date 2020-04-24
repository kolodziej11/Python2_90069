from ex2.stack import Stack, BroadStack


def main():
    stack = BroadStack()
    stack.push(15)
    stack.push(12)
    stack.push(35)
    stack.push(43)
    stack.push(3)
    stack.push(65)

    print(f"Minimalna wartość to {stack.get_minimum()}")

    while not stack.is_empty():
        print(stack.top())
        stack.pop()


if '__main__' == __name__:
    main()
