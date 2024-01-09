import flet as ft


def main(page: ft.Page):
    def validarStatus(e):
        page.add()
    page.add(ft.Text(value="Hello, world!"))

ft.app(target=main)