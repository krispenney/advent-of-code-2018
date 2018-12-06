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

    perform_reaction_with_sub = lambda p, c: perform_reaction(p.replace(c, '').replace(c.upper(), ''))
    result = min(map(lambda comp: perform_reaction_with_sub(polymer, comp), unique_components))

    print("Minimum polymer length:", result)
