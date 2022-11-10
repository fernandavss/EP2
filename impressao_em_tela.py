from funcoes import *
from questoes_prof import *
from questoes_passadas import questoes


relacao_id_nivel = {1:'facil',2:'facil',3:'facil',4:'medio',5:'medio',6:'medio',7:'dificil',8:'dificil',9:'dificil'}

#Apresentação do jogo

print("Eai!\nVocê está no Fortuna FeCami e vai ter a oportunidade de milhões! Responda às seguintes perguntas e concorra a um prêmio de 1 milhão de reais!!")

#Primeira interação

nome_jogador = input('Qual o seu nome?:')

print('Blz, {0}, você tem direito a {1}pular 3 vezes e a 2 ajudas{2}\nSuas opções de resposta são {3}"A", "B", "C", "D", "ajuda", "pula" e "parar".{4}\nNada além disso, ein..!'.format(nome_jogador,'\033[0;35m','\033[m','\033[1;36m','\033[m'))

input('Aperte ENTER para continuar...')

input('Lá vem a primeira questão!\nVamos começar com questões de nivel {0}FÁCIL{1}!\nAperte ENTER para continuar...'.format('\033[0;35m','\033[m'))


#Passo 1: Checando validade da lista de questões
p_1 = valida_questoes(questoes_p)

soma = 0

for dicio_de_erro in p_1:
    if dicio_de_erro == {}:
        soma += 1
print(soma)
print(len(questoes))
if soma == len(questoes_p):
    print('c')

    lista_sorteados = []
    #Passo 2: Separando-as por nível em um dicionário (t_1)

    jogando = True
    id = 1

    while jogando:

        nivel = relacao_id_nivel[id]

        questao = sorteia_questao_inedida(questoes, nivel, lista_sorteados)
        lista_sorteados.append(questao)

        print(questao_para_texto(questao, id))

        jogando = False