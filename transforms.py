def midpoint(v1, v2):
    return ((v1[0] + v2[0]) / 2.0, (v1[1] + v2[1]) / 2.0)


def reflection(base, vx):
    vec = (vx[0] - base[0], vx[1] - base[1])
    return (base[0] - vec[0], base[1] - vec[1])


class Line:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def reflect(self, vx):
        # Use the dot product formula: a \dot b = |a||b| \cos(\theta)
        # First compute the angle and then use trig to compute

        # pick v1 as the base point

        vecb = self.v2 - self.v1

        veca = vx - self.v1

        # proj = a \dot b / |b|
        # nearest = self.v1 + proj * vecb

        return nearest - (vx - nearest)

    def rotate_perpendicular(self):
        mid = ((self.v1[0] + self.v2[0]) / 2.0, (self.v1[1] + self.v2[2]) / 2.0)
        vec1 = (self.v1[0] - mid[0], self.v1[1] - mid[1])
        vec2 = (self.v2[0] - mid[0], self.v2[1] - mid[1])

        fv1 = (mid[0] + vec1[1], mid[1] - vec1[0])
        fv2 = (mid[0] + vec2[1], mid[1] - vec2[0])
        return self.__class__(fv1, fv2)
