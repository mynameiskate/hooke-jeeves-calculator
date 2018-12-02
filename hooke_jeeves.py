from vector import Vector


class HookeJeevesMethod:
    def __init__(self, func, dimensions):
        """
        :param func: target function
        :param dimensions: the amount of dimensions
            (function variables
        """
        self.func = func
        self.dimensions = dimensions

    def _calc_next_point(self, point, delta, e):
        """Calculates next point in one of the N dimensions

        :param point: previously calculated point
        :param delta: step between points
        :param e: base vector
        :return: next base point
        """
        current_value = self.func(point)

        if self.func(point + delta * e) < current_value:
            return point + delta * e
        elif self.func(point - delta * e) < current_value:
            return point - delta * e
        else:
            return point

    def calculate(self, eps, speed=2, division_step=2):
        """Minimizes function with N variables using
            Hooke-Jeeves method

        :param eps: level of function accuracy
        :param speed: speed coefficient
        :param division_step: step division coefficient
        :return: list of all intermediate points with
            the last one as result
        """
        result = []
        delta = 1
        e = Vector.diag(Vector.ones(self.dimensions))
        x = [Vector.ones(self.dimensions)]
        y = [Vector.ones(self.dimensions)]

        while True:
            result.append(x[-1])

            for index in range(0, self.dimensions):
                y.append(self._calc_next_point(y[-1], delta, e[index]))

            if not (self.func(y[-1]) < self.func(x[-1])):
                delta /= division_step
                x.append(x[-1])
                y = [x[-1]]
            else:
                x.append(y[-1])
                y = [y[0] + speed * (x[-1] - x[-2])]

                if ((abs(self.func(x[-1]) - self.func(y[-1])) < eps)
                        or (x[-1].module(y[-1]) < eps)):
                    result.append(y[-1])

                    return result
