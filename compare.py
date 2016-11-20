# this takes two time points expressed as floats
# check for conflict

ctime1 = [209.0, 210.0]
stime1 = [[513.0, 519.0], None, [508.0, 512.5], [108.0, 112.0], [208.0, 219.0],
          [114.0, 119.0], [312.5, 316.0], [308.0, 312.0], [414.0, 416.0],
          [408.5, 412.0]]


def compare(ctime, stime):
    i = 0

    # loop through student avail1
    while i < len(stime):
        if stime[i] is None:
            pass
        elif stime[i][0] <= ctime[0] and stime[i][1] >= ctime[1]:
            return True

        i += 1

    return False


# print compare(ctime1, stime1)
