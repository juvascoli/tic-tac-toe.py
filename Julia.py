

import random

# Matriz de três linhas por três colunas
board = [[0,0,0], 
         [0,0,0], 
         [0,0,0]]

# função que inicializa o tabuleiro
def inicializacaoTabuleiro(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] = ' '  


# Função que imprime o tabuleiro
def imprimeTabuleiro(board):
    for i in board:
           print(i)


def menuPrincipal():
    print(" # JOGUINHO DA VELHA  #")
    print(" ################## ")
    print("1: Modo Jogador | jogador-1 vs jogador-2")
    print("2: Modo fácil | jogador vs máquina ")
    print("3: Modo difícil | jogador vs máquina ")
    print(" ################## ")

    opcaoEscolhida = input("Opção desejada: ")

    if opcaoEscolhida == '1':
        print("Modo Jogador | jogador-1 vs jogador-2")
        modoJogador(board)
        imprimeTabuleiro(board)
    elif opcaoEscolhida == '2':
        print("Modo fácil | jogador vs máquina")
        modoFacil(board)
    elif opcaoEscolhida == '3':
        print("Modo difícil | jogador vs máquina")
        modoDificil(board)
    else:
        print("Opção inválida. Por favor, escolha uma opção entre 1 e 3.")





# receber as coordenadas do usuario
def leiaCoodernadaLinha():
       i = int(input("Escolha a linha [0, 1, 2]: "))
       if i in [0, 1, 2]:
           return i
       else:
           print("Linha inválida. Escolha uma linha entre 0 e 2.")


# receber as coordenadas do usuario
def leiaCoordenadaColuna():
       j = int(input("Escolha a coluna [0, 1, 2]: "))
       if j in [0, 1, 2]:
           return j
       else:
           print("Coluna inválida. Escolha uma coluna entre 0 e 2.")


# função que faz o jogo rodar
def jogar(jogadorAtual, board, leiaCoodernadaLinha, leiaCoordenadaColuna):
    # solicita a linha e a coluna para o jogador atual a partir dessas funções
    i = leiaCoodernadaLinha()
    j = leiaCoordenadaColuna()
    
    # Verifica se a posição é válida
    if posicaoValida(board, i, j):
        # Atualiza o tabuleiro
        board[i][j] = jogadorAtual
        return True
    else:
        print("Posição inválida. Tente novamente.")
        return False
    

# função que imprime pontuacao
def imprimePontuacao(verificaVencedor, board, pontos):
    pontos = {'X': 0, 'O': 0}
    vencedor = verificaVencedor()
    
    if vencedor in pontos:
        pontos[vencedor] += 1
    
    print(f"Pontos: X = {vencedor['X']}, O = {vencedor['O']}")





def verificaVencedor(board):
    # Ve se tem linha vencedora
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' ':
            return board[i][0]
    
    # Ve se tem coluna vencedora
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
            return board[0][i]
    
    # Ve se tem alguma diagonal vencedora
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    
    # Caso n tenha vencedor, retorna None
    return None

def posicaoValida(board, i, j):
    # Ve se a posição tá dentro do limites da matriz board (3x3)
    return 0 <= i < 3 and 0 <= j < 3 and board[i][j] == ' '

# Função que faz o jogo rodar
def jogar(jogadorAtual, board, leiaCoodernadaLinha, leiaCoordenadaColuna):
    # Solicitação a linha e a coluna para o jogador que tá jogando
    i = leiaCoodernadaLinha()
    j = leiaCoordenadaColuna()
    
    # Verifica se a posição é ou naão válida
    if posicaoValida(board, i, j):
        # Atualiza o tabuleiro
        board[i][j] = jogadorAtual
        return True


# Função que imprime a pontuação
def imprimePontuacao(verificaVencedor, board, pontos):

    vencedor = verificaVencedor(board)
    if vencedor:
        pontos[vencedor] += 1
        print(f"Pontos: X = {pontos['X']}, O = {pontos['O']}")

# Verifica se deu empate
def verificarVelha(board):
    for i in board:
        if ' ' in i:
            return False
    return True

# Função que alterna entre jogador e jogardo
def mudarJogador(jogadorAtual):
    return 'O' if jogadorAtual == 'X' else 'X'


