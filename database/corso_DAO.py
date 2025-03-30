# Add whatever it is needed to interface with the DB Table corso
from database.DB_connect import get_connection
from model import corso

class Corso_DAO:
    def __init__(self):
        pass

    def get_corsi(self):
         """Restituisce tutti i corsi presenti nel db"""
         db=get_connection()
         results=[]

         cursor=db.cursor(dictionary=True)
         cursor.execute("SELECT * FROM corso")

         for row in cursor:
             results.append(corso.Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))


         return results

    def cerca_corsi_studente(self, matricola):
        """Restituisce tutti i corsi a cui lo studente con la matricola indicata è iscritto"""
        db = get_connection()
        cursor = db.cursor(dictionary=True)

        query = "SELECT * FROM corso c, iscrizione i WHERE (i.matricola=%s AND i.codins=c.codins)"
        cursor.execute(query, (matricola, ))

        res=[]
        for row in cursor:
            res.append(corso.Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))

        db.close()
        return res

    def iscrivi(self, matricola, corso):
        """Iscrive lo studente con la matricola specificata al corso indicato"""
        db=get_connection()
        cursor=db.cursor(dictionary=True)

        query="INSERT INTO iscrizione (matricola,codins) VALUES (%s, %s)"
        cursor.execute(query, (matricola, corso))

        db.commit()
        db.close()

    def hasStudente(self, matricola, corso):
        """Verifica se lo studente con la matricola indicata è iscritto al corso con il codice indicato."""
        db = get_connection()
        cursor = db.cursor(dictionary=True)

        query="SELECT * FROM iscrizione i WHERE (i.matricola=%s AND i.codins=%s)"

        cursor.execute(query, (matricola, corso))

        return len(cursor.fetchall())>0

    def get_corso(self, cod):
        "Restituisce oggetto Corso con il codice indicato"
        db = get_connection()

        cursor = db.cursor(dictionary=True)
        query="SELECT * FROM corso WHERE codins=%s"

        cursor.execute(query, (cod,))

        for row in cursor:
            return corso.Corso(row["codins"], row["crediti"], row["nome"], row["pd"])


if __name__ == '__main__':
    dao_class=Corso_DAO()
    print(dao_class.hasStudente("190635", "01KSUPG"))

