def replaceList(string, listaPalavras, listaReplace):
    for c in range(len(listaPalavras)):
        string = string.replace(listaPalavras[c], listaReplace[c])

    return string


def formatarEquacao(texto=''):
    lista1 = ['*', r'/', 'º', '^(', '^)', '\seta', '\Seta']
    lista2 = [' \cdot ', r'\frac', r'^\circ', r'\bigg(', r'\bigg)', r'\,\,\rightarrow\,\,', r'\,\,\Rightarrow\,\,']
    texto = replaceList(texto, lista1, lista2)

    return r'\begin{center} ' + f'${texto}$' + r' \end{center}'