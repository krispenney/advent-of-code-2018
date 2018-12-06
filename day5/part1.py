def should_react(current, previous):
    if current.lower() != previous.lower():
        return False
    elif current == previous:
        return False
    elif current.upper() == previous or current == previous.upper():
        return True


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        stack = []
        while True:
            current = f.read(1)

            if not current or current == '\n':
                break
            elif len(stack) == 0:
                stack.append(current)
                continue

            previous = stack.pop()

            if not should_react(current, previous):
                stack.append(previous)
                stack.append(current)

        print('Length of sequence:', len(stack))
