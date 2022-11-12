from funcoes import *
from questoes_prof import *
from questoes_passadas import questoes


relacao_id_nivel = {1:'facil',2:'facil',3:'facil',4:'medio',5:'medio',6:'medio',7:'dificil',8:'dificil',9:'dificil'}
alternativas = ['A','B','C','D']

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
    erro = 0
    ajudas = 2
    pula = 0

    while jogando:

        nivel = relacao_id_nivel[id]


        if erro == 0:
            questao = sorteia_questao_inedida(questoes, nivel, lista_sorteados)
            lista_sorteados.append(questao)

            X = questao_para_texto(questao, id)
            print(X)

            resposta_perg = str(input('resposta: '))

            print(questao['correta'])
            
            #correto
            if resposta_perg == questao['correta']:
                print('Você acertou! Seu prêmio é de R${0}'.format(premios[id-1]))
                input('Aperte ENTER para continuar...')
                id += 1

            elif resposta_perg != questao['correta']:
                
                #ajuda
                if resposta_perg == 'ajuda':

                    while ajudas!=0:
                        if ajudas == 2:
                            print('ok! Lá vem ajuda! ATENÇÃO: você tem direito a mais uma ajuda')
                            ajudas-=1
                        elif ajudas == 1:
                            print('ok! Lá vem ajuda! ATENÇÃO: você NAO tem direito a mais ajuda')
                            k=1
                            ajudas -= 1
                        input('Aperte ENTER para continuar...')
                        print(gera_ajuda(questao))
                        input('Aperte ENTER para continuar...')
                        print(X)
                        resposta_pergunta = input('resposta:')
                        if resposta_pergunta == questao['correta']:
                            print('Você acertou! Seu prêmio é de R${0}'.format(premios[id-1]))
                            id +=1
                            break
                        elif resposta_pergunta in alternativas:
                            print('perdeu tudo :( ) ')
                            cont = input('quer continuar jogando [S/N]?')
                            if cont == 'S':
                                id = 1
                                erro = 0
                                pula = 0 
                                ajudas = 2
                                jogando = True
                            elif cont == 'N':
                                jogando = False
                        #rever pulo
                        elif resposta_pergunta == 'pula':
                            if pula in [0,1]:
                                input('Ok, pulando! Você ainda tem {0} pulos!\nAperte ENTER para continuar...'.format(2 - pula))
                                pula += 1
                                break
                            elif pula == 2:
                                input('Ok, pulando! ATENÇÃO: você não tem mais direito a pulos!\nAperte ENTER para continuar...')
                                pula += 1
                                break
                            else:
                                while resposta_perg == 'pula':
                                    input('{0}Não deu! Você não tem mais direito a pulos!{1}\nAperte ENTER para continuar...'.format('\033[1;31m','\033[m'))
                                    print(X)
                    
                    while ajudas == 0:
                        print('voce nao tem direito a mais ajudas')
                        input('Aperte ENTER para continuar...')
                        print(X)
                        resposta_pergunta = input('resposta:')
                        if resposta_pergunta == questao['correta']:
                            print('Você acertou! Seu prêmio é de R${0}'.format(premios[id-1]))
                            id +=1
                            break
                        elif resposta_pergunta in alternativas:
                            print('perdeu tudo :( ) ')
                            cont = input('quer continuar jogando [S/N]?')
                            if cont == 'S':
                                id = 1
                                erro = 0
                                pula = 0 
                                ajudas = 0
                                jogando = True
                            elif cont == 'N':
                                jogando = False
                            erro +=1
                        elif resposta_pergunta == 'ajuda':
                            print('nao')
                            id += 1
                        elif resposta_pergunta == 'pula':
                            print('nao')
                            id += 1

                #parar
                elif resposta_perg == 'parar':
                    print('saindo...')
                    break

                #pular
                elif resposta_perg == 'pula':
                    if pula in [0,1]:
                        input('Ok, pulando! Você ainda tem {0} pulos!\nAperte ENTER para continuar...'.format(2 - pula))
                        pula += 1
                        id+=1
                    elif pula == 2:
                        input('Ok, pulando! ATENÇÃO: você não tem mais direito a pulos!\nAperte ENTER para continuar...')
                        pula += 1
                        id+=1
                    else:
                        while resposta_perg == 'pula':
                            input('{0}Não deu! Você não tem mais direito a pulos!{1}\nAperte ENTER para continuar...'.format('\033[1;31m','\033[m'))
                            print(X)
                            resposta_perg = str(input('resposta: '))
                        if resposta_perg == questao['correta']:
                            print('Você acertou! Seu prêmio é de R${0}'.format(premios[id-1]))
                            id += 1
                        elif resposta_perg in alternativas and resposta_perg != questao['correta']:
                            print('perdeu tudo :( ) ')
                            cont = input('quer continuar jogando [S/N]?')
                            if cont == 'S':
                                id = 1
                                erro = 0
                                pula = 0 
                                ajudas = 0
                                jogando = True
                            elif cont == 'N':
                                jogando = False
                        elif resposta_perg == 'sair':
                            print('saindo...')
                            break
                        elif resposta_perg == 'ajuda':
                            while ajudas!=0:
                                if ajudas == 2:
                                    print('ok! Lá vem ajuda! ATENÇÃO: você tem direito a mais uma ajuda')
                                    ajudas-=1
                                elif ajudas == 1:
                                    print('ok! Lá vem ajuda! ATENÇÃO: você NAO tem direito a mais ajuda')
                                    k=1
                                    ajudas -= 1
                                input('Aperte ENTER para continuar...')
                                print(gera_ajuda(questao))
                                input('Aperte ENTER para continuar...')
                                print(X)
                                resposta_pergunta = input('resposta:')
                                if resposta_pergunta == questao['correta']:
                                    print('Você acertou! Seu prêmio é de R${0}'.format(premios[id-1]))
                                    id +=1
                                    break
                                elif resposta_pergunta in alternativas:
                                    print('perdeu tudo :( ) ')
                                    cont = input('quer continuar jogando [S/N]?')
                                    if cont == 'S':
                                        id = 1
                                        erro = 0
                                        pula = 0 
                                        ajudas = 0
                                        jogando = True
                                    elif cont == 'N':
                                        jogando = False

                #errado
                elif resposta_perg in alternativas:
                    print('perdeu tudo :( ) ')
                    cont = input('quer continuar jogando [S/N]?')
                    if cont == 'S':
                        id = 1
                        erro = 0
                        pula = 0 
                        ajudas = 0
                        jogando = True
                    elif cont == 'N':
                        jogando = False
                
                #outro
                else:
                    print('opção inválida! ERRO RUDE\n As opções de resposta são: A,B,C,D, ajuda, pula e sair')
                    resposta_perg = input('resposta:')
                    if resposta_perg == questao['correta']:
                        print('Você acertou! Seu prêmio é de R${0}'.format(premios[id-1]))
                        id+=1
                    elif resposta_perg in alternativas:
                        print('perdeu tudo :( ) ')
                        cont = input('quer continuar jogando [S/N]?')
                        if cont == 'S':
                            id = 1
                            erro = 0
                            pula = 0 
                            ajudas = 0
                            jogando = True
                        elif cont == 'N':
                            jogando = False
                    while resposta_perg not in ['A','B','C','D','ajuda','pula','parar']:
                        print('opção inálida!\n As opções de resposta são: A,B,C,D, ajuda, pula e parar')
                        resposta_pergunta = input('resposta:')
                        if resposta_pergunta == questao['correta']:
                            print('Você acertou! Seu prêmio é de R${0}'.format(premios[id-1]))
                            id +=1
                            break
                        elif resposta_pergunta in alternativas:
                            print('perdeu tudo :( ) ')
                            cont = input('quer continuar jogando [S/N]?')
                            if cont == 'S':
                                id = 1
                                erro = 0
                                pula = 0 
                                ajudas = 0
                                jogando = True
                            elif cont == 'N':
                                jogando = False
                        elif resposta_pergunta == 'ajuda':
                            while ajudas!=0:
                                if ajudas == 2:
                                    print('ok! Lá vem ajuda! ATENÇÃO: você tem direito a mais uma ajuda')
                                    ajudas-=1
                                elif ajudas == 1:
                                    print('ok! Lá vem ajuda! ATENÇÃO: você NAO tem direito a mais ajuda')
                                    k=1
                                    ajudas -= 1
                                input('Aperte ENTER para continuar...')
                                print(gera_ajuda(questao))
                                input('Aperte ENTER para continuar...')
                                print(X)
                                resposta_pergunta = input('resposta:')
                                if resposta_pergunta == questao['correta']:
                                    print('Você acertou! Seu prêmio é de R${0}'.format(premios[id-1]))
                                    id +=1
                                    break
                                elif resposta_pergunta in alternativas:
                                    print('perdeu tudo :( ) ')
                                    cont = input('quer continuar jogando [S/N]?')
                                    if cont == 'S':
                                        id = 1
                                        erro = 0
                                        pula = 0 
                                        ajudas = 0
                                        jogando = True
                                    elif cont == 'N':
                                        jogando = False

                        elif resposta_pergunta == 'pula':
                            if pula in [0,1]:
                                input('Ok, pulando! Você ainda tem {0} pulos!\nAperte ENTER para continuar...'.format(2 - pula))
                                pula += 1
                                id+=1
                            elif pula == 2:
                                input('Ok, pulando! ATENÇÃO: você não tem mais direito a pulos!\nAperte ENTER para continuar...')
                                pula += 1
                                id+=1
                            else:
                                while resposta_perg == 'pula':
                                    input('{0}Não deu! Você não tem mais direito a pulos!{1}\nAperte ENTER para continuar...'.format('\033[1;31m','\033[m'))
                                    print(X)
                                    resposta_perg = str(input('resposta: '))
                                if resposta_perg == questao['correta']:
                                    print('Você acertou! Seu prêmio é de R${0}'.format(premios[id-1]))
                                    id += 1
                                elif resposta_perg in alternativas and resposta_perg != questao['correta']:
                                    print('perdeu tudo :( ) ')
                                    cont = input('quer continuar jogando [S/N]?')
                                    if cont == 'S':
                                        id = 1
                                        erro = 0
                                        pula = 0 
                                        ajudas = 0
                                        jogando = True
                                    elif cont == 'N':
                                        jogando = False
                        elif resposta_perg == 'parar':
                            print('saindo...')
                            break

      