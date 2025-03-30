from database import corso_DAO, studente_DAO


class Model:

    def __init__(self):
        self._DAOcorsi=corso_DAO.Corso_DAO()
        self._DAOstudenti=studente_DAO.Student_DAO()

    @property
    def get_corsi(self):
        """Funzione che restituisce tutti i corsi presenti nel db"""
        return self._DAOcorsi.get_corsi()

    def get_studenti(self, value):
        """Funzione che restituisce tutti gli studenti presenti nel db"""
        matricole=self._DAOstudenti.get_studenti_corso(value)
        return matricole

    def get_studente(self, matricola):
        """Funzione che restituisce l'oggetto Studente corrispondente alla matricola passata come parametro."""
        return self._DAOstudenti.search_studente(matricola)

    def get_corsi_studente(self, matricola):
        """Funzione che restituisce tutti i corsi a cui lo studente con la matricola passata come parametro è iscritto"""
        return self._DAOcorsi.cerca_corsi_studente(matricola)

    def iscrivi(self, studente, corso):
        """Funzione che iscrive lo studente passato come parametro al corso specificato"""
        if not (self._DAOcorsi.hasStudente(studente.matricola, corso.codins)):
            self._DAOcorsi.iscrivi(studente.matricola, corso.codins)

    def get_corso(self, cod):
        """Funzioen che restituisce il corso con il codice passato come parametro."""
        return self._DAOcorsi.get_corso(cod)



if __name__=='__main__':
    istanza=Model()
    s=istanza.get_studente("190635")
    print(s)
