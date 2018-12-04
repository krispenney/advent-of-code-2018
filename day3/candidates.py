candidates = [ '721', '1245', '1072', '1165', '852', '1192', '628', '1058', '758', '1006', '1138', '164', '1068', '689', '631', '997', '555', '487', '1182', '826', '1217', '877', '1281', '709', '963', '160', '1209', '850', '1232', '664', '1311', '1150', '902', '1040', '1008', '934', '1056', '940', '954', '1199', '881', '801', '660', '1061', '1169', '614', '855', '1087', '1170', '804', '585' ]

def exclude(x):
    if x <= 664 or 758 <= x:
        return False
    if x == 709:
        return False

    return True

candidates = map(lambda x: int(x), candidates)
candidates = list(filter(exclude, candidates))

print(candidates)
print(min(candidates), max(candidates))
