import tkinter
import time
import keyboard


def combo_Existe(combo_custom):
    try:
        a = open(combo_custom, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_Combo(combo_custom):
    a = open(combo_custom, 'wt+')
    a.close


def ler_Combo(combo_custom):
    a = open(combo_custom, 'rt')
    for linha in a:
        key(linha.rstrip())


def combo_Besta_Demon():
    time.sleep(0.05)
    key('r'), key('d'), key('q'), key('q'),
    key('q'), key('w'), key('f'), key('tab')
    time.sleep(0.05)


def combo_Besta_Caerleon():
    time.sleep(0.05)
    key('r'), key('d'), key('e'), key('e'), key('q'), key('q'), key('q'),
    key('w'), key('f'), key('tab')
    time.sleep(0.05)


def combo_Frost():
    time.sleep(0.05)
    key('q')
    time.sleep(0.05)


def combo_Frost_Completo():
    time.sleep(0.05)
    key('w'), key('r'), key('d'), key('e'), key('e'), key('q'), key('q'),
    key('q'), key('q'), key('q'), key('f')
    time.sleep(0.05)


if not combo_Existe('custom.txt'):
    time.sleep(0.05)
    criar_Combo('custom.txt')
    time.sleep(0.05)


def selecionar_Opcao():
    so = varopcao.get()
    chave = tecla.get()

    if so == '1':
        keyboard.add_hotkey(chave, lambda: combo_Besta_Demon())
        opcao1["fg"] = "#DAA520"
    if so == '2':
        keyboard.add_hotkey(chave, lambda: combo_Besta_Caerleon())
        opcao2["fg"] = "#DAA520"
    if so == '3':
        keyboard.add_hotkey(chave, lambda: combo_Frost())
        opcao3["fg"] = "#DAA520"
    if so == '4':
        keyboard.add_hotkey(chave, lambda: combo_Frost_Completo())
        opcao4["fg"] = "#DAA520"
    if so == '5':
        keyboard.add_hotkey(chave, lambda: ler_Combo('custom.txt'))
        opcao5["fg"] = "#DAA520"


def limpar_Tecla():
    keyboard.unhook_all_hotkeys()
    opcao1["fg"] = "#000000"
    opcao2["fg"] = "#000000"
    opcao3["fg"] = "#000000"
    opcao4["fg"] = "#000000"
    opcao5["fg"] = "#000000"
    tecla.delete(0, tkinter.constants.END)
    tecla.insert(0, "")


# Configurações principais do programa

janela = tkinter.Tk()
janela.title('MA v2.7')
# janela.iconbitmap('icone.ico')
janela.geometry('250x350')
janela.resizable(False, False)

key = keyboard.press_and_release

lista = ['XBOW (capa demoníaca)',
         'XBOW (capa de caerleon)',
         'FROST (somente tecla "Q")',
         'FROST (combo completo)',
         'CUSTOM (editar arquivo "custom.txt")',
         ]

varopcao = tkinter.StringVar()

menu = tkinter.Label(janela, text='Escolha uma das opções abaixo:')
menu.pack(pady=10)

opcao1 = tkinter.Radiobutton(janela, text=(
    lista[0]), value='1', variable=varopcao)
opcao1.pack(pady=2)

opcao2 = tkinter.Radiobutton(janela, text=(
    lista[1]), value='2', variable=varopcao)
opcao2.pack(pady=2)

opcao3 = tkinter.Radiobutton(janela, text=(
    lista[2]), value='3', variable=varopcao)
opcao3.pack(pady=2)

opcao4 = tkinter.Radiobutton(janela, text=(
    lista[3]), value='4', variable=varopcao)
opcao4.pack(pady=2)

opcao5 = tkinter.Radiobutton(janela, text=(
    lista[4]), value='5', variable=varopcao)
opcao5.pack(pady=2)

tecla_Info = tkinter.Label(
    janela, text='Qual tecla deseja usar?')
tecla_Info.pack(pady=5)

tecla = tkinter.Entry(janela)
tecla.pack(pady=5)

start = tkinter.Button(janela, text=(
    'Iniciar o macro'), command=selecionar_Opcao, bg='#00FF00')
start.pack(pady=10)

start = tkinter.Button(janela, text=(
    'Parar Macro'), command=limpar_Tecla, bg='#FF0000')
start.pack(pady=10)

janela.mainloop()
