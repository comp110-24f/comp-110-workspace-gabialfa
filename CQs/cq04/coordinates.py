"""Coordinates"""

__author__ = "730746935"


def get_coords(xs: str, ys: str) -> None:
    index_x: int = 0
    index_y: int = 0
    while len(xs) > index_x:
        while len(ys) > index_y:
            print(f"({xs[index_x]}, {ys[index_y]})")
            index_y += 1
        index_x += 1
        index_y = 0
