import flet as ft

# class Estado(ft.UserControl):
#     def __init__(self, guia, data_status):
#         super().__init__()
#         self.guia = guia
#         self.data_status = data_status
        
#     #se crea el form del estado de la guia
#     def build(self):
#         self.display_estado = ft.controls.append(ft.Text("Estado:" . data_status.value))
        
#         return ft.Column(controls=[self.display_estado])
        
        
#         self.display_view = ft.Row(
#             alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
#             vertical_alignment=ft.CrossAxisAlignment.CENTER,
#             controls=[
                
#             ]
#         )
        
        
#         return super().build()


class InterfazApp(ft.UserControl):
    def build(self):
        
        self.txt_guia = ft.TextField(
            hint_text="Ingresa la guia?", on_submit=self.search_guia, expand=True
        )
        #creo una columna para visualizar el estado
        self.estado = ft.Column()
        
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
                ft.Column(
                    spacing=25,
                    controls=[
                        self.estado,
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            
                        )
                    ]
                )
            ]
        )
        
    async def search_guia(self, e):
        ##aqui va la consulta al servidor envia sobre la guia
        #a validar el estado
        # if self.txt_guia.value:
        #     resultado = Estado(self.new_task.value)
        #     self.estado.controls.append(task)
        #     self.new_task.value = ""
        #     await self.new_task.focus_async()
        #     await self.update_async(
        print(self.txt_guia.value)
        await self.update_async()



async def main(page: ft.Page):
    page.title = "Validador de estado SAC"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.ADAPTIVE

    # create app control and add it to the page
    await page.add_async(InterfazApp())


ft.app(main)