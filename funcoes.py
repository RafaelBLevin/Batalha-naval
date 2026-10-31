def define_posicoes(linha,coluna,orientacao,tamanho):
    posicoes = []
    i = 0
    if orientacao == "horizontal":
        while i  < len(tamanho):
            linha_atual = linha
            coluna_atual = coluna + i
            posicoes.append([linha_atual,coluna_atual])
            i += 1
    elif orientacao == "vertical":
        while i < len(tamanho):
            linha_atual = linha + i
            coluna_atual = coluna
            posicoes.append([linha_atual,coluna_atual])
            i += 1
    return posicoes
