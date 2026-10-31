#exercicio 1
def define_posicoes(linha,coluna,orientacao,tamanho):
    posicoes = []
    i = 0
    if orientacao == "horizontal":
        while i  < tamanho:
            linha_atual = linha
            coluna_atual = coluna + i
            posicoes.append([linha_atual,coluna_atual])
            i += 1
    elif orientacao == "vertical":
        while i < tamanho:
            linha_atual = linha + i
            coluna_atual = coluna
            posicoes.append([linha_atual,coluna_atual])
            i += 1
    return posicoes

#exercicio 2
def preenche_frota(frota, navio, linha, coluna, orientacao,tamanho):
    posicoes = define_posicoes(linha,coluna,orientacao,tamanho)
    if navio not in frota:
        frota[navio] = []
    frota[navio].append(posicoes)
    return frota

