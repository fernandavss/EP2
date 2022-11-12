from funcoes import *
from questoes_prof import *
from questoes_passadas import questoes

#Desterminando o nivel da questão
relacao_id_nivel = {1:'facil',2:'facil',3:'facil',4:'medio',5:'medio',6:'medio',7:'dificil',8:'dificil',9:'dificil'}
alternativas = ['A','B','C','D']


#Apresentação do jogo
print("Eai!\n\nVocê está no Fortuna FeCami e vai ter a oportunidade de milhões! Responda às seguintes perguntas e concorra a um prêmio de 1 milhão de reais!!\n")

nome_jogador = input('Qual o seu nome?:')

print('\nBlz, {0}, você tem direito a {1}pular 3 vezes e a 2 ajudas{2}\nSuas opções de resposta são {3}"A", "B", "C", "D", "ajuda", "pula" e "parar".{4}\n'.format(nome_jogador,'\033[0;35m','\033[m','\033[1;36m','\033[m'))

input('Aperte ENTER para continuar...\n')

input('Para a primeira questão, vamos começar com o nivel {0}FÁCIL{1}!\n\nAperte ENTER para continuar...\n\n'.format('\033[0;35m','\033[m'))


#Iniciando jogo
#Checando validade da lista de questões
erros = valida_questoes(questoes_p)
questoes_validas = 0
for dicio_de_erro in erros:
    if dicio_de_erro == {}:
        questoes_validas += 1

