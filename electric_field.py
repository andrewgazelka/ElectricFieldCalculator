import math

import numpy as np
import matplotlib.pyplot as plot


def calculate_field(q_total: float, rod_length: float, dy: float, data_points: int = 1000):
    dq = q_total / data_points
    max_displacement = rod_length / 2

    E_total_x = 0
    E_total_y = 0

    for dx in np.linspace(-max_displacement, max_displacement, data_points):
        dist2 = dx * dx + dy * dy
        dE_mag = dq / dist2

        dE = get_components(dx, dy, dE_mag)

        E_total_x += dE[0]
        E_total_y += dE[1]

    return (E_total_x, E_total_y)


def get_components(dx, dy, mag):
    """
    Given a vector (dx,dy), find a vector (a,b), where ||(a,b)|| = mag
    :param dx: The difference in x between a point
    :param dy: The difference in y between a point
    :param mag: the magnitude of the vector
    :return:
    """

    # We have
    # (1) -> {F_y}^2 + {F_x}^2 = mag^2
    # (2) -> {dy}/{dx} = {F_y}/{F_x}

    # ==> {F_x} {dy}/{dx} = {F_y}
    # ==> ({F_x} {dy}/{dx})^2 + {F_x}^2 = mag^2
    # ==> {F_x}^2 (1+ ({dy}/{dx})^2) = mag^2
    # ==> F_x = mag / sqrt(1+{dy}/{dx})^2)

    # F_y = sqrt(mag^2-{F_x}^2)

    if dx == 0:
        F_x = 0
        F_y = mag
    elif dy == 0:
        F_x = mag
        F_y = 0
    else:
        F_x = mag / math.sqrt(1 + (dy / dx) ** 2)
        F_y = math.sqrt(mag ** 2 - F_x ** 2)

    return math.copysign(F_x, dx), math.copysign(F_y, dy)


if __name__ == '__main__':

    data = []
    for i in range(1,100):
        result = calculate_field(q_total=100, rod_length=10, dy=0.04, data_points=i)
        to_append = (i, result[1])
        data.append(to_append)
        print(to_append)
    plot.plot(data)
    plot.show()
