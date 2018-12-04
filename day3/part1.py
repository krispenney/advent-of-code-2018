import re
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(threshold=np.nan)

rexp = re.compile(r"#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)")

def make_claim(line):
    match = rexp.match(line)

    return {
        "id": match.group(1),
        "left_edge_dist": int(match.group(2)),
        "top_edge_dist": int(match.group(3)),
        "width": int(match.group(4)),
        "height": int(match.group(5))
    }

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        max_width = 0
        max_height = 0
        claims = []
        for line in f:
            claim = make_claim(line)
            claims.append(claim)

            if max_width < (claim["left_edge_dist"] + claim["width"]):
                max_width = claim["left_edge_dist"] + claim["width"]

            if max_height < (claim["top_edge_dist"] + claim["height"]):
                max_height = claim["top_edge_dist"] + claim["height"]

        fabric = np.zeros((max_width+1, max_height+1))
        zero_regions = []

        for claim in claims:
            region = fabric[claim["left_edge_dist"]:(claim["left_edge_dist"]+claim["width"]), claim["top_edge_dist"]:(claim["top_edge_dist"]+claim["height"])]
            if np.all(region == 0):
                zero_regions.append(claim["id"])

            region += 1
        fabric[fabric == 0] = 0
        fabric[fabric == 1] = 0
        fabric[fabric > 0] = 1
        unique, counts = np.unique(fabric, return_counts=True)
        print(counts[1])
        print(zero_regions)