#loop de reiniciando jogo
recomeco = True
while recomeco:

    if questoes_validas == len(questoes_p):       #Se toda a base está válida, o jogo roda

        lista_sorteados = []                      #Questões já sorteadas entram aqui

        #Contadores
        jogando = True
        id = 1
        ajudas = 2
        pula = 0
        x=1

        #loop de rodadas
        while jogando:

            #Nível da questão
            nivel = relacao_id_nivel[id]

            if id == 4:
                input('{0}Parabéns! Você atingiu o nível MÉDIO{1}!\nClique ENTER para continuar...\n\n\n'.format('\033[1;32m','\033[m'))
            if id == 7:
                input('{0}Parabéns! Você atingiu o nível DIFÍCIL!{1}\nClique ENTER para continuar...\n\n\n'.format('\033[1;32m','\033[m'))
            
            
            #GERANDO QUESTÃO ATUAL
            questao = sorteia_questao_inedida(questoes, nivel, lista_sorteados)
            
            lista_sorteados.append(questao)

            X = questao_para_texto(questao, id)
            print(X)

            resposta_perg = str(input('resposta: '))
            

            #correto
            if resposta_perg == questao['correta']:
                if id != 9:
                    print('{0}Você acertou! Seu prêmio é de R${1}.{2}'.format('\033[1;32m',premios[id-1],'\033[m'))
                    input('Aperte ENTER para continuar...\n\n\n')
                    id += 1
                else:
                    print('{0}PARABÉNS!!! Você finalizou o jogo e conquistou {1}1 MILHÃO DE REAIS{2}\nTu é FODA{3}'.format('\033[1;37m','\033[1;36m','\033[1;37m','\033[m'))

            #Diferente do correto [ajuda, parar, pular e outro]
            elif resposta_perg != questao['correta']:
                

                #ajuda
                if resposta_perg == 'ajuda':

                    while ajudas!=0 and ajudas != -1:
                        if ajudas == 2:
                            print('ok! Lá vem ajuda! ATENÇÃO: você tem direito a mais uma ajuda')
                            ajudas-=1
                        elif ajudas == 1:
                            print('ok! Lá vem ajuda! ATENÇÃO: você {0}NÃO{1} tem direito a mais ajuda'.format('\033[1;31m','\033[m'))
                            x=1
                            ajudas -= 1
                        input('Aperte ENTER para continuar...')
                        print(gera_ajuda(questao))
                        input('Aperte ENTER para continuar...\n\n')
                        print(X)
                        resposta_pergunta = input('resposta:')
                        if resposta_pergunta == questao['correta']:
                            print('{0}Você acertou! Seu prêmio é de R${1}.{2}'.format('\033[1;32m',premios[id-1],'\033[m'))
                            id +=1
                            break
                        elif resposta_pergunta in alternativas:
                            print('perdeu tudo :(')
                            cont = input('quer continuar jogando [S/N]?')
                            if cont == 'S':
                                ajudas = -1
                                jogando = False
                                recomeco = True
                            elif cont == 'N':
                                print('{0}FIM DO JOGO{1}'.format('\033[1;31m','\033[m'))
                                jogando = False
                                recomeco = False
                        elif resposta_pergunta == 'pula':
                            if pula in [0,1]:
                                input('Ok, pulando! Você ainda tem {0} pulos!\nAperte ENTER para continuar...\n\n\n'.format(2 - pula))
                                pula += 1
                                break
                            elif pula == 2:
                                input('Ok, pulando! ATENÇÃO: você {0}NÃO{1} tem mais direito a pulos!\nAperte ENTER para continuar...\n\n\n'.format('\033[1;31m','\033[m'))
                                pula += 1
                                break
                            else:
                                while resposta_perg == 'pula':
                                    input('{0}Não deu! Você NÃO tem mais direito a pulos!{1}\nAperte ENTER para continuar...\n\n\n'.format('\033[1;31m','\033[m'))
                                    print(X)
                    


                        elif resposta_pergunta == 'ajuda': 
                            if ajudas == 0:
                                while ajudas == 0 and  x==0:
                                    print('voce {0}NÃO{1} tem direito a mais ajudas'.format('\033[1;31m','\033[m'))
                                    input('Aperte ENTER para continuar...\n\n\n')
                                    print(X)
                                    resposta_pergunta = input('resposta:')
                                    if resposta_pergunta == questao['correta']:
                                        print('{0}Você acertou! Seu prêmio é de R${1}.{2}'.format('\033[1;32m',premios[id-1]),'\033[m')
                                        id +=1
                                        break
                                    elif resposta_pergunta in alternativas:
                                        print('Perdeu tudo :(')
                                        cont = input('Quer continuar jogando [S/N]?')
                                        if cont == 'S':
                                            ajudas = -1
                                            jogando = False
                                            recomeco = True
                                        elif cont == 'N':
                                            print('{0}FIM DO JOGO!{1}'.format('\033[1;31m','\033[m'))
                                            jogando = False
                                            recomeco = False
                                    elif resposta_pergunta == 'ajuda':
                                        print('nao')
                                        id += 1
                                    elif resposta_pergunta == 'pula':
                                        print('nao')
                                        id += 1


                            elif ajudas == 1:
                                print('ok! Lá vem ajuda! ATENÇÃO: você {0}NÃO{1} tem direito a mais ajuda'.format('\033[1;31m','\033[m'))
                                ajudas -= 1
                                input('Aperte ENTER para continuar...')
                                print(gera_ajuda(questao))
                                input('Aperte ENTER para continuar...\n\n')
                                print(X)
                                resposta_pergunta = input('resposta:')
                                if resposta_pergunta == questao['correta']:
                                    print('{0}Você acertou! Seu prêmio é de R${1}.{2}'.format('\033[1;32m',premios[id-1],'\033[m'))
                                    id +=1
                                    break
                                elif resposta_pergunta in alternativas:
                                    print('perdeu tudo :(')
                                    cont = input('quer continuar jogando [S/N]?')
                                    if cont == 'S':
                                        ajudas = -1
                                        jogando = False
                                        recomeco = True
                                    elif cont == 'N':
                                        print('{0}FIM DO JOGO{1}'.format('\033[1;31m','\033[m'))
                                        jogando = False
                                        recomeco = False
                                elif resposta_pergunta == 'pula':
                                    if pula in [0,1]:
                                        input('Ok, pulando! Você ainda tem {0} pulos!\nAperte ENTER para continuar...\n\n\n'.format(2 - pula))
                                        pula += 1
                                        break
                                    elif pula == 2:
                                        input('Ok, pulando! ATENÇÃO: você {0}NÃO{1} tem mais direito a pulos!\nAperte ENTER para continuar...\n\n\n'.format('\033[1;31m','\033[m'))
                                        pula += 1
                                        break
                                    else:
                                        while resposta_perg == 'pula':
                                            input('{0}Não deu! Você NÃO tem mais direito a pulos!{1}\nAperte ENTER para continuar...\n\n\n'.format('\033[1;31m','\033[m'))
                                            print(X)
                                

                            






                    while ajudas == 0 and  x==0:
                        print('voce {0}NÃO{1} tem direito a mais ajudas'.format('\033[1;31m','\033[m'))
                        input('Aperte ENTER para continuar...\n\n\n')
                        print(X)
                        resposta_pergunta = input('resposta:')
                        if resposta_pergunta == questao['correta']:
                            print('{0}Você acertou! Seu prêmio é de R${1}.{2}'.format('\033[1;32m',premios[id-1]),'\033[m')
                            id +=1
                            break
                        elif resposta_pergunta in alternativas:
                            print('Perdeu tudo :(')
                            cont = input('Quer continuar jogando [S/N]?')
                            if cont == 'S':
                                ajudas = -1
                                jogando = False
                                recomeco = True
                            elif cont == 'N':
                                print('{0}FIM DO JOGO!{1}'.format('\033[1;31m','\033[m'))
                                jogando = False
                                recomeco = False
                        elif resposta_pergunta == 'ajuda':
                            print('nao')
                            id += 1
                        elif resposta_pergunta == 'pula':
                            print('nao')
                            id += 1

                #parar
                elif resposta_perg == 'parar':
                    print('{0}FIM DO JOGO{1}'.format('\033[1;31m','\033[m'))
                    recomeco = False
                    break
                    

                #pular
                elif resposta_perg == 'pula':
                    if pula in [0,1]:
                        input('Ok, pulando! Você ainda tem {0} pulos!\nAperte ENTER para continuar...\n\n\n'.format(2 - pula))
                        pula += 1
                    elif pula == 2:
                        input('Ok, pulando! ATENÇÃO: você {0}NÃO{1} tem mais direito a pulos!\nAperte ENTER para continuar...\n\n\n'.format('\033[1;31m','\033[m'))
                        pula += 1
                    else:
                        while resposta_perg == 'pula':
                            input('{0}Não deu! Você NÃO tem mais direito a pulos!{1}\nAperte ENTER para continuar...\n\n\n'.format('\033[1;31m','\033[m'))
                            print(X)
                            resposta_perg = str(input('resposta: '))
                        if resposta_perg == questao['correta']:
                            print('{0}Você acertou! Seu prêmio é de R${1}.{2}'.format('\033[1;32m',premios[id-1],'\033[m'))
                            id += 1
                        elif resposta_perg in alternativas and resposta_perg != questao['correta']:
                            print('perdeu tudo :(')
                            cont = input('quer continuar jogando [S/N]?')
                            if cont == 'S':
                                ajudas = -1
                                jogando = False
                                recomeco = True
                            elif cont == 'N':
                                print('{0}FIM DO JOGO{1}'.format('\033[1;31m','\033[m'))
                                jogando = False
                                recomeco = False
                        elif resposta_perg == 'parar':
                            print('{0}FIM DO JOGO{1}'.format('\033[1;31m','\033[1;31m'))
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
                                input('Aperte ENTER para continuar...\n\n')
                                print(X)
                                resposta_pergunta = input('resposta:')
                                if resposta_pergunta == questao['correta']:
                                    print('{0}Você acertou! Seu prêmio é de R${1}.{2}'.format('\033[1;32m',premios[id-1],'\033[m'))
                                    id +=1
                                    break
                                elif resposta_pergunta in alternativas:
                                    print('perdeu tudo :(')
                                    cont = input('quer continuar jogando [S/N]?')
                                    if cont == 'S':
                                        ajudas = -1
                                        jogando = False
                                        recomeco = True
                                    elif cont == 'N':
                                        print('{0}FIM DO JOGO{1}'.format('\033[1;31m','\033[m'))
                                        jogando = False
                                        recomeco = False

                #errado a alternativa
                elif resposta_perg in alternativas:
                    print('perdeu tudo :(')
                    cont = input('quer continuar jogando [S/N]?')
                    if cont == 'S':
                        ajudas = -1
                        jogando = False
                        recomeco = True
                    elif cont == 'N':
                        print('{0}FIM DO JOGO{1}'.format('\033[1;31m','\033[m'))
                        jogando = False
                        recomeco = False
                


                #outro (resposta aleatoria)
                else:
                    print('Opção inválida!\n{0}ERRO RUDE{1}\nAs opções de resposta são: {2}A,B,C,D, ajuda, pula e sair{3}'.format('\033[1;31m','\033[m','\033[1;36m','\033[m'))
                    resposta_perg = input('resposta:')


                    if resposta_perg == questao['correta']:
                        print('{0}Você acertou! Seu prêmio é de R${1}.{2}'.format('\033[1;32m',premios[id-1],'\033[m'))
                        id+=1


                    elif resposta_perg in alternativas:
                        print('perdeu tudo :(')
                        cont = input('quer continuar jogando [S/N]?')
                        if cont == 'S':
                            ajudas = -1
                            jogando = False
                            recomeco = True
                        elif cont == 'N':
                            print('{0}FIM DO JOGO{1}'.format('\033[1;31m','\033[m'))
                            jogando = False
                            recomeco = False
                    


                    elif resposta_perg == 'pula':
                            if pula in [0,1]:
                                input('Ok, pulando! Você ainda tem {0} pulos!\nAperte ENTER para continuar...\n\n\n'.format(2 - pula))
                                pula += 1
                            elif pula == 2:
                                input('Ok, pulando! ATENÇÃO: você não tem mais direito a pulos!\nAperte ENTER para continuar...\n\n\n')
                                pula += 1
                            else:
                                while resposta_perg == 'pula':
                                    input('{0}Não deu! Você NÃO tem mais direito a pulos!{1}\nAperte ENTER para continuar...\n'.format('\033[1;31m','\033[m'))
                                    print(X)
                                    resposta_perg = str(input('resposta: '))
                                if resposta_perg == questao['correta']:
                                    print('{0}Você acertou! Seu prêmio é de R${1}.{2}'.format('\033[1;32m',premios[id-1],'\033[m'))
                                    id += 1
                                elif resposta_perg in alternativas and resposta_perg != questao['correta']:
                                    print('perdeu tudo :(')
                                    cont = input('quer continuar jogando [S/N]?')
                                    if cont == 'S':
                                        ajudas = -1
                                        jogando = False
                                        recomeco = True
                                    elif cont == 'N':
                                        print('{0}FIM DO JOGO{1}'.format('\033[1;31m','\033[m'))
                                        jogando = False
                                        recomeco = False


                    elif resposta_perg == 'parar':
                        print('{0}FIM DO JOGO{1}'.format('\033[1;31m','\033[m'))
                        recomeco = False
                        break 



                    elif resposta_perg == 'ajuda':
                            while ajudas!=0:
                                if ajudas == 2:
                                    print('ok! Lá vem ajuda! ATENÇÃO: você tem direito a mais uma ajuda')
                                    ajudas-=1
                                elif ajudas == 1:
                                    print('ok! Lá vem ajuda! ATENÇÃO: você NAO tem direito a mais ajuda')
                                    ajudas -= 1
                                input('Aperte ENTER para continuar...')
                                print(gera_ajuda(questao))
                                input('Aperte ENTER para continuar...\n')
                                print(X)
                                resposta_pergunta = input('resposta:')
                                if resposta_pergunta == questao['correta']:
                                    print('{0}Você acertou! Seu prêmio é de R${1}.{2}'.format('\033[1;32m',premios[id-1],'\033[m'))
                                    id +=1
                                    break
                                elif resposta_pergunta in alternativas:
                                    print('perdeu tudo :(')
                                    cont = input('quer continuar jogando [S/N]?')
                                    if cont == 'S':
                                        ajudas = -1
                                        jogando = False
                                        recomeco = True
                                    elif cont == 'N':
                                        print('{0}FIM DO JOGO{1}'.format('\033[1;31m','\033[m'))
                                        jogando = False
                                        recomeco = False
                                elif resposta_pergunta == 'pula':
                                    if pula in [0,1]:
                                        input('Ok, pulando! Você ainda tem {0} pulos!\nAperte ENTER para continuar...'.format(2 - pula))
                                        pula += 1
                                    elif pula == 2:
                                        input('Ok, pulando! ATENÇÃO: você NÃO tem mais direito a pulos!\nAperte ENTER para continuar...')
                                        pula += 1
                                    else:
                                        while resposta_perg == 'pula':
                                            input('{0}Não deu! Você não tem mais direito a pulos!{1}\nAperte ENTER para continuar...'.format('\033[1;31m','\033[m'))
                                            print(X)
                                            resposta_perg = str(input('resposta: '))
                                        if resposta_perg == questao['correta']:
                                            print('{0}Você acertou! Seu prêmio é de R${1}.{2}'.format('\033[1;32m',premios[id-1],'\033[m'))
                                            id += 1
                                        elif resposta_perg in alternativas and resposta_perg != questao['correta']:
                                            print('perdeu tudo :(')
                                            cont = input('quer continuar jogando [S/N]?')
                                            if cont == 'S':
                                                ajudas = -1
                                                jogando = False
                                                recomeco = True
                                            elif cont == 'N':
                                                print('{0}FIM DO JOGO{1}'.format('\033[1;31m','\033[m'))
                                                jogando = False
                                                recomeco = False

                






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
                                ajudas = -1
                                jogando = False
                                recomeco = True
                            elif cont == 'N':
                                print('saindo...')
                                jogando = False
                                recomeco = False
                            elif resposta_pergunta == 'pula':
                                if pula in [0,1]:
                                    input('Ok, pulando! Você ainda tem {0} pulos!\nAperte ENTER para continuar...'.format(2 - pula))
                                    pula += 1
                                elif pula == 2:
                                    input('Ok, pulando! ATENÇÃO: você não tem mais direito a pulos!\nAperte ENTER para continuar...')
                                    pula += 1
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
                                            ajudas = -1
                                            jogando = False
                                            recomeco = True
                                        elif cont == 'N':
                                            print('saindo...')
                                            jogando = False
                                            recomeco = False
                        elif resposta_perg == 'parar':
                            print('saindo...')
                            break
                        elif resposta_pergunta == 'ajuda':
                            while ajudas!=0:
                                if ajudas == 2:
                                    print('ok! Lá vem ajuda! ATENÇÃO: você tem direito a mais uma ajuda')
                                    ajudas-=1
                                elif ajudas == 1:
                                    print('ok! Lá vem ajuda! ATENÇÃO: você NAO tem direito a mais ajuda')
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
                                        ajudas = -1
                                        jogando = False
                                        recomeco = True
                                    elif cont == 'N':
                                        print('saindo...')
                                        jogando = False
                                        recomeco = False
                                elif resposta_pergunta == 'pula':
                                    if pula in [0,1]:
                                        input('Ok, pulando! Você ainda tem {0} pulos!\nAperte ENTER para continuar...'.format(2 - pula))
                                        pula += 1
                                    elif pula == 2:
                                        input('Ok, pulando! ATENÇÃO: você não tem mais direito a pulos!\nAperte ENTER para continuar...')
                                        pula += 1
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
                                                ajudas = -1
                                                jogando = False
                                                recomeco = True
                                            elif cont == 'N':
                                                print('saindo...')
                                                jogando = False
                                                recomeco = False
                                elif resposta_perg == 'parar':
                                    print('saindo...')
                                    break
