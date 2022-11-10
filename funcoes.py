# Definindo as funções que serão usadas no programa


# TRANSFORMA BASE DE QUESTÕES
# recebe uma lista de questões e separa as questões por nível (acessada em um dicio)
def transforma_base(questoes_lista):
    questoes_por_nivel = {}
    for questao in questoes_lista:
        nivel = questao['nivel']
        if nivel not in questoes_por_nivel:
            questoes_por_nivel[nivel] = [questao]
        else:
            questoes_por_nivel[nivel].append(questao)
    return questoes_por_nivel

#VALIDA UMA QUESTÃO
#identifica erro numa questão
def valida_questao(questao):
    dicio = {}
    
    chaves = ['titulo', 'nivel', 'opcoes', 'correta']
    for key in chaves:
        if key not in questao:
            dicio[key] = 'nao_encontrado'
    
    if len(questao) != 4:
        dicio['outro'] = 'numero_chaves_invalido'
    
    if 'titulo' in questao:
        a = questao['titulo']
        if a.strip() == '':
            dicio['titulo'] = 'vazio'
    
    if 'nivel' in questao:
        lista = ['facil', 'medio','dificil']
        if questao['nivel'] not in lista:
            dicio['nivel'] = 'valor_errado'
    
    lista_de_opcoes = ['A', 'B', 'C', 'D']
    if 'opcoes' in questao:
        if len(questao['opcoes']) != 4:
            dicio['opcoes'] = 'tamanho_invalido'
        else:
            if lista_de_opcoes != list(questao['opcoes']):
                dicio['opcoes'] = 'chave_invalida_ou_nao_encontrada'
            else:
                dicio_1 = {}
                for e, i in questao['opcoes'].items():
                    if i.strip() == '':
                        dicio_1[e] = 'vazia'
                if dicio_1 != {}:
                    dicio['opcoes'] = dicio_1
                
    if 'correta' in questao:
        if questao['correta'] not in lista_de_opcoes:
            dicio['correta'] = 'valor_errado'
    
    return dicio

# VALIDA LISTA DE QUESTÕES
# recebe uma lista de questões e retorna uma lista de erros encontrados
def valida_questoes(questoes_lista):
    lista = []
    for quest in questoes_lista:
        a = valida_questao(quest)
        lista.append(a)
    return lista

# SORTEIA UMA QUESTÃO
import random

def sorteia_questao(dicio_questoes, nivel):
    questoes_do_nivel = dicio_questoes[nivel]
    a = random.choice(questoes_do_nivel)
    return a

#SORTEIA UMA QUESTÃO INÉDITA
def sorteia_questao_inedida(dicio_questoes, nivel, lista_sorteados):
    q = sorteia_questao(dicio_questoes,nivel)
    a = True
    while a:
        if q in lista_sorteados:
            q = sorteia_questao(dicio_questoes,nivel)
        else:
            a = False
    lista_sorteados.append(q)
    return q

#QUESTÃO PARA TEXTO

def questao_para_texto(questao, id):
    a = '----------------------------------------\nQUESTAO {0}\n\n{1}\n\nRESPOSTAS:\n{2}: {3}\n{4}: {5}\n{6}: {7}\n{8}: {9}\n'.format(id,questao['titulo'],list(questao['opcoes'])[0],questao['opcoes']['A'],list(questao['opcoes'])[1],questao['opcoes']['B'],list(questao['opcoes'])[2],questao['opcoes']['C'],list(questao['opcoes'])[3],questao['opcoes']['D'])
    return a

#GERA AJUDA EM UMA QUESTÃO
def gera_ajuda(questao):
    lista_de_opcoes = list(questao['opcoes'])
    lista_de_opcoes.remove(questao['correta'])
    vezes = random.randint(1,2)
    if vezes == 1:
        alternativa_1 = random.choice(lista_de_opcoes)
        a1 = questao['opcoes'][alternativa_1]
        return 'DICA:\nOpções certamente erradas: {0}'.format(a1)

    elif vezes == 2:
        alternativa_1 = random.choice(lista_de_opcoes)
        a1 = questao['opcoes'][alternativa_1]
        lista_de_opcoes.remove(alternativa_1)
        alternativa_2 = random.choice(lista_de_opcoes)
        a2 = questao['opcoes'][alternativa_2]
        return 'DICA:\nOpções certamente erradas: {0} | {1}'.format(a1,a2)

from questoes_passadas import *
from lista_premio import *

#produz questao

def produz_uma_questao(questoes,nivel,id):
    lista_sorteados = list(range(1,id))

    questao = sorteia_questao_inedida(questoes, nivel, lista_sorteados)
    questao_para_texto(questao, id)
    
    resposta = input('Qual sua resposta?!')
    
    alternativa_correta = questao['correta']
    lista_de_alternativas = ['A', 'B', 'C', 'D']
    lista_de_erradas = lista_de_alternativas.remove(alternativa_correta)
    
    
    if resposta == alternativa_correta:
        print('Você acertou! Seu prêmio atual é R${0}'.format(p_acumulado[id - 1]))
    elif resposta in lista_de_erradas:
        print('Que pena! Você errou e vai sair sem nada :(')

x = produz_uma_questao(questoes, 'facil', 1)
print(x)
# ALTERAÇÃO DE COR

# Orientações de uso do format para variações de cor com ANSI:

# style: {'0':'sem estilo', '1':'negrito', '4':'sublinhado', '7':'inverter fundo com tela'}
# text: [30,37] = sequencia igual background
# background: [40,47] = [branco,vermelho, amarelo, azul, azul, magenta, ciano, ciano, cinza]

#sequencia no format: \033[style;text;back m

#exemplo de código alterando cor:

#print('{}Olá,Mundo{}, tudo bem,{} como anda?'.format('\033[1;34m','\033[1;37m', '\033[m'))

# fim