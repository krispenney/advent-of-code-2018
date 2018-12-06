def should_react(current, previous):
    if current.lower() != previous.lower():
        return False
    elif current == previous:
        return False
    elif current.upper() == previous or current == previous.upper():
        return True

def perform_reaction(polymer):
    stack = []

    for current in polymer:
        if not current or current == '\n':
            break
        elif len(stack) == 0:
            stack.append(current)
            continue

        previous = stack.pop()

        if not should_react(current, previous):
            stack.append(previous)
            stack.append(current)
    return len(stack)


if __name__ == '__main__':
    polymer = ''
    with open('input.txt', 'r') as f:
        polymer = f.read().replace('\n', '')

    unique_components = set(polymer.lower())

    min_length = 2**31

    for comp in unique_components:
        sub_polymer = polymer.replace(comp, '').replace(comp.upper(), '')
        result = perform_reaction(sub_polymer)

        if result < min_length:
            min_length = result

    print('Length of sequence:', min_length)
