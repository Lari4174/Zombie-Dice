import random
import time

print("\/\/\/\/\/ JOGO - ZOMBIE DICE \/\/\/\/\/")
print(" Seja bem-vindo(a) ao jogo Zombie Dice! ")
numJogadores = 0
score = []
while numJogadores < 2:
    numJogadores = int(input(" Informe a quantidade de jogadores: "))
    if numJogadores < 2:
        print(" AVISO: Você precisa de pelo menos 2 jogadores! ")

listaJogadores = []
for i in range(numJogadores):
    print(" Informe o nome do jogador", (i) + 1, ":")
    nome = input(" Olá jogador {}, qual é seu nome? ".format(i))
    print(" Olá {}, seja bem-vindo(a) ao jogo! ".format(nome))
    score.append(0)
    listaJogadores.append(nome)
    listaJogadores[i] = nome

dadoVerde = "CPCTPC"
dadoAmarelo = "TPCTPC"
dadoVermelho = "TPTCPT"

listaDados = [
    dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde,
    dadoAmarelo, dadoAmarelo, dadoAmarelo, dadoAmarelo,
    dadoVermelho, dadoVermelho, dadoVermelho
]

print("        INICIANDO O JOGO...")
scoreJogador = []
jogadorAtual = 0
dadosSorteados = []
tiros = 0
cerebros = 0
passos = 0
pontua = 0
listaGa = []
for i in range(numJogadores):
    listaGa.append(0)
print(listaGa)
while True:
    print("        TURNO DO JOGADOR: ", listaJogadores[jogadorAtual])
    for i in range(0, 3, 1):
        numSorteado = random.randint(0, 12)
        dadoSorteado = listaDados[numSorteado]
        if dadoSorteado == "CPCTPC":
            corDado = "VERDE"
        elif dadoSorteado == "TPCTPC":
            corDado = "AMARELO"
        else:
            corDado = "VERMELHO"
        print("      Dado sorteado: ", corDado)
        dadosSorteados.append(dadoSorteado)
        time.sleep(1)
    print("\n    As faces sorteadas foram: ")
    for dadoSorteado in dadosSorteados:
        numFaceDado = random.randint(0, 5)
        if dadoSorteado[numFaceDado] == "C":
            print("- CÉREBRO (você comeu um cérebro) -")
            cerebros = cerebros + 1
        elif dadoSorteado[numFaceDado] == "T":
            print("-    TIRO (você levou um tiro)    -")
            tiros = tiros + 1
        else:
            print("-   PASSOS (uma vítima escapou)   -")
            passos = passos + 1
        time.sleep(1)
    print("\n           SCORE ATUAL: ")
    print(" CÉREBROS: ", cerebros)
    print(" TIROS: ", tiros)
    VerificadorT = True
    if tiros >= 3:
        print(" AVISO: você perdeu seu score! ")
        dadosSorteados = []
        tiros = 0
        cerebros = 0
        passos = 0
        if jogadorAtual == len(listaJogadores) - 1:
            jogadorAtual = 0
            continuarJogando = input(" AVISO: todos os jogadores querem jogar mais uma rodada? (s/n) ")
            if continuarJogando == 's':
                break
            elif continuarJogando == 'n':
                VerificadorT = False
                pass
            else:
                print("Resposta inválida! Utilize apenas 's' ou 'n', continuando! ")
                continue

        else:
            jogadorAtual = jogadorAtual + 1
    else:
        VerificadorV = cerebros + score[jogadorAtual]
        if VerificadorV >= 13:
            print(" Você atingiu o placar para ganhar, com: " + str(VerificadorV) + " cérebros! ")
            listaGa[jogadorAtual] = VerificadorV
            pontua = cerebros
            Tpontua = score[jogadorAtual] + pontua
            score[jogadorAtual] = Tpontua
            print(" Sua pontuação atual é: " + str(score[jogadorAtual]) + " cérebros! ")
            jogadorAtual = jogadorAtual + 1
            dadosSorteados = []
            tiros = 0
            cerebros = 0
            passos = 0
            pontua = 0
        else:
            continuarTurno = input(" AVISO: Você deseja continuar jogando dados? (s/n) ")
            if continuarTurno == 'n':
                pontua = cerebros
                Tpontua = score[jogadorAtual] + pontua
                score[jogadorAtual] = Tpontua
                print(" Sua pontuação atual é: " + str(score[jogadorAtual]) + " cérebros! ")
                jogadorAtual = jogadorAtual + 1
                dadosSorteados = []
                tiros = 0
                cerebros = 0
                passos = 0
                pontua = 0
            else:
                print("Resposta inválida! Use apenas 's' ou 'n', continuando! ")

    if VerificadorT is False:
        print(" Finalizando o jogo... ")
        break
    else:
        if jogadorAtual == len(listaJogadores):
            continuarJogando = input(" AVISO: todos os jogadores querem jogar mais uma rodada? (s/n) ")
            if (continuarJogando == 's'):
                print(" Iniciando mais um turno! ")
                jogadorAtual = 0
                continue
            elif continuarJogando == 'n':
                print(" Finalizando o jogo... ")
                break
            else:
                print("Resposta inválida! Use apenas 's' ou 'n', continuando! ")
        else:
            print(" Iniciando mais uma rodada do turno atual... ")
        dadosSorteados = []

jogadorAtual = 0
for i in range(numJogadores):
    print(" O jogador: " + str(listaJogadores[jogadorAtual]) + " comeu: " + str(score[jogadorAtual]) + " cérebros. ")
    jogadorAtual = jogadorAtual + 1
print(listaGa)
