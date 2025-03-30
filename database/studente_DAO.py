# Add whatever it is needed to interface with the DB Table corso
from database.DB_connect import get_connection
from model import studente


class Student_DAO:

    def __init__(self):
        pass

    def get_studenti(self):
        """Restituisce tutti gli studenti presenti nel db"""
        db = get_connection()
        results = []

        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM studente")

        for row in cursor:
            results.append(studente.Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"]))

        db.close()
        return results

    def get_studenti_corso(self, value):
            """Restituisce tutti gli studenti iscritti al corso con il codice indicato"""
            db = get_connection()
            results=[]
            cursor = db.cursor(dictionary=True)
            query = """SELECT * FROM iscrizione i, studente s WHERE (i.codins=%s and i.matricola=s.matricola)"""

            cursor.execute(query, (value,))

            for row in cursor:
                results.append(studente.Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"]))

            db.close()
            return results

    def search_studente(self, matricola):
        """Restituisce un oggetto Studente con la matricola indicata"""
        db=get_connection()
        cursor=db.cursor(dictionary=True)

        query="""SELECT * FROM studente WHERE matricola=%s"""

        cursor.execute(query, (matricola,))

        for row in cursor:
            return studente.Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"])

        db.close()

if __name__ == '__main__':
    s=Student_DAO()
    s.search_studente("190635")
    print(str(s))

