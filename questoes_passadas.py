from funcoes import transforma_base

questoes = transforma_base([
{'titulo': 'Qual o resultado da operação 57 + 32?',
'nivel': 'facil',
'opcoes': {'A': '-19', 'B': '85', 'C': '89', 'D': '99'},
'correta': 'C'}, 

{'titulo': 'Qual a capital do Brasil?',
'nivel': 'facil',
'opcoes': {'A': 'Brasília', 'B': 'Rio de janeiro', 'C': 'São Paulo', 'D': 'Osasco'},
'correta': 'A'},

{'titulo': 'Quando é o feriado da Independência do Brasil?',
'nivel': 'facil',
'opcoes': {'A': '21 de Abril', 'B': '12 de Outubro', 'C': '07 de Setembro', 'D': '15 de Novembro'},
'correta': 'C'},

{'titulo': '_________ é um conjunto de particularidades que caracterizam um grupo de pessoas, uma família ou uma sociedade. É formada por princípios morais, hábitos, costumes, histórias, manifestações religiosas, entre outros. Qual palavra melhor completa o início da frase?',
'nivel': 'facil',
'opcoes': {'A': 'Missão', 'B': 'Cultura', 'C': 'Curso superior', 'D': 'Culinária'},
'correta': 'B'},

{'titulo': 'Qual destes termos menos tem relação com o fenômeno da globalização?',
'nivel': 'facil',
'opcoes': {'A': 'Aculturação', 'B': 'Neoliberalismo', 'C': 'União Europeia', 'D': 'A Terra é plana'},
'correta': 'D'},

{'titulo': 'Qual o feriado do aniversário da cidade de São Paulo?',
'nivel': 'facil',
'opcoes': {'A': '25 de Janeiro', 'B': '25 de Março', 'C': '9 de Julho', 'D': '12 de Novembro'},
'correta': 'A'},
{'titulo': 'Qual destas não é uma fruta?',
'nivel': 'facil',
'opcoes': {'A': 'Laranja', 'B': 'Maça', 'C': 'Tomate', 'D': 'Abacate'},
'correta': 'B'},
{'titulo': 'Em qual ano o TikTok atingiu 1 bilhão de usuários?',
'nivel': 'facil',
'opcoes': {'A': '2019', 'B': '2021', 'C': '2015', 'D': '2018'},
'correta': 'B'},
{'titulo': 'Qual destes não é um app com foco em streaming de vídeo?',
'nivel': 'facil',
'opcoes': {'A': 'Netflix', 'B': 'Disney Plus', 'C': 'TIDAL', 'D': 'HBO Max'},
'correta': 'C'},
{'titulo': 'Qual destes parques não se localiza em São Paulo?!',
'nivel': 'facil',
'opcoes': {'A': 'Ibirapuera', 'B': 'Parque do Carmo', 'C': 'Parque Villa Lobos', 'D': 'Morro da Urca'},
'correta': 'D'},
{'titulo': 'Qual destas não é uma linguagem de programação?',
'nivel': 'facil',
'opcoes': {'A': 'Miratdes', 'B': 'Python', 'C': 'Lua', 'D': 'C++'},
'correta': 'A'},
{'titulo': 'Dentre os listados, qual destes esportes é menos praticado no Brasil?',
'nivel': 'facil',
'opcoes': {'A': 'Natação', 'B': 'Vôlei', 'C': 'Ski Cross Country', 'D': 'Futebol'},
'correta': 'C'},
{'titulo': 'Qual o resultado da operação 5 + 2 * 3?',
'nivel': 'medio',
'opcoes': {'A': '21', 'B': '11', 'C': '30', 'D': '10'},
'correta': 'B'},

{'titulo': 'Qual destas é uma pseudociência que estuda os corpos celestes e as prováveis relações que possuem com a vida das pessoas e os acontecimentos na Terra?',
'nivel': 'medio',
'opcoes': {'A': 'Astronomia', 'B': 'Física quântica', 'C': 'Astrologia', 'D': 'Computação'},
'correta': 'C'},
	

{'titulo': 'Qual destas não foi considerada em 2007 uma das sete maravilhas do mundo moderno?',
'nivel': 'medio',
'opcoes': {'A': 'Muralha da China', 'B': 'Machu Picchu', 'C': 'Cristo Redentor', 'D': 'Torre Eiffel'},
'correta': 'D'},
	

{'titulo': 'Qual destas pessoas conduziu importantes estudos sobre radioatividade, sendo ganhadora de dois prêmios Nobel?',
'nivel': 'medio',
'opcoes': {'A': 'Marie Curie', 'B': 'Paul Erdős', 'C': 'Clive W.J. Granger', 'D': 'Maria Ressa'},
'correta': 'A'},
	

{'titulo': 'Quem é considerada a primeira pessoa programadora do mundo?!',
'nivel': 'medio',
'opcoes': {'A': 'Marie Curie', 'B': 'Alan Turing', 'C': 'Ada Lovelace', 'D': 'Edsger Dijkstra'},
'correta': 'C'},
	

{'titulo': 'Qual destes números é primo?',
'nivel': 'medio',
'opcoes': {'A': '259', 'B': '85', 'C': '49', 'D': '19'},
'correta': 'D'},
	

{'titulo': 'Na Conjectura de _______, escolhendo-se um número natural inicial n, onde n > 0, os seguintes critérios serão obedecidos: Se n for par o seu sucessor será a metade e se n for ímpar o seu sucessor será o triplo mais um, gerando então um novo número. Qual o nome da conjectura?',
'nivel': 'medio',
'opcoes': {'A': 'Collatz', 'B': 'Goldbach', 'C': 'Poincaré', 'D': 'Hodge'},
'correta': 'A'},
	

{'titulo': 'Como faço para chamar o SAMU?',
'nivel': 'medio',
'opcoes': {'A': 'Ligue 191', 'B': 'Ligue 192', 'C': 'Ligue 193', 'D': 'Ligue 190'},
'correta': 'B'},
	

{'titulo': 'Qual a segunda pessoa mais seguida no Instagram?',
'nivel': 'medio',
'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Kylie Jenner'},
'correta': 'D'},
	

{'titulo': 'Qual a pessoa mais seguida no Instagram?',
'nivel': 'medio',
'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Lionel Messi'},
'correta': 'A'},
	

