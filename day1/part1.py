def parse_count(line):
    sign = line[0]
    value = int(line[1:])

    if sign == '+':
        return value
    elif sign == '-':
        return -value

if __name__ == '__main__':
    frequency = 0
    with open("input.txt", 'r') as f:
       for line in f:
          frequency += parse_count(line)
    print(frequency)
