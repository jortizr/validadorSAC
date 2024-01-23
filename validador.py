import flet as ft
import requests
from bs4 import BeautifulSoup
class InterfazApp(ft.UserControl):
    def search_guia(self, e):
        #se le pasa los valores del input al texto 
        self.guia.value = self.txt_guia.value
        #se le pasa la guia a la url para completar
        self.url_guia = 'http://wsa/sato/detalleguia.aspx?guia=' + self.txt_guia.value
        #se hace la peticion web a la url
        self.response = requests.get(self.url_guia)
        # Verificar si la petición fue exitosa (código de estado 200)
        if self.response.status_code == 200:
            # Paso 2: Parsear el contenido HTML de la respuesta
            self.soup = BeautifulSoup(self.response.text, 'html.parser')
            # Paso 3: Buscar y extraer elementos por su ID
            self.get_estado = self.soup.find(id='dtlGuias_ctl00_lblEstadoN')
            #verificar si se encontro el elemento
            if self.get_estado:
                #acceder al atributo texto del elemento encontrado por su id
                self.guia_estado.value = str(self.get_estado.text)
                
                self.update()
            else:
                print("no se encontro resultado de la guia")
        else:
            print(f'Error al hacer la petición. Código de estado: {self.response.status_code}')
        
        
        self.txt_guia.value= ""
        #await self.update_async()
        self.update()
    
    def build(self):
        self.color_estado="red"
        self.servidor = 0 #cambiar de int a string
        
        self.txt_guia = ft.TextField(
            hint_text="Ingresa la guia?", on_submit=self.search_guia, expand=True
        )
        self.label_guia = ft.Text("Guia: ",  size=16,   color="white", weight=ft.FontWeight.BOLD)
        self.guia = ft.Text("-",  size=16,   color="green", weight=ft.FontWeight.BOLD)
        self.guia_estado = ft.Text("vacio",  size=16,   color=self.color_estado, weight=ft.FontWeight.BOLD)

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
                                self.guia
                            ]
                            ),
                        ft.Row(
                            
                            # alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            # vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Text("Estado: ",  size=16,   color="white", weight=ft.FontWeight.BOLD),
                                self.guia_estado,
                                ##aqui va el resultado de consulta
                                ft.Text("Consulta: " + str(self.servidor),  size=16,   color="white", weight=ft.FontWeight.BOLD),
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