# modo jogador-usuario #1
def modoJogador(board):
    inicializacaoTabuleiro(board)
    jogadorAtual = 'X'
    pontos = {'X': 0, 'O': 0}

    while True:
        imprimeTabuleiro(board)
        jogada = jogar(jogadorAtual, board, leiaCoodernadaLinha, leiaCoordenadaColuna)
        
        if jogada:
            vencedor = verificaVencedor(board) #checa se há vencedores na partida
            if vencedor in board: #caso seja achado um ganhador
                print(f"jogador {vencedor} venceu")
                imprimePontuacao(verificaVencedor, board, pontos) #atualiza as info
                break
            elif verificarVelha(board):
                print("empate")
                break
            
            jogadorAtual = mudarJogador(jogadorAtual)
        else:
            print("opa! tente de novo ")
    
inicializacaoTabuleiro(board)




def verificarVencedorMaquina(board, jogador):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = jogador
                if verificaVencedor(board) == jogador:
                    board[i][j] = ' '
                    return (i, j)
                board[i][j] = ' '
    return None

def jogadaMaquinaDificil(board):
    # maquina tenta ganhar 
    jogada = verificarVencedorMaquina(board, 'O')
    if jogada:
        board[jogada[0]][jogada[1]] = 'O'
        return
    
    # Tenta bloquear a jogada do jogador
    jogada = verificarVencedorMaquina(board, 'X')
    if jogada:
        board[jogada[0]][jogada[1]] = 'O'
        return
    
    # joga no centro se tiver disponível
    if board[1][1] == ' ':
        board[1][1] = 'O'
        return
    
    # Joga em cantos se tiver disponível
    cantos = [(0, 0), (0, 2), (2, 0), (2, 2)]
    for (i, j) in cantos:
        if board[i][j] == ' ':
            board[i][j] = 'O'
            return
    

# modo dificil entre maquina e usuario
def modoDificil(board):
    inicializacaoTabuleiro(board)
    jogadorAtual = 'X'  
    
    while True:
        imprimeTabuleiro(board)
        print( "----------")
        
        if jogadorAtual == 'X':
            jogar(jogadorAtual, board, leiaCoodernadaLinha, leiaCoordenadaColuna)
        else:
            jogadaMaquinaDificil(board)
        
        vencedor = verificaVencedor(board)
        if vencedor:
            imprimeTabuleiro(board)
            print(f"jogador {vencedor} venceu!")
            break
        
        if verificarVelha(board):
            print("empate!")
            break
        
        jogadorAtual = mudarJogador(jogadorAtual)



# modo facil entre maquina e usuario
def modoFacil(board):
    inicializacaoTabuleiro(board)  
    jogadorAtual = 'X'  
    pontos = {"X": 0, "O": 0}

    while True:
        imprimeTabuleiro(board)
        
        # ve as coordenada da jogada dos jogadores
        print("sua vez de jogar")
        i = leiaCoodernadaLinha()
        j = leiaCoordenadaColuna()
        
        if posicaoValida(board, i, j):
            board[i][j] = jogadorAtual
        else:
            print("Posição inválida. Tente novamente.")
            continue

        # Verifica se o jogador ganhou ou se o jogo empatou
        vencedor = verificaVencedor(board)
        if vencedor:
            imprimeTabuleiro(board)
            print(f"Jogador {vencedor} venceu!")
            imprimePontuacao(verificaVencedor, board, pontos)
            break
        elif verificarVelha(board):
            imprimeTabuleiro(board)
            print("Empate!")
            break
        
        # Muda para o próximo jogador
        jogadorAtual = mudarJogador(jogadorAtual)
        
        # Jogada da máquina
        print("Vez da máquina!")
        while True:
            i, j = jogadaMaquinaFacil(board)
            if posicaoValida(board, i, j):
                board[i][j] = jogadorAtual
                break




def jogadaMaquinaFacil(board):
        while True:
            # gera uma linha e uma coluna aleatória
            i = random.randint(0, 2)
            j = random.randint(0, 2)
            # vê se ta vazio
            if board[i][j] == ' ':
                return i, j

     

menuPrincipal()
