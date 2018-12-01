from vector import Vector


class HookeJeevesMethod:
    def __init__(self, func):
        self.func = func

    def _calc_next_point(self, point, delta, e):
        current_value = self.func(point)

        if self.func(point + delta * e) < current_value:
            return point + delta * e
        elif self.func(point - delta * e) < current_value:
            return point - delta * e
        else:
            return point

    def calculate(self, eps, speed=2, division_step=2):
        result = []
        delta = 1
        e = [Vector([1, 0, 0, 0, 0]),
             Vector([0, 1, 0, 0, 0]),
             Vector([0, 0, 1, 0, 0]),
             Vector([0, 0, 0, 1, 0]),
             Vector([0, 0, 0, 0, 1])]

        x = [Vector([1, 1, 1, 1, 1])]
        y = [Vector([1, 1, 1, 1, 1])]

        while True:
            result.append(x[-1])

            for index in range(0, len(e)):
                y.append(self._calc_next_point(y[-1], delta, e[index]))

            if not (self.func(y[-1]) < self.func(x[-1])):
                delta /= division_step
                y = [x[-1]]
                x.append(x[-1])
            else:
                x.append(y[-1])
                y = [x[-1] + speed * (x[-1] - x[-2])]

                if ((abs(self.func(x[-1]) - self.func(y[-1])) < eps)
                        or (x[-1].module(y[-1]) < eps)):
                    result.append(y[-1])

                    return result
