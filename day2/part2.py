import numpy as np
from numpy import inf

def diff_letters(a, b):
    diff = 0
    for l, r in zip(a, b):
        if l != r:
            diff += 1

    return diff

def min_dist(box_ids):
    v_distance = np.vectorize(diff_letters)
    n_ids = len(box_ids)
    distances = np.zeros((n_ids, n_ids))

    for i in range(n_ids):
       for j in range(n_ids):
           if i != j:
               distances[i, j] = diff_letters(box_ids[i], box_ids[j])

    distances[distances == 0] = inf # offset diagonals (always 0)

    x, y = np.unravel_index(np.argmin(distances),distances.shape)

    print("Closest ids:", ''.join([a if a == b else '' for a, b in zip(box_ids[x], box_ids[y])]))

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        box_ids = f.read().splitlines()

        min_dist(box_ids)
