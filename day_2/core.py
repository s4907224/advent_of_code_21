import os


def parse_data():
    """
    Parse the data, into direction & value pairs.  Each line contains a direction, then value, separated by a single space.
    """

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '_res/input.txt'), 'r') as fp:
        return tuple((key, int(value)) for key, value in (line.split(' ') for line in fp.readlines()))


def calculate_position_simple():
    """
    Simply add forward & depth values to the position.
    """

    position = [0, 0]

    for key, value in parse_data():
        if key == 'forward':
            position[0] += value
            continue

        if key == 'up':
            # -- Flip value if we're going upwards.
            value *= -1

        position[1] += value

    return position

def calculate_position_aim():
    position = [0, 0]
    aim = 0

    for key, value in parse_data():
        if key == 'forward':
            position[0] += value
            position[1] += aim * value
            continue

        if key == 'up':
            value *= -1

        aim += value

    return position


def main():
    position_simple = calculate_position_simple()
    print('Solution 1: {}'.format(position_simple[0] * position_simple[1]))

    position_aim = calculate_position_aim()
    print('Solution 2: {}'.format(position_aim[0] * position_aim[1]))

if __name__ == '__main__':
    main()
