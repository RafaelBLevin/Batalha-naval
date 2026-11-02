from funcoes import define_posicoes, posiciona_frota, preenche_frota, posicao_valida, faz_jogada, afundados
import random
random.seed(1)
def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto
#exercicio 7
frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}
regras = {
    "porta-aviões": [4, 1],
    "navio-tanque": [3, 2],
    "contratorpedeiro": [2, 3],
    "submarino": [1, 4]
}

for nome in frota:
    tamanho = regras[nome][0]
    quantidade = regras[nome][1]
    contador = 0
    while contador < quantidade:
        valida = False
        while not valida:
            print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))
            if nome == "submarino":
                orientacao = "horizontal"
            else: 
                opcao = int(input("Orientação: "))
                if opcao == 1:
                    orientacao = "vertical"
                else:
                    orientacao = "horizontal"
            if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
                valida = True
            else:
                print("Esta posição não está válida!")
        contador += 1
#exercicio 8 
frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}
tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)

navios = 0 
for nome in frota_oponente:
    navios += len(frota_oponente[nome])

posicoes_acertadas = []

navios_jogador = 0
for nome in frota:
    navios_jogador += len(frota[nome])

posicoes_oponente = []

jogando = True
while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
    posicao_nova = False
    while not posicao_nova:   
        linha_valida = False
        while not linha_valida:
            linha = int(input("Jogador, digite a linha da jogada: "))
            if linha >= 0 and linha <= 9:
                linha_valida = True
            else:
                print("Linha inválida!")
        coluna_valida = False
        while not coluna_valida:
            coluna = int(input("Jogador, digite a coluna da jogada: "))
            if coluna >= 0 and coluna <= 9:
                coluna_valida = True
            else:
                print("Coluna inválida!")
        if [linha, coluna] in posicoes_acertadas:
            print(f"A posição linha {linha} e coluna {coluna} já foi informada anteriormente!")
        else:
            posicao_nova = True
    posicoes_acertadas.append([linha, coluna])
    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)
    if afundados(frota_oponente, tabuleiro_oponente) == navios:
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando = False
    else:
        sorteio = False
        while not sorteio:
            linha_oponente = random.randint(0, 9)
            coluna_oponente = random.randint(0, 9)
            if [linha_oponente, coluna_oponente] not in posicoes_oponente:
                sorteio = True
        posicoes_oponente.append([linha_oponente, coluna_oponente])
        print(f"Seu oponente está atacando a posição linha {linha_oponente} e coluna {coluna_oponente}")
        tabuleiro_jogador = faz_jogada(tabuleiro_jogador, linha_oponente, coluna_oponente)
        if afundados(frota, tabuleiro_jogador) == navios_jogador:
            print("Xi! O oponente derrubou toda a sua frota =(")
            jogando = False
        
           