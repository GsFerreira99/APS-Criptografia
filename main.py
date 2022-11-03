from interface.menu import menu, validar_opcao, get_opcoes, gerar_novas_chaves, limpar
import time



while True:
    menu()
    index = input("\nSelecione uma das opções: ")
    if validar_opcao(index, get_opcoes()) is False:
        print('Informe uma opção válida ex.: 2')
        time.sleep(2)
    else:
        print('Sucesso!')
        get_opcoes(index)['funcao']()
        time.sleep(2)

    limpar()



