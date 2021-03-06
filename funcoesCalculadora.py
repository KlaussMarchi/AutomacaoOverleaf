# IMPORTANDO AS BIBLIOTECAS
import pyperclip, sys, os
import sympy as sp                           # pip install sympy
import antlr4
from sympy.parsing.latex import parse_latex  # pip install antlr4-python3-runtime
import numpy as np

lista1 = np.array([
    ' ', '$', '\int', 'int', '\cos', 'cos', '\sin', 'sen', 'sin', r'\tan', 'tan',
    'r)', 'ang(', 'rad(', '**', 'd/dx',
    '\pi', '\e', 'pi', 'e', '\ln', 'ln'
])

lista2 = np.array([
    '', '', 'int', '\int', 'cos', '\cos', 'sin', 'sin', '\sin', 'tan', r'\tan',
    ' * (3.14159 / 180))', '(180 / 3.14159) * (', '(3.14159/180) * (',
    '^', r'\frac{d}{dx}',
    'pi', 'e', '3.14159', '2.71828', 'ln', '\ln'
])

# SUBSTITUI TODAS AS STRINGS DA LISTA 1 PELAS STRING CORRESPONDENTES NA LISTA 2
def replaceList(string, listaPalavras, listaReplace):
    for c in range(len(listaPalavras)):
        string = string.replace(listaPalavras[c], listaReplace[c])

    return string

def blockPrint():
    sys.stdout = open(os.devnull, 'w')

def enablePrint():
    sys.stdout = sys.__stdout__

def strFloat(valor, casasDecimais):
    try:
        valor = float(valor)
        valor = round(valor, casasDecimais)
    except:
        valor = sp.sympify(valor)
    return str(valor).replace('**', '^').replace('*', '').replace('I', '*I')

# RECEBE UMA STRING COM UMA EXPRESSÃO MATEMÁTICA EM CÓDIGO LATEX E A RESOLVE
def solveExpression(expressaoLatex):
    expressaoLatex = replaceList(expressaoLatex, lista1, lista2)

    blockPrint()
    equacao = parse_latex(expressaoLatex)
    enablePrint()

    if type(equacao) != sp.core.relational.Equality:
        solucoes = equacao.doit()
        return strFloat(solucoes, 3)

    solucoes = sp.solve(equacao)
    for c, sol in enumerate(solucoes):
        sol = sp.N(sol)
        solucoes[c] = strFloat(sol, 3)

    return ', '.join(solucoes)
