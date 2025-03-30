from dataclasses import dataclass

from networkx.classes import non_edges


@dataclass
class Corso:
    codins:str
    crediti:int
    nome:str
    pd:int

    def __str__(self):
        return f"{self.nome} ({self.codins})"

    def __hash__(self):
        return self.nome

    def __eq__(self, other):
        return self.nome==other.nome

