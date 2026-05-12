"""
Fichier contenant la classe Tile

Auteur: Adrien Buschbeck
"""

import dataclasses as dc
from dataclasses import dataclass


@dataclass(eq=True)
class Tile:
    """
    Classe représentant les différents types de terrains
    Name --> Nom
    Colour --> couleur par laquelle le terrain va être représenté (systèem RGB)
    wfc_delete --> terrain qui ne peuvent pas être à côté (conectivité 4)
    """

    Name: str
    Color: tuple[int, int, int] = dc.field(
        default_factory=tuple[int, int, int]
    )
    wfc_delete: list["Tile"] = dc.field(
        default_factory=list["Tile"]
    )  # not hashable, to do with enum and namedtuple
    # wealth: float will add if time and if Albert
    # wildness: float will add if time and if Albert

    def __repr__(self):
        return self.Name[0]

    def __hash__(self):
        return hash(self.Name)


Placeholer = Tile(
    "Placeholer",
    (255, 255, 255),
    [],
)  # (0, 0,)
