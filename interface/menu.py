import os


def get_opcoes(index: str = 'tudo') -> dict:
    dict_opcoes: dict = {
        '1': {
            'texto': 'Gerar Novas Chaves',
            'funcao': gerar_novas_chaves,
        },
        '2': {
            'texto': 'Exportar Chave Pública',
            'funcao': exportar_chave_publica,
        },
        '3': {
            'texto': 'Importar Chave Pública',
            'funcao': importar_chave_publica,
        },
        '4': {
            'texto': 'Criptografar Texto',
            'funcao': criptografar_texto,
        },
        '5': {
            'texto': 'Decriptar Texto',
            'funcao': decriptar_texto,
        },
    }
    return dict_opcoes if index == 'tudo' else dict_opcoes[index]


def limpar() -> None:
    """
    Limpa a Tela
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def menu(msg: str = "BEM VINDO AO SISTEMA DE CRIPTOGRAFIA") -> None:
    print(f"..........::::::::::  {msg}   ::::::::::..........\n")
    for i, dados in get_opcoes().items():
        print(f"{i} - {dados['texto']}")


def validar_opcao(index: str, opcoes: dict) -> float:
    return True if index in opcoes.keys() else False


def gerar_novas_chaves():
    print('Gerar Chave')


def exportar_chave_publica():
    pass


def importar_chave_publica():
    pass


def criptografar_texto():
    pass


def decriptar_texto():
    pass