{'titulo': 'A reprodução dos seres vivos é um processo biológico através do qual os organismos geram descendência. Qual desta não é uma forma de reprodução assexuada?',
'nivel': 'dificil',
'opcoes': {'A': 'Autogamia', 'B': 'Esporulação', 'C': 'Partenogênese', 'D': 'Divisão binária'},
'correta': 'A'},
	

{'titulo': 'Qual o resultado da operação 5 + 2 * 3 ^ 2, onde ^ representa potenciação?',
'nivel': 'dificil',
'opcoes': {'A': '441', 'B': '86', 'C': 'Nenhuma das outras respostas', 'D': '23'},
'correta': 'D'},
	

{'titulo': 'Quem é Oxóssi?!',
'nivel': 'dificil',
'opcoes': {'A': 'Rede de mercados', 'B': 'Tipo de poema Dissílabo', 'C': 'Divindade das religiões africanas', 'D': 'Trapper brasileiro'},
'correta': 'C'},
	

{'titulo': 'Qual a altura do Cristo Redentor?',
'nivel': 'dificil',
'opcoes': {'A': 'entre 0 e 20 metros', 'B': 'Entre 21 e 40 metros', 'C': 'Entre 41 e 60 metros', 'D': 'Mais que 60 metros'},
'correta': 'B'},
	

{'titulo': 'Em que ano faleceu Charles Babbage?',
'nivel': 'dificil',
'opcoes': {'A': '2022', 'B': '1791', 'C': '1935', 'D': '1871'},
'correta': 'A'},
	

{'titulo': 'Einstein foi Nobel de física em qual ano?',
'nivel': 'dificil',
'opcoes': {'A': '1906', 'B': '1905', 'C': '1920', 'D': '1921'},
'correta': 'D'},
	

{'titulo': 'Qual o número atômico do nitrogênio?',
'nivel': 'dificil',
'opcoes': {'A': '9', 'B': '7', 'C': '6', 'D': '8'},
'correta': 'B'},
	

{'titulo': 'Qual o ponto de fusão do nitrogênio?',
'nivel': 'dificil',
'opcoes': {'A': '120º C', 'B': '15º C', 'C': '-210º C', 'D': '-180º C'},
'correta': 'C'},
	         
{'titulo': 'Quantos gols Pelé fez oficialmente?',
'nivel': 'dificil',
'opcoes': {'A': '815', 'B': '762', 'C': '1100', 'D': '1057'},
'correta': 'B'},
	

{'titulo': 'O que é Necrose?',
'nivel': 'dificil',
'opcoes': {'A': 'Uma banda de Rock', 'B': 'Uma marca de luxo', 'C': 'Cidade Francesa', 'D': 'Morte de tecido orgânico'},
'correta': 'D'},

# 10 feitas

{'titulo': 'Qual a data de nascimento de Leonardo Davinte?',
'nivel': 'medio',
'opcoes': {'A': '15/04', 'B': '08/12', 'C': '17/09', 'D': '30/01'},
'correta': 'A'},

