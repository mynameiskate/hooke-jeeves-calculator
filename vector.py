class Vector:
    def __init__(self, values):
        self.values = values.copy()

    def __repr__(self):
        result = ''
        for value in self.values:
            result += ' {}'.format(value)

        return '(' + result + ' )'

    def __add__(self, other):
        assert(len(self.values) == len(other.values))
        result = []
        for index in range(0, len(self.values)):
            result.append(self.values[index] + other.values[index])

        return Vector(result)

    def __sub__(self, other):
        assert(len(self.values) == len(other.values))
        result = []
        for index in range(0, len(self.values)):
            result.append(self.values[index] - other.values[index])

        return Vector(result)

    def __rmul__(self, other):
        result = []
        for index in range(0, len(self.values)):
            result.append(self.values[index] * other)

        return Vector(result)

    def __len__(self):
        return len(self.values)

    def __getitem__(self, i):
        if 0 <= i <= len(self):
            return self.values[i]
        raise IndexError('Vector: index {} is out of range'.format(i))

    def __setitem__(self, key, value):
        if 0 <= key <= len(self):
            self.values[key] = value
        else:
            raise IndexError('Vector: index {} is out of range'.format(key))

    def __truediv__(self, other):
        result = []
        for index in range(0, len(self.values)):
            result.append(self.values[index] / other)

        return Vector(result)

    def copy(self):
        return Vector(self.values.copy())

    def module(self, other):
        assert (len(self.values) == len(other.values))
        result = 0
        for index in range(0, len(self.values)):
            result += (self.values[index] - other.values[index]) ** 2

        return result

    @staticmethod
    def ones(length):
        return Vector([1] * length)

    @staticmethod
    def zeros(length):
        return Vector([0] * length)

    @staticmethod
    def diag(arr):
        length = len(arr)
        matrix = []

        for row in range(0, length):
            matrix.append(Vector.zeros(length))
            matrix[row][row] = arr[row]

        return matrix
