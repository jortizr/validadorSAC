import flet as ft





def main(page: ft.Page):
    interfaz = ft.Row(
        controls=[
            ft.TextField(label="ingresa la guia"),
            
        ]
    )
        
    page.add(interfaz)

ft.app(target=main)