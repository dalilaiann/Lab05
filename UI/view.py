import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.txt_result = None
        self.txt_container = None
        self._corsi = None
        self._txtMatricola = None
        self.txt_cognome = None
        self._iscriviButton = None
        self._searchCorsiButton = None
        self._searchStudentButton = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        #riga 1 - Corso + Cerca Iscritti
        self._alert = ft.AlertDialog(title=ft.Text("Selezionare un corso"))
        self._corsi=ft.Dropdown(label="corso", hint_text="Selezionare un corso", width=500)
        self._fillDropDown()
        self._btnSearch=ft.ElevatedButton(text="Cerca Iscritti", on_click=self._controller.handle_Search)
        row1=ft.Row([self._corsi, self._btnSearch], alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row1)

        #riga 2 - matricola, nome, cognome
        self._txtMatricola=ft.TextField(label="matricola", width=200)
        self.txt_name=ft.TextField(label="nome", width=200, disabled=True)
        self.txt_cognome=ft.TextField(label="cognome", width=200, disabled=True)
        row2=ft.Row([self._txtMatricola, self.txt_name, self.txt_cognome], alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row2)

        #riga 3 - CercaStudente - Cerca corsi - Iscrivi
        self._searchStudentButton=ft.ElevatedButton(text="Cerca Studente", tooltip="Verifica se c'è uno studente con la matricola specificata", on_click=self._controller.handle_cercaStudente)
        self._searchCorsiButton=ft.ElevatedButton(text="Cerca corsi", on_click=self._controller.handle_CercaCorsi)
        self._iscriviButton=ft.ElevatedButton(text="Iscrivi", on_click=self._controller.handle_Iscrivi)
        row3=ft.Row([self._searchStudentButton, self._searchCorsiButton, self._iscriviButton], alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row3)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self.txt=ft.Text("")
        self.txt_result.controls.append(self.txt)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()

    def _fillDropDown(self):
       corsi=self._controller.get_corsi()

       for c in corsi:
          self._corsi.options.append(ft.dropdown.Option(key=c.codins, text=c.__str__()))