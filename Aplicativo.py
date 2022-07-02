# CHAMANDO AS SUB FUNÇÕES DE CADA JANELA
from funcoesDownload import *
from funcoesEquacaoLatex import *
from funcoesTabelaLatex import *
from funcoesUpload import *
from funcoesCalculadora import *

# IMPORTANDO AS BIBLIOTECAS
from tkinter import *
import pyperclip

# ESCONDENDO O CONSOLE
def hideTerminal():
    import win32gui, win32con
    the_program_to_hide = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)

# VOLTANDO AO MENU PRINCIPAL
def voltar(root):
    root.destroy()
    MenuPrincipal()


# CONFIGURANDO AS PROPRIEDADES DE UMA JANELA TKINTER
def ConfigurarJanela(titulo, nLinhas, nColunas, width, height):
    root = Tk()
    root.title(titulo)

    # CENTRALIZANDO A JANELA NO MEIO DA TELA DO PC
    screenWidth = root.winfo_screenwidth()
    screenHeignt = root.winfo_screenheight()

    x = (screenWidth/2) - (width/2)
    y = (screenHeignt/2) - (height/2)

    root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

    # PERMITIR QUE O USUÁRIO COLOQUE EM TELA CHEIA E AJUSTE
    root.resizable(True, True)

    # CONFIGURANDO AS LINHAS E COLUNAS PARA ESTICAR JUNTO COM A JANELA (USAR STICKY)
    for c in range(0, nLinhas):
        root.rowconfigure(c, weight=1)
    for c in range(0, nColunas):
        root.columnconfigure(c, weight=1)
    return root


def EquacaoLatex(root):
    root.destroy()
    root = ConfigurarJanela('Equação', 3, 3, width=600, height=220)

    lblEquacao = Label(root, text='Digite Sua Equação', font=('Arial', 16))
    lblEquacao.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

    lblAux = Label(root, text='')
    lblAux.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky='nsew')

    caixaTexto = Entry(root, width=10, borderwidth=3, font=('Arial', 16), justify=CENTER)
    caixaTexto.grid(row=1, column=0, columnspan=3, padx=10, pady=10, ipady=20, sticky='nsew')

    btnVoltar = Button(root, text='Voltar', font=('Arial', 12), command=lambda: voltar(root))
    btnVoltar.grid(row=0, column=0, padx=10, sticky='nsew')

    quadro = LabelFrame(root, text='Resultado', padx=50, pady=10)
    quadro.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky='nsew')

    lblResultado = Label(quadro, text='', font=('Arial', 10))
    lblResultado.pack(padx=10, pady=10, anchor=CENTER)

    def action(event):
        texto = formatarEquacao(caixaTexto.get())

        pyperclip.copy(texto)
        caixaTexto.delete(0, END)

        lblResultado['text'] = texto

    root.bind("<Return>", action)
    root.mainloop()


def ConverterTabela(root):
    root.destroy()
    root = ConfigurarJanela('Excel para Latex', 3, 3, width=600, height=300)

    lblCole = Label(root, text='Cole Aqui Sua Tabela (ou separe com "|")', font=('Arial', 14))
    lblCole.grid(row=0, column=2, padx=5, pady=5, sticky='nsew')

    btnVoltar = Button(root, text='voltar', font=('Arial', 12), command=lambda: voltar(root))
    btnVoltar.grid(row=0, column=0, padx=5, sticky='nsew')

    CaixaTexto = Entry(root, font=('Arial', 16), width=40)
    CaixaTexto.grid(row=1, column=0, columnspan=3, padx=5, pady=5, ipady=12, sticky='nsew')

    def Converter(event=0):
        string = formatarTabela(CaixaTexto.get())

        lblTabela = Label(root, text=string)
        lblTabela.grid(row=3, column=0, columnspan=3, sticky='nsew')

        CaixaTexto.delete(0, END)
        pyperclip.copy(string)

    btnConcluido = Button(root, text='Concluído', width=60, command=Converter)
    btnConcluido.grid(row=2, column=0, columnspan=3, pady=10, sticky='nsew')

    root.bind("<Return>", Converter)
    root.mainloop()


