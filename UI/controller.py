import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_Search(self,e):
        """ Funzione che gestisce la ricerca di tutti gli studenti iscritti al corso specificato e li stampa"""
        corso=self._view._corsi.value

        if corso is None or corso == "":
             self._view.create_alert("Selezionare un corso!")
             return

        self._view.txt.value=""
        results=self._model.get_studenti(self._view._corsi.value)
        self._view.txt.value=f"Ci sono {len(results)} iscritti al corso: "

        for studente in results:
            self._view.txt.value+="\n"+str(studente)

        self._view.update_page()


    def handle_cercaStudente(self, e):
        """Funzione che controlla se la matricola di uno studente esiste o meno"""

        studente=self._model.get_studente(self._view._txtMatricola.value)

        if studente is None:
            self._view.create_alert("Non esiste nessun studente con questa matricola!")
        else:
            self._view.txt_name.value=studente.nome
            self._view.txt_cognome.value=studente.cognome
        self._view.update_page()


    def handle_CercaCorsi(self, e):
        """Funzione che stampa tutti i corsi di uno studente"""

        studente=self._model.get_studente(self._view._txtMatricola.value)

        if studente is not None:
            corsi=self._model.get_corsi_studente(studente.matricola)
            self._view.txt.value=f"Risultano {len(corsi)} corsi:"
            for c in corsi:
                self._view.txt.value+="\n"+str(c)
        else:
            self._view.create_alert("Non esiste nessun studente con questa matricola!")

        self._view.update_page()

    def handle_Iscrivi(self, e):
        """Funzione che iscrive uno studente ad un corso"""

        studente=self._model.get_studente(self._view._txtMatricola.value)
        corso=self._model.get_corso(self._view._corsi.value)

        if (studente is not None) and (corso is not None):
            self._model.iscrivi(studente, corso)
        else:
            if corso is None:
                self._view.create_alert("Non esiste questo corso")
            else:
                self._view.create_alert("Non esiste nessun studente con questa matricola!")

    def get_corsi(self):
        """Funzione che restituisce tutti i corsi presenti nel db"""
        return self._model.get_corsi