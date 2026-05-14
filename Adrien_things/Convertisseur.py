"""
Programme qui convertit une matrice de tile en une matrice de bytes

Auteur: Adrien Buschbeck, Albert Stanislawek
"""


def convertisseur(matrix) -> bytes:
    """
    Convertit une matrice de tile en une matrice de bytes
    """

    dim_x = len(matrix)
    dim_y = len(matrix[0])

    bytestr: bytes = b""
    for y in range(dim_y):
        for x in range(dim_x):
            cell = matrix[y][x]
            t = cell + (255,)
            bb = b""
            for i in t:
                bbb = i.to_bytes(1, byteorder="big")
                bb += bbb
            bytestr += bb

    return bytestr

m = [
    [(5, 6, 7), (5, 6, 7)],
    [(5, 6, 7), (5, 6, 7)],
]

print(convertisseur(m))
