"""
Programme créant une carte

Auteur: Adrien Buschbeck
"""

from collections import Counter
import random as ran
import matrix_manager as mm
from matrix_manager import Position, Matrix, set, get
from Tile import Tile
from typing import cast

# faire enum et NamedTule
Plain = Tile("Plain", (124, 252, 0), [])  # (1, 1,)
Mountain = Tile("Mountain", (139, 137, 137), [])  # (0.25, 10,)
Forest = Tile("Forest", (34, 139, 34), [])  # (1.25, 5,)
Sea = Tile("Sea", (28, 107, 160), [])  # (0, 10000,)
River = Tile("River", (70, 130, 180), [])  # (0, 3,)
Desert = Tile("Desert", (237, 201, 175), [])  # (0.1, 0.5,)

# obligatoire pour w_f_c_evolved
Water = Tile("Water", (70, 130, 180), [])  # (1, 1,)
Coast = Tile("Coast", (237, 201, 175), [])  # (1, 1,)
Ground = Tile("Ground", (34, 139, 34), [])  # (1, 1,)


Tile.application_wfc_delete(Plain, [Sea, River])
Tile.application_wfc_delete(Mountain, [Sea, River])
Tile.application_wfc_delete(Forest, [Sea, Desert, River])
Tile.application_wfc_delete(Desert, [Sea, Forest])
Tile.application_wfc_delete(River, [Plain, Mountain, Forest])
Tile.application_wfc_delete(Sea, [Plain, Mountain, Forest, Desert])
Tile.application_wfc_delete(Water, [Ground])
Tile.application_wfc_delete(Ground, [Water])


def water_placement(
    matrix: Matrix[dict[Tile, int] | Tile],
    coordinate: list[Position],
    humidity: int,
    set_of_value: dict[Tile, int] = {Water: 1},
) -> tuple[
    list[Position], Matrix[dict[Tile, int] | Tile], list[Position]
]:
    """
    Place des zones d'eau de départ
    humidity --> nombres de point d'eau aux départs
    """
    coords_water: list[Position] = []
    for _ in range(humidity):
        coord = ran.choice(coordinate)
        coords_water.append(coord)
        coordinate.remove(coord)
    matrix = mm.matrix_change(matrix, coords_water, set_of_value)
    return (coordinate, matrix, coords_water)


def w_f_c_evolved(
    matrix: Matrix[dict[Tile, int] | Tile],
    water_p_val: int,
    ran_wal_value: tuple[int, int, Tile],
    humidity: int = 1,
):
    """
    Retourne une matrix générée avec un wfc simplifié

    Les éléments de la matrix doivent être des listes
    ne marche qu'avec un triple élément

    water_p_val --> nombre de tuiles d'eau placées au départ
    """

    COORDINATES = [
        (i, j)
        for j in range(len(matrix[len(matrix) - 1]))
        for i in range(len(matrix))
    ]
    coordinates = COORDINATES
    coordinates, matrix, water_coordinates = water_placement(  # ToDo
        matrix, coordinates, water_p_val
    )

    for _ in range(humidity):
        matrix = mm.random_walk(
            matrix,
            water_coordinates,
            ran_wal_value[0],
            ran_wal_value[1],
            ran_wal_value[2],
        )

    for p in COORDINATES:
        matrix = mm.in_concact(matrix, p, Water, Coast, Water)
        cell = get(matrix, p)
        if cell != Water and cell != Coast:
            set(matrix, Ground, p)

    for p in COORDINATES:
        matrix = mm.fill(matrix, p)

    return matrix


def w_f_c_simplified(
    matrix: Matrix[dict[Tile, int] | Tile],
) -> Matrix[Tile | dict[Tile, int]]:
    """
    Retourne une matrix générée avec un wfc simplifié

    Les éléments de la matrix doivent être des listes
    """

    COORDINATES = [
        (i, j)
        for j in range(len(matrix[len(matrix) - 1]))
        for i in range(len(matrix))
    ]
    coordinates = [
        (i, j)
        for j in range(len(matrix[len(matrix) - 1]))
        for i in range(len(matrix))
    ]
    test_value = len(matrix) * len(matrix[len(matrix) - 1])

    while test_value != 0:
        cell = mm.lobject_cell(matrix, coordinates)  # ToDO
        coordinates.remove((cell[0][0], cell[0][1]))
        if len(cell[1]) == 0:  # ToDo
            print("Contradiction atteinte")
            print(test_value)
            break

        matrix[cell[0][0]][cell[0][1]] = ran.choice(
            list(Counter(cell[1]).elements())
        )  # ToDo
        condition(matrix, (cell[0][0], cell[0][1]))
        test_value -= 1

    for i in COORDINATES:
        matrix = mm.fill(matrix, i)

    return matrix


def condition(
    matrix: Matrix[dict[Tile, int] | Tile], position: Position
):
    """
    Enlève les possibilitées impossibles avec l'argument wfc_delete

    position[0] : axe -y
    position[1] : axe x
    """
    cell = get(matrix, position)
    for i in range(4):
        match i:  # ToDo
            case 0:
                tested_cell = mm.up(matrix, position)
            case 1:
                tested_cell = mm.down(matrix, position)
            case 2:
                tested_cell = mm.right(matrix, position)
            case 3:
                tested_cell = mm.left(matrix, position)
            case _:
                raise ValueError("The number must stay 4.")

        if tested_cell is None or isinstance(tested_cell[1], Tile):
            continue
        for i in cast(
            Tile, cell
        ).wfc_delete:  # ToDo référence dictionnaire
            cast(tuple[Position, dict[Tile, int]], tested_cell)[1].pop(
                i, None
            )


# ToDo
"""def convertisseur_affichage(matrix: mm.Matrix[U])
     -> mm.Matrix[Tile.Color]: 
    Convertit une matrice de type U en une matrice de type Tile
    for i in matrix:
        i = i.Color
    return matrix
    """


if __name__ == "__main__":

    matrix_test_1 = w_f_c_simplified(
        mm.create_matrix(
            (10, 10),
            {Plain: 3, Mountain: 1, Forest: 2, Desert: 2, Sea: 1, River: 2},
        )
    )

    matrix_test_2 = w_f_c_evolved(
        mm.create_matrix((10, 10), {}), 5, [25, 1, Water]
    )

    print("\n".join([str(i) for i in matrix_test_1]))

    print("\n".join([str(i) for i in matrix_test_2]))
