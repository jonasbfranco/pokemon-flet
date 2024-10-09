import flet as ft

def main(page: ft.Page):
    page.window.width = 420
    page.window.height = 780
    page.window.resizable = False
    page.window.maximizable = False
    page.theme_mode = ft.ThemeMode.DARK
    page.window.always_on_top = True
    

    WIDTH = page.window.width
    HEIGHT = page.window.height

    numero_pokemon = 1
    

    # Função para visualizar o Pokémon anterior
    def preview_pokemon(e):
        pass

    # Função para visualizar o próximo Pokémon
    def next_pokemon(e):
        pass


    # endereco da imagem do pokemon
    sprite_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/{numero_pokemon}.svg"

    # Renderizando a imagem
    imagem = ft.Image(
        src=sprite_url,
        scale=1,
        width=200,
        height=200
    )

    


    
    page.add(
        ft.Container(
            bgcolor="#FFFFFF",
            width=400,
            height=720,
            border_radius=35,
            padding=ft.padding.only(left=0, top=0, right=0, bottom=0),
            
            content=ft.Stack(
                controls=[
                    ft.Container(
                        bgcolor=ft.colors.GREEN_200,
                        height=HEIGHT - 540,
                    ),
                    ft.Container(
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        imagem,
                                    ],
                                ),
                            ],
                        ),
                        bgcolor="#F79F1F",
                        padding=10,
                        border_radius=35,
                        width=WIDTH,
                        height=HEIGHT - 500,
                    ),

                    
                    ft.Column(
                        top=120,
                        left=10,
                        right=10,
                        width=WIDTH -60,
                        controls=[
                            ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    ft.FloatingActionButton(
                                        icon=ft.icons.ARROW_BACK,
                                        height=35,
                                        width=35,
                                        bgcolor="#2D3436",
                                        opacity=0.9,
                                        on_click=preview_pokemon
                                    ),
                                    ft.FloatingActionButton(
                                        icon=ft.icons.ARROW_FORWARD,
                                        height=35,
                                        width=35,
                                        bgcolor="#2D3436",
                                        opacity=0.9,
                                        on_click=next_pokemon
                                    ),
                                ]
                            ),
                        ]
                    ),

                ],
            ), # fim da Stack
        ), # fim do Container principal
    )




    page.update()

ft.app(target=main)