def ModeloImagem(root):
    root.destroy()
    root = ConfigurarJanela("Imagem", 1, 2, width=400, height=150)

    def copiar(event=0):
        valor = str(tam.get()).replace(',', '.')
        tam.delete(0, END)

        lblConcluido['text'] = 'CONCLUÍDO!'
        pyperclip.copy(r'\begin{center}  ' + rf'\includegraphics[width={valor}cm]' + '{}' + '  \end{center}')

    lblTam = Label(root, text='TAMANHO: ', font=('Arial', 15))
    lblTam.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')

    btnVoltar = Button(root, text='voltar', font=('Arial', 15), command=lambda: voltar(root))
    btnVoltar.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

    tam = Entry(root, font=('Arial', 15), justify=CENTER, width=10)
    tam.grid(row=0, column=2, padx=5, pady=5, sticky='nsew')
    root.bind('<Return>', copiar)

    lblConcluido = Label(root, text='', font=('Arial', 15), fg='blue', pady=15)
    lblConcluido.grid(row=1, column=0, padx=5, pady=5, columnspan=3, sticky='nsew')


def Upload(root):
    root.destroy()
    root = ConfigurarJanela("UPLOAD", 2, 2, width=490, height=200)
    pyautogui.PAUSE = 0.3

    btnVoltar = Button(root, text='voltar', font=('Arial', 15), command=lambda: voltar(root))
    btnVoltar.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

    lblImagem = Label(root, text='Tamanho da Imagem: ', font=('Arial', 15))
    lblImagem.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')

    tam = Entry(root, font=('Arial', 15), justify=CENTER, width=10)
    tam.grid(row=0, column=2, padx=5, pady=5, sticky='nsew')
    tam.insert(0, '20')

    lblPasta = Label(root, text='Nome da Pasta:', font=('Arial', 15))
    lblPasta.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')

    pasta = Entry(root, font=('Arial', 15), justify=CENTER, width=10)
    pasta.grid(row=1, column=1, columnspan=2, padx=5, pady=5, sticky='nsew')

    pasta.insert(0, 'imagens')

    ordenarData = BooleanVar()
    ordenarData.set(False)
    opcaoData = Checkbutton(root, text='Ordenar por data de criação', variable=ordenarData, anchor='w', width=100)
    opcaoData.grid(row=2, column=0, padx=5, pady=5, columnspan=2)

    def iniciar(event):
        showImages(root, tam.get(), pasta.get(), ordenarData.get())

    def runBot():
        botUpload()
        iniciar(0)

    btnImagens = Button(root, text='CARREGAR IMAGENS', font=('Arial', 15), padx=5, pady=5, command=lambda: iniciar(0))
    btnImagens.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky='nsew')

    btnUpload = Button(root, text='UPLOAD', font=('Arial', 15), padx=5, pady=5, command=lambda: runBot())
    btnUpload.grid(row=3, column=2, columnspan=3, padx=5, pady=5, sticky='nsew')

    root.bind("<Return>", iniciar)
    root.mainloop()


