import re

def le_assinatura():
    #A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    #A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    #A funcao recebe um texto e devolve uma lista das sentencas dentro do texto
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    #A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    #A funcao recebe uma frase e devolve uma lista das palavras dentro da frase
    return frase.split()

def n_palavras_unicas(lista_palavras):
    #Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    #Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    #IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas
    i = 0
    soma = 0
    list_das_diferencas = []
    while i <= 5:
        valor = as_a[i] - as_b[i]

        if valor < 0:
            list_das_diferencas.append(valor* -1)
        else:
            list_das_diferencas.append(valor)

        i += 1

    for k in list_das_diferencas:
        soma += k

    similiridade = soma / 6

    return similiridade

def calcula_assinatura(texto):
    #IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.
    lista_plvr = []
    lista_fras = []
    lista_sent = separa_sentencas(texto)
    total_caraceteres = 0
    total_caract_frs = 0
    total_caract_sent = 0
    for sent in lista_sent:
        frases2 = separa_frases(sent)
        lista_fras.extend(frases2)

    for fras in lista_fras:
        palavras2 = separa_palavras(fras)
        lista_plvr.extend(palavras2)

    for i in lista_plvr:
        x = len(i)
        total_caraceteres += x

    for a in lista_sent:
        total_caract_sent += len(a)

    for k in lista_fras:
        total_caract_frs += len(k)

    wal_texto = total_caraceteres / len(lista_plvr)
    ttr_texto = n_palavras_diferentes(lista_plvr) / len(lista_plvr)
    hlr_texto = n_palavras_unicas(lista_plvr) / len(lista_plvr)
    sal_texto = total_caract_sent / len(lista_sent)
    sac_texto = len(lista_fras) / len(lista_sent)
    pal_texto = total_caract_frs / len(lista_fras)

    return [wal_texto, ttr_texto, hlr_texto, sal_texto, sac_texto, pal_texto]

def avalia_textos(textos, ass_cp):
    #IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH
    lista_assinaturas = []
    lista_similiridades = []
    for i in textos:
        as_b = calcula_assinatura(i)
        lista_assinaturas.append(as_b)

    for k in lista_assinaturas:
        valor_similar = compara_assinatura(ass_cp,k)
        lista_similiridades.append(valor_similar)

    return lista_similiridades.index(min(lista_similiridades)) + 1


ass_a = le_assinatura()
lista_textos = le_textos()

print('O autor do texto', avalia_textos(lista_textos, ass_a),'está infectado com COH-PIAH')




