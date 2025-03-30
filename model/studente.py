from dataclasses import dataclass

@dataclass
class Studente:

    matricola: int
    cognome:str
    nome: str
    cds:str

    def __hash__(self):
        return self.matricola

    def __eq__(self, other):
        return self.matricola==other.matricola

    def __str__(self):
        return f"{self.nome}, {self.cognome} ({self.matricola})"