def showImages(root, tam, pasta, ordenarData):
    root.destroy()
    root = ConfigurarJanela("UPLOAD", 4, 3, width=600, height=450)

    endereco = r'C:\Users\march\OneDrive\Documentos\Imagens LaTex'
    enderecoImagens = organizarArquivos(endereco, ordenarData) # ENDEREÇO DAS IMAGENS

    nomesImagens = []
    listaImagens = []

    for c in range(len(enderecoImagens)):
        nome = nomeArquivo(enderecoImagens[c])
        nomesImagens.append(nome)

        img = processarImagem(enderecoImagens[c], (534, 316))
        listaImagens.append(img)

    btnVoltar = Button(root, text='voltar', font=('Arial', 15), command=lambda: voltar(root))
    btnVoltar.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

    lblImagem = Label(root, text=nomesImagens[0], font=('Arial', 13))
    lblImagem.grid(row=0, column=1, padx=5, pady=5, sticky='nsew', columnspan=2)

    myLabel = Label(image=listaImagens[0])
    myLabel.grid(row=1, column=0, columnspan=3)

    centralizarImagemLatex(enderecoImagens[0], pasta, tam)

    def carregarImagem(index):
        # FAZENDO UMA LIGAÇÃO COM AS VARIÁVEIS DE FORA DA FUNÇÃO
        nonlocal myLabel
        nonlocal lblImagem
        nonlocal bProximo
        nonlocal bAnterior
        nonlocal pasta
        nonlocal tam

        # RETIRANDO A IMAGEM QUE ESTAVA LÁ
        myLabel.grid_forget()
        lblImagem.grid_forget()

        myLabel = Label(image=listaImagens[index])
        myLabel.grid(row=1, column=0, columnspan=3)  # OCUPA 3 COLUNAS

        lblImagem = Label(root, text=nomesImagens[index], font=('Arial', 13))
        lblImagem.grid(row=0, column=1, padx=5, pady=5, sticky='nsew', columnspan=2)

        # O PRÓXIMO BOTÃO APONTA PARA A PRÓXIMA POSIÇÃO, O INDEX AUMENTA EM 1
        bProximo = Button(text='>>', font=15, command=lambda: carregarImagem(index + 1))
        bProximo.grid(row=2, column=2)

        # O BOTÃO ANTERIOR APONTA PARA A POSIÇÃO ANTERIOR, O INDEX DIMINUI EM 1
        bAnterior = Button(text='<<', font=15, command=lambda: carregarImagem(index - 1))
        bAnterior.grid(row=2, column=0)

        def action(event):
            if index != len(listaImagens) - 1:
                carregarImagem(index + 1)

        root.bind("<Return>", action)

        # SE FOR A ÚLTIMA POSIÇÃO DA LISTA, DESATIVE O PRÓXIMO BOTÃO
        if index == len(listaImagens) - 1:
            bProximo = Button(text='>>', font=15, state=DISABLED)
            bProximo.grid(row=2, column=2)

        # SE FOR O PRIMEIRO DA LISTA, DESATIVE O BOTÃO ANTERIOR
        if index == 0:
            bAnterior = Button(text='<<', font=15, state=DISABLED)
            bAnterior.grid(row=2, column=0)

        # IMPRIMINDO A POSIÇÃO NO APP
        bPos = Label(text=f'{index + 1} de {len(listaImagens)}', relief=SUNKEN, anchor=W)
        bPos.grid(row=3, column=0, pady=10, columnspan=3, sticky=W + E)

        # COPIANDO A ESTRUTURA CENTRALIZADA PARA A ÁREA DE TRANSFERÊNCIA
        centralizarImagemLatex(enderecoImagens[index], pasta, tam)

    bAnterior = Button(text='<<', font=15, state=DISABLED)
    bAnterior.grid(row=2, column=0)

    bProximo = Button(text='>>', font=15, command=lambda: carregarImagem(1))
    bProximo.grid(row=2, column=2)

    if len(nomesImagens) == 1:
        bProximo['state'] = DISABLED

    bPos = Label(text=f'1 de {len(listaImagens)}', relief=SUNKEN, anchor=E)
    bPos.grid(row=3, column=0, pady=10, columnspan=3, sticky=W + E)

    def apagarImagens(endereco):
        deletarArquivos(endereco)
        voltar(root)

    def action(event):
        if len(nomesImagens) != 1:
            carregarImagem(1)

    btnApagar = Button(text='APAGAR IMAGENS', font=15, command=lambda: apagarImagens(endereco))
    btnApagar.grid(row=2, column=1)

    root.bind("<Return>", action)
    root.mainloop()


