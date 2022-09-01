import operator
import click
from tqdm import tqdm


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


def rate_approximation(x, approximation):
    return abs(approximation - x)


@click.command()
@click.option('--num', help='Number to approximate', required=True)
def generate(num):
    """Generate an approximation"""
    if not num.replace(".", "").isnumeric():
        click.echo("--num must be a number")
        return
    num = float(num)
    score_dict = {}
    for x in tqdm(range(1, 1000)):
        for y in range(1, 1000):
            score = rate_approximation(x/y, num)
            score_dict[score] = [x, y]
    best = min(score_dict.items(), key=operator.itemgetter(0))
    common = gcd(best[1][0], best[1][1])
    best[1][0] //= common
    best[1][1] //= common
    click.echo("     Result     ")
    click.echo("-"*17)
    click.echo(f"Score (lower is better) : {best[0]}")
    click.echo(f"Approximation (fraction): {best[1]}")
