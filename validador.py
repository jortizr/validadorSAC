import flet as ft

class InterfazApp(ft.UserControl):
    def search_guia(self, e):
        #se le pasa los valores del input al texto 
        self.label_estado.value = self.txt_guia.value


        #self.txt_guia.value= ""
        #await self.update_async()
        self.update()
    
    def build(self):
        self.color_estado="red"
        self.estado_guia="Entregado"
        
        self.txt_guia = ft.TextField(
            hint_text="Ingresa la guia?", on_submit=self.search_guia, expand=True
        )
        self.label_guia = ft.Text("Guia: ",  size=16,   color="white", weight=ft.FontWeight.BOLD)
        self.label_estado = ft.Text("-",  size=16,   color="green", weight=ft.FontWeight.BOLD)
        #devuelve de la funcion el control con los componentes creados en la interfaz
        return ft.Column(
            width=400,
            top=30,
            controls=[
                #creo el encabezado en una fila dentro de una columna
                ft.Row(
                    [ ft.Text(value="Validador de estados GUIA", style=ft.TextThemeStyle.HEADLINE_MEDIUM)],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                #fila para posicionar el input
                ft.Row(
                    controls=[
                        #llamo el componente del input
                        self.txt_guia,
                        #le creo un boton
                        ft.FloatingActionButton(
                            icon=ft.icons.ADD, on_click=self.search_guia
                        )
                    ]
                ),
                ft.Divider(height=2, color="white"),
                ft.Column(
                    spacing=25,
                    controls=[
                        ft.Row(
                            controls=[
                                self.label_guia,
                                self.label_estado
                            ]
                            ),
                        ft.Row(
                            
                            # alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            # vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Text("Estado: ",  size=16,   color="white", weight=ft.FontWeight.BOLD),
                                ft.Text(self.estado_guia,  size=16,   color=self.color_estado, weight=ft.FontWeight.BOLD)      
                                      ]
                            
                        ),
                        ft.Divider(height=1)
                        
                    ]
                )
            ]
        )



def main(page: ft.Page):
    page.title = "Validador de estado SAC"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.ADAPTIVE

    # create app control and add it to the page
    page.add(InterfazApp())


ft.app(main)