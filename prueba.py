import flet as ft

class Counter(ft.UserControl):
    def add_click(self, e):
        self.counter += 1
        self.text.value = str(self.counter)
        self.update()

    def build(self):
        #se crea la variable iniciada
        self.counter = 0
        #se crea el componente de texto que se va a actualizar
        self.text = ft.Text(str(self.counter))
        
        self.txt_guia = ft.TextField(
            hint_text="Ingresa la guia?", on_submit=self.add_click, expand=False
        )
        
        #se retornan los elementos a la pagina
        return ft.Row(
            [self.txt_guia,
             self.text,
             ft.ElevatedButton("Add", on_click=self.add_click)])

def main(page):
    page.add(Counter())

ft.app(target=main)