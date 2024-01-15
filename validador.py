import flet as ft





async def main(page: ft.Page):
    page.title = "Validador de estado SAC"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.ADAPTIVE

    # create app control and add it to the page
    await page.add_async(TodoApp())


ft.app(main)