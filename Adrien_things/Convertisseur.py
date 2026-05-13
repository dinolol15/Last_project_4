"""
Programme qui convertit une matrice de tile en une matrice de bytes

Auteur: Adrien Buschbeck
"""

from matrix_manager import Matrix, get
from Tile import Tile


def convertisseur(matrix: Matrix[Tile]) -> bytes:
    """
    Convertit une matrice de tile en une matrice de bytes
    """
    coords = [
        (i, j)
        for j in range(len(matrix[len(matrix) - 1]))
        for i in range(len(matrix))
    ]
    bytestr: bytes = b""
    for c in coords:
        print(c)
        cell = get(matrix, c)
        cell_new = cell.Color + (255,)
        print(cell_new)
        bb = b""
        for i in cell_new:
            bb += i.to_bytes(1)
        bytestr += bb

    return bytestr
