import flet as ft
from models import Produto
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

CONN = 'sqlite:///projeto2.db'

engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

lista_produtos = ft.ListView(expand=True)

def main(page: ft.Page):

    page.title = 'Cadastro App'

    def cadastrar(e):
        try:
            novo_produto = Produto(titulo=produto.value, preco=preco.value)
            session.add(novo_produto)
            session.commit()
            lista_produtos.controls.append(ft.Container(
                    ft.Text(produto.value),
                    bgcolor=ft.Colors.BLACK_12,
                    padding=15,
                    margin=3,
                    border_radius=10
                ))
            txt_erro.visible = False
            txt_acerto.visible = True
        except:
            txt_erro.visible = True
            txt_acerto.visible = False
        page.update()
        print('Produto salvo com sucesso!')

    txt_erro = ft.Container(ft.Text('Erro ao salvar o produto!'), visible=False, bgcolor=ft.Colors.RED, padding=10, alignment=ft.Alignment.CENTER)
    txt_acerto = ft.Container(ft.Text('Produto salvo com sucesso!'), visible=False, bgcolor=ft.Colors.GREEN, padding=10, alignment=ft.Alignment.CENTER)


    txt_titulo = ft.Text('Titulo do produto: ')
    produto = ft.TextField(label='Digite o nome do produto..', text_align=ft.TextAlign.LEFT)
    txt_preco = ft.Text('Preço do produto: ')
    preco = ft.TextField(value='0', label='Digite o preço do produto..', text_align=ft.TextAlign.LEFT)
    btn_produto = ft.ElevatedButton('Cadastrar', on_click=cadastrar)

    page.add(
        txt_acerto,
        txt_erro,
        txt_titulo,
        produto,
        txt_preco,
        preco,
        btn_produto
    )

    for p in session.query(Produto).all():
        lista_produtos.controls.append(ft.Container(
                ft.Text(p.titulo),
                bgcolor=ft.Colors.BLACK_12,
                padding=15,
                margin=3,
                border_radius=10
            )
        )

    page.add(
        lista_produtos,
    )

ft.app(target=main) 

# Inicializando um app com essa ferramenta ft.app
# O target vai ser passado como parametro qual a função python que vai ser responsavel por definir aquela interface
# Então esta sendo passado o seguint: A interface que vou rodar, vai se uma interface chamada main