import math
import operator
from tqdm import tqdm


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


def rate_approximation(x, approximation):
    return abs(approximation - x)


def generate_approximation():
    score_dict = {}
    for x in tqdm(range(1, 1000)):
        for y in range(1, 1000):
            score = rate_approximation(x/y, math.e)
            score_dict[score] = [x, y]
    best = min(score_dict.items(), key=operator.itemgetter(0))
    common = gcd(best[1][0], best[1][1])
    best[1][0] //= common
    best[1][1] //= common
    print(best)


if __name__ == "__main__":
    generate_approximation()
