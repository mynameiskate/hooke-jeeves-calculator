from hooke_jeeves import HookeJeevesMethod


def func(point):
    """Example 5D function"""
    return (4000 / point[0] + 8 * point[0]
            + 7200 / point[1] + 4 * point[1]
            + 8800 / point[2] + 4 * point[2]
            + 6300 / point[3] + 3.5 * point[3]
            + 1600 / point[4] + 2 * point[4])


def print_iteration(x, step):
    print('Iteration no.{}'.format(step))
    print('X vector: {}'.format(x))
    print('F = {}'.format(func(x)))
    print('_' * 100)


result = HookeJeevesMethod(func).calculate(0.00001)
count = 0

for point in result:
    print_iteration(point, count)
    count += 1