def Download(root):
    root.destroy()
    root = ConfigurarJanela("UPLOAD", 2, 2, width=400, height=200)

    btnVoltar = Button(root, text='voltar', font=('Arial', 15), command=lambda: voltar(root))
    btnVoltar.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

    frame = LabelFrame(root, padx=5, pady=5)
    frame.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')

    lblIntro = Label(frame, text='Download do Drive', font=('Arial', 15))
    lblIntro.pack(padx=5, pady=5, anchor=CENTER)

    def clicked():
        run()
        voltar(root)

    btnDownload = Button(root, text='INICIAR', padx=5, pady=5, command=clicked)
    btnDownload.grid(row=1, column=0, padx=5, pady=5, sticky='nsew', columnspan=2)

    root.mainloop()


def Calculadora(root):
    root.destroy()
    root = ConfigurarJanela('Calculadora Avançada', 3, 3, width=600, height=250)
    solveExpression('2+2')

    btnVoltar = Button(root, text='voltar', font=('Arial', 15), command=lambda: voltar(root))
    btnVoltar.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

    lblEquacao = Label(root, text='Digite Sua Equação', font=('Arial', 16))
    lblEquacao.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

    lblAux = Label(root, text='')
    lblAux.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky='nsew')

    caixaTexto = Entry(root, width=10, borderwidth=3, font=('Arial', 16), justify=CENTER)
    caixaTexto.grid(row=1, column=0, columnspan=3, padx=10, pady=10, ipady=20, sticky='nsew')

    quadro = LabelFrame(root, text='Resultado', padx=20, pady=10)
    quadro.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky='nsew')

    lblResultado = Label(quadro, text='', font=('Arial', 14))
    lblResultado.pack(padx=10, pady=10, anchor=CENTER)

    def action(event):
        texto = solveExpression(caixaTexto.get())

        pyperclip.copy(texto)
        caixaTexto.delete(0, END)

        lblResultado['text'] = texto

    root.bind("<Return>", action)
    root.mainloop()


def MenuPrincipal():
    root = ConfigurarJanela('Latex Automático', 3, 2, width=350, height=250)

    quadro = LabelFrame(root, text='Latex Automático', padx=50, pady=10)
    quadro.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky='nsew')

    lblMenu = Label(quadro, text='MENU PRINCIPAL', font=('Arial', 16))
    lblMenu.pack(padx=10, pady=10, anchor=CENTER)

    btnEquacao = Button(root, text='Equação Centralizada', padx=5, pady=5, command=lambda: EquacaoLatex(root))
    btnEquacao.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')

    btnConverter = Button(root, text='Converter Tabela Excel', padx=5, pady=5, command=lambda: ConverterTabela(root))
    btnConverter.grid(row=1, column=1, padx=5, pady=5, sticky='nsew')

    btnImagem = Button(root, text='Modelo Imagem', padx=18, pady=5, command=lambda: ModeloImagem(root))
    btnImagem.grid(row=2, column=0, padx=5, pady=5, sticky='nsew')

    btnUpload = Button(root, text='Upload Imagens', padx=21, pady=5, command=lambda: Upload(root))
    btnUpload.grid(row=2, column=1, padx=5, pady=5, sticky='nsew')

    btnDownload = Button(root, text='Download Imagens', padx=21, pady=7, command=lambda: Download(root))
    btnDownload.grid(row=3, column=0, padx=5, pady=5, sticky='nsew')

    btnCalc = Button(root, text='Calculadora', padx=21, pady=7, command=lambda: Calculadora(root))
    btnCalc.grid(row=3, column=1, padx=5, pady=5, sticky='nsew')

    root.mainloop()


# INICIALIZANDO O PROGRAMA NA JANELA DO MENU PRINCIPAL
hideTerminal()
MenuPrincipal()