def parse_count(line):
    sign = line[0]
    value = int(line[1:])

    if sign == '+':
        return value
    elif sign == '-':
        return -value

if __name__ == '__main__':
    frequency = 0
    past_frequencies = { 0 }
    done = False
    while not done:
        with open("input.txt", 'r') as f:
            for line in f:
                frequency += parse_count(line)

                if frequency in past_frequencies:
                    print(frequency)
                    done = True
                    break

                past_frequencies |= { frequency }
