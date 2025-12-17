🏰 Batalha dos Reinos ⚔️
Projeto desenvolvido para atender critérios aprendidos durante a cadeira de Estrutura de Dados no IFPE.

Este é um jogo de simulação de batalha baseado em console, desenvolvido em Python, que utiliza diversas estruturas de dados para gerenciar o estado do jogo, calcular o dano e manter o histórico.

📜 Estruturas de Dados Utilizadas
O código implementa e utiliza as seguintes estruturas de dados para as funcionalidades principais:

1.	Lista Encadeada (Histórico):
	Classe: No, ListaEncadeada
	Função: Armazena o registro de cada ação e resultado das batalhas em ordem cronológica, permitindo a visualização do histórico.

2.	Dicionário (Reinos):
	Variável: personagens
	Função: Armazena os atributos (vida, ataque, defesa, moedas) de cada reino de forma eficiente, permitindo acesso rápido pelas chaves (nomes dos reinos).

3.	Árvore Binária (Cálculo de Dano):
	Classes: NoArvore
	Variável: arvore_dano
	Função: Estrutura o cálculo de dano como uma operação hierárquica. O cálculo é feito percorrendo a árvore, onde o dano final é $\max(1, \text{Ataque} - \text{Defesa})$.

4.	Heapsort (Ranking):
	Funções: heapify, heapsort
	Função: É utilizado para classificar os reinos com base na sua pontuação de vida atual, gerando um ranking ordenado.

⚙️ Funcionalidades

O jogo oferece as seguintes opções no menu principal:
•	1 - Listar reinos: Exibe o nome de cada reino, seus atributos atuais (Vida, Ataque, Defesa) e a quantidade de Moedas.

•	2 - Iniciar batalha: Permite escolher dois reinos para um combate rápido.
	Um reino é escolhido aleatoriamente como atacante e o outro como defensor.
	O dano é calculado usando a Árvore Binária.
	O reino perdedor tem sua vida reduzida pelo dano.
	O vencedor ganha 1 moeda, e o perdedor ganha moedas baseadas no dano sofrido ($\max(1, \text{Dano} // 10)$).
	O histórico da batalha é registrado na Lista Encadeada.

•	3 - Mostrar ranking: Classifica e exibe os reinos do maior para o menor valor de vida usando o algoritmo Heapsort.

•	4 - Comprar vida: Permite que um reino gaste 1 moeda para aumentar sua vida em +25.

•	5 - Ver histórico: Exibe o log completo de todas as batalhas e ações registradas na Lista Encadeada.

•	6 - Sair: Encerra o programa.

🚀 Como Executar
1.	Certifique-se de ter o Python 3 instalado em sua máquina.
2.	Salve o código como batalha_dos_reinos.py.
3.	Abra o terminal ou prompt de comando.
4.	Navegue até o diretório onde você salvou o arquivo.
5.	Execute o jogo com o comando:
