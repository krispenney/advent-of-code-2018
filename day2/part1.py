from collections import defaultdict

def count_letters(box_id):
    counts = defaultdict(int)

    for c in box_id:
        counts[c] += 1

    return counts.items()

def contains_letter_exact(counts, n):
    for k, v in counts:
        if v == n:
            return True

    return False

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        two_count = 0
        three_count = 0
        for box_id in f:
            counts = count_letters(box_id)

            two_count += 1 if contains_letter_exact(counts, 2) else 0
            three_count += 1 if contains_letter_exact(counts, 3) else 0

        print("checksum:", two_count*three_count)
