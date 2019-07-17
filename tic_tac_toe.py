def mostra_tabuleiro(**posicoes):
    print('       |       |       ')
    print('  {}    |   {}   |   {}   '.format(posicoes['pos1'], posicoes['pos2'], posicoes['pos3']))
    print('       |       |       ')
    print('-------|-------|-------')
    print('       |       |       ')
    print('  {}    |   {}   |   {}   '.format(posicoes['pos4'], posicoes['pos5'], posicoes['pos6']))
    print('       |       |       ')
    print('-------|-------|-------')
    print('       |       |       ')
    print('  {}    |   {}   |   {}   '.format(posicoes['pos7'], posicoes['pos8'], posicoes['pos9']))
    print('       |       |       ')



def pede_jogada(lista_palpites):
    print('-=-'*15)
    while True:
        jogada = input('Digite uma posição no tabuleiro para jogar: ')
        if jogada.isdigit():
            jogada = int(jogada)
            if jogada in lista_palpites:
                break
            else:
                print('Você digitou um número já pedido, tente novamente')
        else:
                print('Você não digitou um número, tente novamente')
    print('-=-'*15)        
    return jogada


def averigua_jogada(jogada, numero_jogadas, **posicoes):
    for key, value in posicoes.items():
        if jogada == value:
            if numero_jogadas % 2 == 0:
                    posicoes[key] = 'X'
            else:
                    posicoes[key] = 'O'
    return posicoes


def procura_vencedor(**posicoes):
    possibilidade_1 = posicoes['pos1'] == posicoes['pos4'] == posicoes['pos7']
    possibilidade_2 = posicoes['pos1'] == posicoes['pos2'] == posicoes['pos3']
    possibilidade_3 = posicoes['pos1'] == posicoes['pos5'] == posicoes['pos9']
    possibilidade_4 = posicoes['pos2'] == posicoes['pos5'] == posicoes['pos8']
    possibilidade_5 = posicoes['pos3'] == posicoes['pos6'] == posicoes['pos9']
    possibilidade_6 = posicoes['pos4'] == posicoes['pos5'] == posicoes['pos6']
    possibilidade_7 = posicoes['pos7'] == posicoes['pos8'] == posicoes['pos9']
    possibilidade_8 = posicoes['pos3'] == posicoes['pos5'] == posicoes['pos7']
    
    lista_possibilidades = [possibilidade_1, 
                            possibilidade_2, 
                            possibilidade_3, 
                            possibilidade_4, 
                            possibilidade_5, 
                            possibilidade_6, 
                            possibilidade_7, 
                            possibilidade_8]

    for possibilidade in lista_possibilidades:
        if possibilidade == True:
            print('Temos um vencedor! Parabéns!')
            return True

posicoes = {
    'pos1': 1,
    'pos2': 2,
    'pos3': 3,
    'pos4': 4,
    'pos5': 5,
    'pos6': 6,
    'pos7': 7,
    'pos8': 8,
    'pos9': 9
}

lista_palpites = [1, 2, 3, 4, 5, 6, 7, 8, 9]

contador_jogadas = 0

while True:
    mostra_tabuleiro(**posicoes)
    jogada = pede_jogada(lista_palpites)
    lista_palpites[jogada - 1] = 'X'
    posicoes = averigua_jogada(jogada, contador_jogadas, **posicoes)
    if procura_vencedor(**posicoes):
        mostra_tabuleiro(**posicoes)
        break
    contador_jogadas += 1
