import flet as ft
import aiohttp
import asyncio

def main(page: ft.Page):
    page.window.width = 420
    page.window.height = 780
    page.window.resizable = False
    page.window.maximizable = False
    page.theme_mode = ft.ThemeMode.DARK
    page.window.always_on_top = True

    page.fonts = {
        "zpix": "https://github.com/SolidZORO/zpix-pixel-font/releases/download/v3.1.9/zpix.ttf",
        "Poppins": "fonts/Poppins-Regular.ttf"
    }
   
    page.theme = ft.Theme(font_family="Poppins")
    page.update()
    

    WIDTH = page.window.width
    HEIGHT = page.window.height

    numero_pokemon = ft.Ref[int]()
    numero_pokemon.current = 1

    
    async def buscar_pokemon(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.json() 


    nivel = 3


    def update_pokemon_image():
        sprite_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/{numero_pokemon.current}.svg"
        imagem.src = sprite_url
        page.update()
    

    # Função para visualizar o Pokémon anterior
    async def preview_pokemon(e):
        if numero_pokemon.current == 1:
            numero_pokemon.current = 150
            
            resultado = await buscar_pokemon(f"https://pokeapi.co/api/v2/pokemon/{numero_pokemon.current}")
            sprite_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/{numero_pokemon.current}.svg" 
            name = f"{resultado['name']}"
            imagem.src = sprite_url
            nome.value = name
            numero.value = numero_pokemon.current

            tipo = f"{resultado['types'][0]['type']['name']}"
            tipo_pokemon.value = tipo

            height = f"{resultado['height']} Kg"
            peso_pokemon.value = height

            page.update()
            ## update_pokemon_image()
        elif numero_pokemon.current > 1:
            numero_pokemon.current -= 1

            resultado = await buscar_pokemon(f"https://pokeapi.co/api/v2/pokemon/{numero_pokemon.current}")
            sprite_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/{numero_pokemon.current}.svg" 
            name = f"{resultado['name']}"
            imagem.src = sprite_url
            nome.value = name
            numero.value = numero_pokemon.current

            tipo = f"{resultado['types'][0]['type']['name']}"
            tipo_pokemon.value = tipo

            height = f"{resultado['height']} Kg"
            peso_pokemon.value = height

            page.update()

            ## update_pokemon_image()

    # Função para visualizar o próximo Pokémon
    async def next_pokemon(e):
        if numero_pokemon.current == 150:
            numero_pokemon.current = 1

            resultado = await buscar_pokemon(f"https://pokeapi.co/api/v2/pokemon/{numero_pokemon.current}")
            sprite_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/{numero_pokemon.current}.svg" 
            name = f"{resultado['name']}"
            imagem.src = sprite_url
            nome.value = name
            numero.value = numero_pokemon.current

            tipo = f"{resultado['types'][0]['type']['name']}"
            tipo_pokemon.value = tipo

            height = f"{resultado['height']} Kg"
            peso_pokemon.value = height

            page.update()

            ## update_pokemon_image()
        elif numero_pokemon.current > 0:
            numero_pokemon.current += 1
            
            resultado = await buscar_pokemon(f"https://pokeapi.co/api/v2/pokemon/{numero_pokemon.current}")
            sprite_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/{numero_pokemon.current}.svg" 
            name = f"{resultado['name']}"
            imagem.src = sprite_url
            nome.value = name
            numero.value = numero_pokemon.current

            tipo = f"{resultado['types'][0]['type']['name']}"
            tipo_pokemon.value = tipo

            height = f"{resultado['height']} Kg"
            peso_pokemon.value = height


            page.update()

            ## update_pokemon_image()



    # Renderizando a imagem
    imagem = ft.Image(
        src=f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/{numero_pokemon.current}.svg",
        scale=1,
        width=200,
        height=200
    )


    nome = ft.Text(
                value="bulbasaur", 
                color="#353B48", 
                size=36, 
                weight="bold", 
                font_family="zpix"
            )

    numero = ft.Text(
                value=f"#001", 
                color="#7F8C8D", 
                size=18, 
                weight="bold", 
                font_family="zpix"
            )

    tipo_pokemon = ft.Text(
                value=f"grass", 
                color="#FFFFFF", 
                size=16, 
                weight="bold", 
                font_family="zpix"
            )

    peso_pokemon = ft.Text(
                value=f"{7} kg", 
                color='#000000', 
                size=22, 
                weight='bold', 
                opacity=0.6,
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


                    ft.Column(
                        spacing=0,
                        top=290,
                        left=20,
                        right=20,
                        alignment=ft.CrossAxisAlignment.START,
                        controls=[
                            ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                width=WIDTH,
                                height=100,
                                controls=[
                                    ft.Column(
                                        spacing=0,
                                        height=100,
                                        controls=[
                                            nome,
                                            numero,
                                        ],
                                    ),

                                    ft.Row(
                                        height=46,
                                        spacing=10,
                                        controls=[
                                            ft.Column(
                                                spacing=0,
                                                alignment=ft.MainAxisAlignment.END,
                                                controls=[
                                                    ft.Text(value=f"Nível", color="#7F8C8D", size=10, weight="bold", font_family="zpix"),
                                                    ft.Text(value="EVOLUÇÃO", color="#7F8C8D", size=10, weight="bold", font_family="zpix"),
                                                ],
                                            ),

                                            ft.Row(
                                                controls=[
                                                ft.Text(value=f"{nivel}", color="#7F8C8D", size=40, weight="bold", font_family="zpix"),

                                                ]
                                            ),
                                        ],
                                    ),
                                    
                                ],
                            ),
                            

                        ],
                    ),


                    ft.Container(
                        height=HEIGHT-730,
                        width=WIDTH-260,
                        top = 400,
                        left=20,
                        bgcolor="#F79F1F",
                        border_radius=30,
                        alignment=ft.alignment.center,
                        padding=ft.padding.only(left=10, top=10, right=10, bottom=10),
                        content=tipo_pokemon,
                    ),

                    ft.Row(
                        left=20,
                        top=485,
                        controls=[
                            ft.Text(
                                value=f"Ele cospe fogo que é quente o suficiente para derreter pedregulhos. Pode causar incêndios florestais soprando chamas:",
                                color="#7F8C8D",
                                size=14,
                                weight="bold",
                                max_lines=4,
                                width=WIDTH-80,
                                text_align="justify",    
                            )
                        ],
                    ),


                    ft.Row(
                        top=590,
                        left=20,
                        right=20,
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        width=WIDTH,
                        controls=[
                            ft.Column(
                                spacing=0,
                                controls=[
                                    ft.Row(
                                        spacing=3,
                                        controls=[
                                            ft.Icon(name=ft.icons.LINE_WEIGHT_SHARP, color='#000000', size=20, opacity=0.4),
                                            ft.Text(value="PESO", color='#000000', size=14, weight='bold', opacity=0.4),
                                        ],
                                    ),
                                    peso_pokemon,
                                ],
                            ),
                            ft.Column(
                                spacing=0,
                                controls=[
                                    ft.Row(
                                        spacing=3,
                                        controls=[
                                            ft.Icon(name=ft.icons.HEIGHT, color='#000000', size=20, opacity=0.4),
                                            ft.Text(value="ALTURA", color='#000000', size=14, weight='bold', opacity=0.4),
                                        ],
                                    ),
                                    ft.Text(value=f"{1.7} m", color='#000000', size=22, weight='bold', opacity=0.6),
                                ],
                            ),
                            ft.Column(
                                spacing=0,
                                controls=[
                                    ft.Row(
                                        spacing=3,
                                        controls=[
                                            ft.Icon(name=ft.icons.BOLT, color='#000000', size=20, opacity=0.4),
                                            ft.Text(value="HABILIDADE", color='#000000', size=14, weight='bold', opacity=0.4),
                                        ],
                                    ),
                                    ft.Text(value=f"Chama", color='#000000', size=22, weight='bold', opacity=0.6),
                                ],
                            ),
                        ],
                    ),


                ],
            ), # fim da Stack
        ), # fim do Container principal


    )




    page.update()

ft.app(target=main, assets_dir="assets")