{'titulo': 'Qual a cor do cavalo branco de Napoleão?',
'nivel': 'medio',
'opcoes': {'A': 'Branco', 'B': 'Preto', 'C': 'Marrom', 'D': 'Nenhuma, porque ele está morto'},
'correta': 'C'},

{'titulo': 'Quantos anos durou a guerra dos cem anos?',
'nivel': 'medio',
'opcoes': {'A': '100', 'B': '99', 'C': '101', 'D': '116'},
'correta': 'D'},

{'titulo': 'Qual cor não faz parte das cores primárias?',
'nivel': 'facil',
'opcoes': {'A': 'amarelo', 'B': 'azul', 'C': 'vermelho', 'D': 'roxo'},
'correta': 'D'},

{'titulo': 'Quem descobriu o Brasil?',
'nivel': 'facil',
'opcoes': {'A': 'José Amado', 'B': 'Pedro Alveres Cabral', 'C': 'Luiz Lacerda', 'D': 'Dom Pedro'},
'correta': 'B'},

{'titulo': 'Quantos pernas a centopeia não tem?',
'nivel': 'facil',
'opcoes': {'A': '300', 'B': '320', 'C': '100', 'D': '30'},
'correta': 'C'},

{'titulo': 'pior analfabeto para Bertold Brecht:',
'nivel': 'dificil',
'opcoes': {'A': 'analfabeto funcional', 'B': 'analfabeto politico', 'C': 'analfabeto digital', 'D': 'aquele que não reconhece a própria ignorancia'},
'correta': 'B'},



{'titulo': 'quantos tipos de obras Jose de Alencar escreveu?',
'nivel': 'dificil',
'opcoes': {'A': '5', 'B': '7', 'C': '4', 'D': '3'},
'correta': 'C'},

{'titulo': 'Qual o livro de Wislawa Zsymbroska?',
'nivel': 'dificil',
'opcoes': {'A': 'Ocaso do Seculo', 'B': 'Pessoas perdidas', 'C': 'O barco que salvou', 'D': 'nenhuma das anteriores'},
'correta': 'A'},

{'titulo': 'Quem foi Miguel Bakun?',
'nivel': 'dificil',
'opcoes': {'A': 'escritor', 'B': 'sociologo', 'C': 'pintor', 'D': 'ator'},
'correta': 'C'},

# 10 questoes feitas

{'titulo': 'Qual dessas cores nao e secundaria?',
'nivel': 'facil',
'opcoes': {'A': 'amarelo', 'B': 'laranja', 'C': 'verde', 'D': 'roxo'},
'correta': 'A'},

{'titulo': 'Quanto estados o Brasil tem?',
'nivel': 'facil',
'opcoes': {'A': '25', 'B': '26', 'C': '27', 'D': '24'},
'correta': 'B'},

{'titulo': 'Qual o pais mais populoso?',
'nivel': 'facil',
'opcoes': {'A': 'Brasil', 'B': 'India', 'C': 'China', 'D': 'Russia'},
'correta': 'C'},

{'titulo': 'Quantos paises tem na africa?',
'nivel': 'medio',
'opcoes': {'A': '33', 'B': '61', 'C': '58', 'D': '54'},
'correta': 'D'},

{'titulo': 'Quantas ilhas existem?',
'nivel': 'medio',
'opcoes': {'A': '8975', 'B': '11295', 'C': '17883', 'D': '27823'},
'correta': 'C'},

{'titulo': 'O que é o zoroatrismo?',
'nivel': 'medio',
'opcoes': {'A': 'religiao', 'B': 'corrente filosofica', 'C': 'classificacao socologica', 'D': 'comportamento'},
'correta': 'A'},

{'titulo': 'Qual a cidade mais ao norte do Brasil?',
'nivel': 'dificil',
'opcoes': {'A': 'Oiapoque', 'B': 'Uiramuta', 'C': 'Chui', 'D': 'Santa Rosa'},
'correta': 'B'},

{'titulo': 'Qual a cidade mais ao sul do Brasil?',
'nivel': 'dificil',
'opcoes': {'A': 'Oiapoque', 'B': 'Uiramuta', 'C': 'Chui', 'D': 'Santa Rosa'},
'correta': 'C'},


{'titulo': 'Qual a cidade mais ao sul do mundo?',
'nivel': 'dificil',
'opcoes': {'A': 'Svalbard', 'B': 'Ushuaia', 'C': 'Puerto Williams', 'D': 'Hammerfest'},
'correta': 'C'},


{'titulo': 'Qual grau do the lean?',
'nivel': 'dificil',
'opcoes': {'A': '45', 'B': '90', 'C': '37', 'D': '48'},
'correta': 'A'}
])

