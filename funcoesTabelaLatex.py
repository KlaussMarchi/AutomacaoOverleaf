def replaceList(string, listaPalavras, listaReplace):
    for c in range(len(listaPalavras)):
        string = string.replace(listaPalavras[c], listaReplace[c])

    return string


def formatarTabela(string=''):
    string = string.replace(',', '.').replace('±', '$\pm$').replace('ϴ', r'$\theta$')

    if '|' in string:
        lista = string.split('|')
    else:
        lista = string.split('\n')

    for c in range(0, len(lista)):
        lista[c] = lista[c].split()
    string = r'\begin{center}' + '\n\t' + r'\begin{tabular}' + '{' + '|c' * len(lista[0]) + '|}' + '\n\t\t' + r'\hline' + '\n'

    for c in range(0, len(lista)):
        string += f"\t\t{' & '.join(lista[c])}" + r'\\' + '\n'
    string += '\t\t' + r'\hline' + '\n\t' + r'\end{tabular}' + '\n' + r'\end{center}' + '\n\n'

    return string


