import os

def read_data():
    """
    Don't want to read file more than once.
    """

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '_res/input.txt'), 'r') as fp:
        # -- Convert to ints.  One data entry per line.
        return [int(x) for x in fp.readlines()]

def part_1(data):
    """
    Part 1 compares each successive data entry, and increments by 1 if it is larger than the previous entry.

    :param data: Data to parse.
    :type data: list of int
    """

    count = 0

    # -- Start at element 1 as we need to compare against element 0.
    for i in range(1, len(data)):
        if data[i] > data[i - 1]:
         count += 1

    return count


def part_2(data):
    """
    Part 2 compares rolling sums of 3 elements at a time. 
    There's always 3 sums being incremented, and an additional sum that has finished being added to.

    :param data: Data to parse.
    :type data: list of int
    """

    count = 0

    # -- Initialise the first sum to avoid costly branching in our iteration.
    sums = [sum(data[:3]), sum(data[1:3]), sum(data[2:3]), data[3]]

    # -- We want to start our data off *after* our initialisation.
    for i in range(3, len(data)):

        # -- Index 'a' will always be our finished sum.  Indices b, c, & d are the next sums, in decreasing order of closest to finished.
        a, b, c, d = [(i - 3 + x) % 4 for x in range(4)]

        # -- Add to our 'active' sums.
        sums[b] += data[i]
        sums[c] += data[i]
        sums[d] += data[i]

        # -- If our newly finished sum is larger than the last finished sum, check if it is larger,
        if (sums[b] > sums[a]):
            # -- and if it is, increment our counter.
            count += 1

        # -- Reset our last finished sum, as it's about to become active again.
        sums[a] = 0

    return count


def main():
  data = read_data()
  
  print('Solution to part 1: {}'.format(part_1(data)))

  print('Solution to part 2: {}'.format(part_2(data)))


if __name__ == '__main__':
  main()
