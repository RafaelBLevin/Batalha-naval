from funcoes import define_posicoes, preenche_frota, posicao_valida
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
        print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
        valida = False
        while not valida:
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
print(frota)