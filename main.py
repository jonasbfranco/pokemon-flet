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
            numero_pokebola.value = f"#{numero_pokemon.current}"

            tipo = f"{resultado['types'][0]['type']['name']}"
            tipo_pokemon.value = tipo
            btn_tipo1.bgcolor = (
                "#4592C4" if tipo_pokemon.value == 'water' else
                "#9BCC50" if tipo_pokemon.value == 'grass' else
                "#F79F1F" if tipo_pokemon.value == 'fire' else
                "#729F3F" if tipo_pokemon.value == 'bug' else
                "#A4ACAF" if tipo_pokemon.value == 'normal' else
                "#B97FC9" if tipo_pokemon.value == 'poison' else
                "#51C4E7" if tipo_pokemon.value == 'ice' else
                "#EED535" if tipo_pokemon.value == 'electric' else
                "#AB9842" if tipo_pokemon.value == 'ground' else
                "#FDB9E9" if tipo_pokemon.value == 'fairy' else
                "#D56723" if tipo_pokemon.value == 'fighting' else
                "#F366B9" if tipo_pokemon.value == 'psychic' else
                "#A38C21" if tipo_pokemon.value == 'rock' else
                "#F16E57" if tipo_pokemon.value == 'dragon' else
                "#7B62A3" if tipo_pokemon.value == 'ghost' else
                "#FFFFFF"
            )

            # alterando cor de fundo da imagem do pokemon
            imagem_pokemon.bgcolor = btn_tipo1.bgcolor


            tipo2 = f"{resultado['types'][1]['type']['name']}" if len(resultado['types']) > 1 else ""
            tipo2_pokemon.value = tipo2
            btn_tipo2.bgcolor = (
                "#4592C4" if tipo2_pokemon.value == 'water' else
                "#9BCC50" if tipo2_pokemon.value == 'grass' else
                "#F79F1F" if tipo2_pokemon.value == 'fire' else
                "#729F3F" if tipo2_pokemon.value == 'bug' else
                "#A4ACAF" if tipo2_pokemon.value == 'normal' else
                "#B97FC9" if tipo2_pokemon.value == 'poison' else
                "#51C4E7" if tipo2_pokemon.value == 'ice' else
                "#EED535" if tipo2_pokemon.value == 'electric' else
                "#AB9842" if tipo2_pokemon.value == 'ground' else
                "#FDB9E9" if tipo2_pokemon.value == 'fairy' else
                "#D56723" if tipo2_pokemon.value == 'fighting' else
                "#F366B9" if tipo2_pokemon.value == 'psychic' else
                "#A38C21" if tipo2_pokemon.value == 'rock' else
                "#F16E57" if tipo2_pokemon.value == 'dragon' else
                "#7B62A3" if tipo2_pokemon.value == 'ghost' else
                "#FFFFFF"
            )



            height = f"{resultado['height'] / 10:.1f} m"
            altura_pokemon.value = height

            weight = f"{resultado['weight'] / 10:.1f} Kg".rstrip('0').rstrip('.') if resultado['weight'] % 10 != 0 else f"{resultado['weight'] // 10} Kg"
            peso_pokemon.value = weight

            abilities = f"{resultado['abilities'][0]['ability']['name']}"
            habilidade.value = abilities

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
            numero_pokebola.value = f"#{numero_pokemon.current}"

            tipo = f"{resultado['types'][0]['type']['name']}"
            tipo_pokemon.value = tipo
            btn_tipo1.bgcolor = (
                "#4592C4" if tipo_pokemon.value == 'water' else
                "#9BCC50" if tipo_pokemon.value == 'grass' else
                "#F79F1F" if tipo_pokemon.value == 'fire' else
                "#729F3F" if tipo_pokemon.value == 'bug' else
                "#A4ACAF" if tipo_pokemon.value == 'normal' else
                "#B97FC9" if tipo_pokemon.value == 'poison' else
                "#51C4E7" if tipo_pokemon.value == 'ice' else
                "#EED535" if tipo_pokemon.value == 'electric' else
                "#AB9842" if tipo_pokemon.value == 'ground' else
                "#FDB9E9" if tipo_pokemon.value == 'fairy' else
                "#D56723" if tipo_pokemon.value == 'fighting' else
                "#F366B9" if tipo_pokemon.value == 'psychic' else
                "#A38C21" if tipo_pokemon.value == 'rock' else
                "#F16E57" if tipo_pokemon.value == 'dragon' else
                "#7B62A3" if tipo_pokemon.value == 'ghost' else
                "#FFFFFF"
            )

            # alterando cor de fundo da imagem do pokemon
            imagem_pokemon.bgcolor = btn_tipo1.bgcolor

            tipo2 = f"{resultado['types'][1]['type']['name']}" if len(resultado['types']) > 1 else ""
            tipo2_pokemon.value = tipo2
            btn_tipo2.bgcolor = (
                "#4592C4" if tipo2_pokemon.value == 'water' else
                "#9BCC50" if tipo2_pokemon.value == 'grass' else
                "#F79F1F" if tipo2_pokemon.value == 'fire' else
                "#729F3F" if tipo2_pokemon.value == 'bug' else
                "#A4ACAF" if tipo2_pokemon.value == 'normal' else
                "#B97FC9" if tipo2_pokemon.value == 'poison' else
                "#51C4E7" if tipo2_pokemon.value == 'ice' else
                "#EED535" if tipo2_pokemon.value == 'electric' else
                "#AB9842" if tipo2_pokemon.value == 'ground' else
                "#FDB9E9" if tipo2_pokemon.value == 'fairy' else
                "#D56723" if tipo2_pokemon.value == 'fighting' else
                "#F366B9" if tipo2_pokemon.value == 'psychic' else
                "#A38C21" if tipo2_pokemon.value == 'rock' else
                "#F16E57" if tipo2_pokemon.value == 'dragon' else
                "#7B62A3" if tipo2_pokemon.value == 'ghost' else
                "#FFFFFF"
            )


            height = f"{resultado['height'] / 10:.1f} m"
            altura_pokemon.value = height

            weight = f"{resultado['weight'] / 10:.1f} Kg".rstrip('0').rstrip('.') if resultado['weight'] % 10 != 0 else f"{resultado['weight'] // 10} Kg"
            peso_pokemon.value = weight

            abilities = f"{resultado['abilities'][0]['ability']['name']}"
            habilidade.value = abilities

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
            numero_pokebola.value = f"#{numero_pokemon.current}"

            tipo = f"{resultado['types'][0]['type']['name']}"
            tipo_pokemon.value = tipo
            btn_tipo1.bgcolor = (
                "#4592C4" if tipo_pokemon.value == 'water' else
                "#9BCC50" if tipo_pokemon.value == 'grass' else
                "#F79F1F" if tipo_pokemon.value == 'fire' else
                "#729F3F" if tipo_pokemon.value == 'bug' else
                "#A4ACAF" if tipo_pokemon.value == 'normal' else
                "#B97FC9" if tipo_pokemon.value == 'poison' else
                "#51C4E7" if tipo_pokemon.value == 'ice' else
                "#EED535" if tipo_pokemon.value == 'electric' else
                "#AB9842" if tipo_pokemon.value == 'ground' else
                "#FDB9E9" if tipo_pokemon.value == 'fairy' else
                "#D56723" if tipo_pokemon.value == 'fighting' else
                "#F366B9" if tipo_pokemon.value == 'psychic' else
                "#A38C21" if tipo_pokemon.value == 'rock' else
                "#F16E57" if tipo_pokemon.value == 'dragon' else
                "#7B62A3" if tipo_pokemon.value == 'ghost' else
                "#FFFFFF"
            )

            # alterando cor de fundo da imagem do pokemon
            imagem_pokemon.bgcolor = btn_tipo1.bgcolor

            tipo2 = f"{resultado['types'][1]['type']['name']}" if len(resultado['types']) > 1 else ""
            tipo2_pokemon.value = tipo2
            btn_tipo2.bgcolor = (
                "#4592C4" if tipo2_pokemon.value == 'water' else
                "#9BCC50" if tipo2_pokemon.value == 'grass' else
                "#F79F1F" if tipo2_pokemon.value == 'fire' else
                "#729F3F" if tipo2_pokemon.value == 'bug' else
                "#A4ACAF" if tipo2_pokemon.value == 'normal' else
                "#B97FC9" if tipo2_pokemon.value == 'poison' else
                "#51C4E7" if tipo2_pokemon.value == 'ice' else
                "#EED535" if tipo2_pokemon.value == 'electric' else
                "#AB9842" if tipo2_pokemon.value == 'ground' else
                "#FDB9E9" if tipo2_pokemon.value == 'fairy' else
                "#D56723" if tipo2_pokemon.value == 'fighting' else
                "#F366B9" if tipo2_pokemon.value == 'psychic' else
                "#A38C21" if tipo2_pokemon.value == 'rock' else
                "#F16E57" if tipo2_pokemon.value == 'dragon' else
                "#7B62A3" if tipo2_pokemon.value == 'ghost' else
                "#FFFFFF"
            )



            height = f"{resultado['height'] / 10:.1f} m"
            altura_pokemon.value = height

            weight = f"{resultado['weight'] / 10:.1f} Kg".rstrip('0').rstrip('.') if resultado['weight'] % 10 != 0 else f"{resultado['weight'] // 10} Kg"
            peso_pokemon.value = weight

            abilities = f"{resultado['abilities'][0]['ability']['name']}"
            habilidade.value = abilities

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
            numero_pokebola.value = f"#{numero_pokemon.current}"

            tipo = f"{resultado['types'][0]['type']['name']}"
            tipo_pokemon.value = tipo
            btn_tipo1.bgcolor = (
                "#4592C4" if tipo_pokemon.value == 'water' else
                "#9BCC50" if tipo_pokemon.value == 'grass' else
                "#F79F1F" if tipo_pokemon.value == 'fire' else
                "#729F3F" if tipo_pokemon.value == 'bug' else
                "#A4ACAF" if tipo_pokemon.value == 'normal' else
                "#B97FC9" if tipo_pokemon.value == 'poison' else
                "#51C4E7" if tipo_pokemon.value == 'ice' else
                "#EED535" if tipo_pokemon.value == 'electric' else
                "#AB9842" if tipo_pokemon.value == 'ground' else
                "#FDB9E9" if tipo_pokemon.value == 'fairy' else
                "#D56723" if tipo_pokemon.value == 'fighting' else
                "#F366B9" if tipo_pokemon.value == 'psychic' else
                "#A38C21" if tipo_pokemon.value == 'rock' else
                "#F16E57" if tipo_pokemon.value == 'dragon' else
                "#7B62A3" if tipo_pokemon.value == 'ghost' else
                "#FFFFFF"
            )

            # alterando cor de fundo da imagem do pokemon
            imagem_pokemon.bgcolor = btn_tipo1.bgcolor

            tipo2 = f"{resultado['types'][1]['type']['name']}" if len(resultado['types']) > 1 else ""
            tipo2_pokemon.value = tipo2
            tipo2 = f"{resultado['types'][1]['type']['name']}" if len(resultado['types']) > 1 else ""
            tipo2_pokemon.value = tipo2
            btn_tipo2.bgcolor = (
                "#4592C4" if tipo2_pokemon.value == 'water' else
                "#9BCC50" if tipo2_pokemon.value == 'grass' else
                "#F79F1F" if tipo2_pokemon.value == 'fire' else
                "#729F3F" if tipo2_pokemon.value == 'bug' else
                "#A4ACAF" if tipo2_pokemon.value == 'normal' else
                "#B97FC9" if tipo2_pokemon.value == 'poison' else
                "#51C4E7" if tipo2_pokemon.value == 'ice' else
                "#EED535" if tipo2_pokemon.value == 'electric' else
                "#AB9842" if tipo2_pokemon.value == 'ground' else
                "#FDB9E9" if tipo2_pokemon.value == 'fairy' else
                "#D56723" if tipo2_pokemon.value == 'fighting' else
                "#F366B9" if tipo2_pokemon.value == 'psychic' else
                "#A38C21" if tipo2_pokemon.value == 'rock' else
                "#F16E57" if tipo2_pokemon.value == 'dragon' else
                "#7B62A3" if tipo2_pokemon.value == 'ghost' else
                "#FFFFFF"
            )


            height = f"{resultado['height'] / 10:.1f} m"
            altura_pokemon.value = height

            weight = f"{resultado['weight'] / 10:.1f} Kg".rstrip('0').rstrip('.') if resultado['weight'] % 10 != 0 else f"{resultado['weight'] // 10} Kg"
            peso_pokemon.value = weight

            abilities = f"{resultado['abilities'][0]['ability']['name']}"
            habilidade.value = abilities


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
                size=46, 
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
    tipo2_pokemon = ft.Text(
                value=f"poison", 
                color="#FFFFFF", 
                size=16, 
                weight="bold", 
                font_family="zpix"
            )

    peso_pokemon = ft.Text(
                value=f"{6.9} kg", 
                color='#000000', 
                size=22, 
                weight='bold', 
                opacity=0.6,
            )
    
    altura_pokemon = ft.Text(
                value=f"{0.7} m", 
                color='#000000', 
                size=22, 
                weight='bold', 
                opacity=0.6,
            )

    habilidade = ft.Text(
            value=f"overgrow", 
            color='#000000', 
            size=22, 
            weight='bold', 
            opacity=0.6
        )
    
    numero_pokebola = ft.Text(
            value=f"#1", 
            color="#7F8C8D", 
            size=40, 
            weight="bold", 
            font_family="zpix"
        )

    btn_tipo1 = ft.Container(
            height=HEIGHT-730,
            width=WIDTH-260,
            top = 450,
            left=20,
            bgcolor="#9BCC50",
            border_radius=30,
            alignment=ft.alignment.center,
            padding=ft.padding.only(left=10, top=10, right=10, bottom=10),
            content=tipo_pokemon,
        )

    btn_tipo2 = ft.Container(
            height=HEIGHT-730,
            width=WIDTH-260,
            top = 450,
            right=20,
            bgcolor="#B97FC9",
            border_radius=30,
            alignment=ft.alignment.center,
            padding=ft.padding.only(left=10, top=10, right=10, bottom=10),
            content=tipo2_pokemon,
        )


    imagem_pokemon = ft.Container(
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
            bgcolor="#9BCC50",
            padding=10,
            border_radius=35,
            width=WIDTH,
            height=HEIGHT - 500,
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
                    
                    imagem_pokemon,

                    
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
                        top=310,
                        left=20,
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
                                        ],
                                    ),   
                                ],
                            ),
                            

                        ],
                    ),

                    ft.Column(
                        spacing=0,
                        top=370,
                        right=20,
                        alignment=ft.CrossAxisAlignment.START,
                        controls=[
                            ft.Row(
                                height=46,
                                spacing=10,
                                controls=[
                                    ft.Column(
                                        spacing=0,
                                        alignment=ft.MainAxisAlignment.END,
                                        controls=[
                                            ft.Text(value=f"Número", color="#7F8C8D", size=14, weight="bold", font_family="zpix"),
                                            ft.Text(value="POKEBOLA", color="#7F8C8D", size=16, weight="bold", font_family="zpix"),
                                        ],
                                    ),

                                    ft.Row(
                                        controls=[
                                            numero_pokebola,
                                        ]
                                    ),
                                ],
                            ),
                        ],
                    ),


                    btn_tipo1,
                    btn_tipo2,

                    
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
                                    altura_pokemon,
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
                                    habilidade,
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