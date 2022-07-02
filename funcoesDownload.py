from botcity.core import DesktopBot
import pyautogui, pyperclip
import os, zipfile

# SUBSTITUI TODAS AS STRINGS DA LISTA 1 PELAS STRING CORRESPONDENTES NA LISTA 2
def replaceList(string, listaPalavras, listaReplace):
    for c in range(len(listaPalavras)):
        string = string.replace(listaPalavras[c], listaReplace[c])

    return string

# EXTRAI UM ARQUIVO QUE ESTÁ EM UM ENDEREÇO E MOVE ELE PARA UMA PASTA DESTINO
def extrairZip(endereco, destino):
    with zipfile.ZipFile(endereco, 'r') as arquivoZip:
        arquivoZip.extractall(destino)


# RETORNA O ENDEREÇO DE UM ARQUIVO CASO ELE EXISTA NESTE DIRETÓRIO (LOOP INFINITO ENQUANTO NÃO EXISTIR)
def verificarArquivo(endereco, pedacoNome1, pedacoNome2):
    arquivos = []

    while True:
        for caminho_diretorio, nome_diretorio, nome_arquivo in os.walk(endereco):
            if caminho_diretorio == endereco:
                arquivos.extend(nome_arquivo)

        for arquivo in arquivos:
            if pedacoNome1 in arquivo.lower() or pedacoNome2 in arquivo.lower():
                return endereco + fr'\{arquivo}'


class Bot(DesktopBot):
    def action(self, execution=None):

        # ENTRANDO NO SITE (GOOGLE DRIVE) E ESPERANDO 2000 MILISSEGUNDOS
        self.browse('https://drive.google.com/drive/u/0/folders/1fAcJRYjCP9gO9Je0Yo_56Z0jKgBMp2WO?lfhs=2')
        self.wait(2000)

        # ENCONTRANDO ALGUM SIMBOLO DE IMAGEM
        if not self.find( "imagem", matching=0.97, waiting_time=4000):
            if not self.find( "zip", matching=0.97, waiting_time=4000):
                self.not_found("zip")
        self.click()
        self.wait(1000)

        # SELECIONANDO TODAS AS IMAGENS
        pyautogui.hotkey('ctrl', 'a')
        self.wait(500)

        # APERTANDO COM O BOTAO DIRETO
        self.right_click()
        self.wait(500)

        # ESPERANDO O ARQUIVO BAIXAR E CLICANDO EM DOWNLOADS
        if not self.find( "download", matching=0.97, waiting_time=10000):
            self.not_found("download")
        self.click()
        self.wait(500)

        # CLICANDO EM "SALVAR COMO" (POR TEXTO AO INVES DE IMAGEM)
        if not self.find_text( "Salvar Como", threshold=230, waiting_time=100000):
            self.not_found("Salvar Como")
        self.click()
        
        # CLICANDO NO CAMPO DE ESCREVER O DIRETORIO
        if not self.find( "pasta", matching=0.97, waiting_time=2000):
            if not self.find( "pasta2", matching=0.97, waiting_time=2000):
                self.not_found("pasta2")
        self.click()

        # ESCREVENDO O DIRETORIO E DANDO ENTER
        self.paste(r'C:\Users\march\Downloads')
        self.wait(500)
        self.enter()
        
        if not self.find_text( "SalvarArquivos", threshold=230, waiting_time=10000):   
            self.not_found("SalvarArquivos")
        self.click()
        
        

        # VOLTANDO NOVAMENTE PARA AS IMAGENS DO DRIVE
        if not self.find( "imagem", matching=0.97, waiting_time=4000):
            if not self.find( "zip", matching=0.97, waiting_time=4000):
                self.not_found("zip")
        self.click()
        self.wait(1000)

        # SELECIONANDO TODOS OS ARQUIVOS E DELETANDO
        pyautogui.hotkey('ctrl', 'a')
        self.wait(500)
        self.delete()
        self.enter()

        # FECHANDO A ABA DO NAVEGADOR DEPOIS DE 5 SEGUNDOS
        self.wait(5000)
        pyautogui.hotkey('ctrl', 'w')

        # ENDEREÇO ORIGINAL E DESTINO
        enderecoZip = verificarArquivo(r'C:\Users\march\Downloads', 'drive', 'cam')
        destino = r'C:\Users\march\OneDrive\Documentos\Imagens Latex'

        # EXTRAINDO O ARQUIVO E COLOCANDO NA PASTA DESTINO
        extrairZip(enderecoZip, destino)

        # DELETANDO A PASTA EXTRAIDA E O ARQUIVO ZIP
        os.remove(enderecoZip)

    def not_found(self, label):
        print(f"Element not found: {label}")


def run():
    Bot.main()



















































