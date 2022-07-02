import os, pyperclip
from PIL import ImageTk, Image
from botcity.core import DesktopBot
import pyautogui


# RETORNA O NOME DE TODOS OS ARQUIVOS EM UMA PASTA
def obterArquivos(endereco):
    arquivos = []
    for caminho_diretorio, nome_diretorio, nome_arquivo in os.walk(endereco):
        if caminho_diretorio == endereco:
            arquivos.extend(nome_arquivo)

    return arquivos


# RETORNA O ENDEREÇO DE TODOS OS ARQUIVOS EM UMA PASTA
def obterEnderecos(endereco):
    listaArquivos = obterArquivos(endereco)
    enderecos = []

    for arquivo in listaArquivos:
        enderecoCompleto = endereco + fr'\{arquivo}'
        enderecos.append(enderecoCompleto)

    return enderecos


def ordenaArquivosNome(endereco):
    arquivos = obterArquivos(endereco)
    arquivos.sort()
    return arquivos


def ordenarArquivosData(endereco):
    arquivos = obterArquivos(endereco)
    enderecos = obterEnderecos(endereco)

    lista = []
    for c in range(0, len(enderecos)):
        enderecoCompleto = enderecos[c]
        data = os.path.getctime(enderecoCompleto)  # PEGANDO DATA DE CRIAÇÃO DO ARQUIVO
        nome = arquivos[c]
        lista.append([nome, data])                 # ADICIONANDO O NOME JUNTO À DATA DE CRIAÇÃO [NOME, DATA]

    def segundo_valor(item):
        return item[1]                             # ORGANIZANDO PELA DATA

    lista.sort(key=segundo_valor)

    nomeArquivos = []
    for arquivo in lista:
        nomeArquivos.append(arquivo[0])            # SOMENTE O NOME DO ARQUIVO

    return nomeArquivos


def deletarArquivos(endereco):
    enderecos = obterEnderecos(endereco)
    for c in range(len(enderecos)):
        os.remove(enderecos[c])


def organizarArquivos(endereco, ordenarData=False):
    if ordenarData:
        arquivos = ordenarArquivosData(endereco)
    else:
        arquivos = ordenaArquivosNome(endereco)

    for c in range(len(arquivos)):
        arquivos[c] = endereco + fr'\{arquivos[c]}'

    return arquivos


def nomeArquivo(enderecoImagem):
    return os.path.basename(enderecoImagem)


def centralizarImagemLatex(enderecoImagem, pasta, tamanho):
    arquivo = nomeArquivo(enderecoImagem)

    if pasta.strip() != '':
        pasta = fr'{pasta}/'

    string = r'\begin{center}\includegraphics' + f'[width={tamanho}cm]' + '{' + pasta + arquivo + r'}\end{center}'
    pyperclip.copy(string)


def processarImagem(endereco, tamanho):
    img = Image.open(endereco)
    img = img.resize(tamanho)
    return ImageTk.PhotoImage(img)


class BotLatex(DesktopBot):
    def action(self, execution=None):
        # ENTRANDO NO SITE (LATEX) E ESPERANDO 2000 MILISSEGUNDOS
        self.browse('https://google.com')
        self.wait(1000)

        pyautogui.hotkey('ctrl', 'w')
        self.wait(1000)

        if not self.find("latex", matching=0.97, waiting_time=10000):
            self.not_found("latex")
        self.click()
        self.wait(200)

        if not self.find("pastaImagens", matching=0.97, waiting_time=2000):
            if not self.find("imagens2", matching=0.97, waiting_time=2000):
                self.not_found("imagens2")
        self.click()
        self.wait(200)

        if not self.find("addImagem", matching=0.97, waiting_time=10000):
            self.not_found("addImagem")
        self.click()
        self.wait(200)

        if not self.find("btnUpload", matching=0.97, waiting_time=10000):
            self.not_found("btnUpload")
        self.click()

        if not self.find("selectImagens", matching=0.97, waiting_time=10000):
            self.not_found("selectImagens")
        self.click()

        # CLICANDO NO CAMPO DE ESCREVER O DIRETORIO
        if not self.find("pasta", matching=0.97, waiting_time=2000):
            if not self.find("pasta2", matching=0.97, waiting_time=2000):
                self.not_found("pasta2")
        self.click()

        # ESCREVENDO O DIRETORIO E DANDO ENTER
        self.paste(r'C:\Users\march\OneDrive\Documentos\Imagens Latex')
        self.enter()

        if not self.find("abrirCancelar", matching=0.97, waiting_time=10000):
            self.not_found("abrirCancelar")
        self.move()
        self.wait(400)

        x = self.get_last_x()
        y = self.get_last_y()

        self.click_at(x, y - 100)

        pyautogui.hotkey('ctrl', 'a')
        self.wait(200)
        self.enter()

        if self.find("ovewrite", matching=0.97, waiting_time=2000):
            self.click()

        if not self.find("pronto", matching=0.97, waiting_time=60000):
            self.not_found("pronto")

    def not_found(self, label):
        print(f"Element not found: {label}")


def botUpload():
    BotLatex.main()