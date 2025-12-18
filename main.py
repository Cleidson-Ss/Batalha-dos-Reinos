# Batalha entre Reinos
# Disc: Estrutura de Dados
# Profa. Viviane Araújo
# Alunos: Cleidson Silva / Ivaldo Dantas

import random

# ==========================================================
# LISTA ENCADEADA – HISTÓRICO DA BATALHA
# ==========================================================

class No: # Define a classe para um nó da Lista Encadeada.
    def __init__(self, acao): # Método construtor que recebe a string de ação/evento.
        self.acao = acao # Armazena a string da ação (o dado do nó).
        self.proximo = None # Inicializa a referência para o próximo nó como None.


class ListaEncadeada: # Define a classe para a estrutura de Lista Encadeada.
    def __init__(self): # Método construtor.
        self.inicio = None # Inicializa a cabeça/início da lista como None (lista vazia).

    def adicionar(self, acao): # Método para adicionar um novo evento/ação no final da lista.
        novo = No(acao) # Cria um novo objeto No com a ação fornecida.
        if not self.inicio: # Verifica se a lista está vazia.
            self.inicio = novo # Se estiver vazia, o novo nó se torna o início.
        else: # Se a lista não estiver vazia:
            atual = self.inicio # Começa a percorrer a lista a partir do início.
            while atual.proximo: # Loop que continua enquanto houver um próximo nó.
                atual = atual.proximo # Move o ponteiro 'atual' para o próximo nó.
            atual.proximo = novo # O último nó da lista aponta para o novo nó.

    def limpar(self): # Método para redefinir a lista.
        self.inicio = None # Define o início como None, apagando todos os nós.

    def gerar_texto(self): # Método para converter todo o histórico em uma única string formatada.
        texto = "" # Inicializa uma string vazia para armazenar o histórico.
        atual = self.inicio # Começa a percorrer a lista a partir do início.
        while atual: # Loop que continua enquanto 'atual' não for None.
            texto += "• " + atual.acao + "\n" # Adiciona a ação do nó atual, formatada com um bullet point, à string.
            atual = atual.proximo # Move o ponteiro 'atual' para o próximo nó.
        return texto # Retorna a string completa do histórico.


historico = ListaEncadeada() # Cria uma instância da ListaEncadeada para armazenar o histórico de batalhas.

# ==========================================================
# REINOS (DICIONÁRIO)
# ==========================================================

personagens = { # Define um dicionário onde as chaves são os nomes dos reinos (strings).
    "Reino do Fogo": {"vida": 120, "ataque": 25, "defesa": 10, "moedas": 0}, # Sub-dicionário com atributos do Reino do Fogo.
    "Reino da Água": {"vida": 100, "ataque": 20, "defesa": 15, "moedas": 0}, # Sub-dicionário com atributos do Reino da Água.
    "Reino da Terra": {"vida": 150, "ataque": 15, "defesa": 20, "moedas": 0}, # Sub-dicionário com atributos do Reino da Terra.
    "Reino dos Céus": {"vida": 80, "ataque": 30, "defesa": 5, "moedas": 0}, # Sub-dicionário com atributos do Reino dos Céus.
}

# ==========================================================
# ÁRVORE BINÁRIA – CÁLCULO DE DANO
# ==========================================================

class NoArvore: # Define a classe para um nó da Árvore Binária.
    def __init__(self, valor, esq=None, dir=None): # Construtor com valor e referências opcionais para esquerda e direita.
        self.valor = valor # Armazena o valor do nó (e.g., "calculo", "ataque", "defesa").
        self.esq = esq # Referência para o nó filho esquerdo.
        self.dir = dir # Referência para o nó filho direito.


arvore_dano = NoArvore( # Cria a raiz da Árvore Binária, que representa o cálculo.
    "calculo", # Valor da raiz.
    NoArvore("ataque"), # Nó filho esquerdo (representa o valor de Ataque).
    NoArvore("defesa") # Nó filho direito (representa o valor de Defesa).
)


def calcular_dano(atacante, defensor, no): # Função recursiva para calcular o dano usando a árvore.
    if no is None: # Caso base: se o nó for nulo, retorna 0.
        return 0

    if no.valor == "ataque": # Se o nó for "ataque", retorna o valor de ataque do atacante.
        return personagens[atacante]["ataque"]

    if no.valor == "defesa": # Se o nó for "defesa", retorna o valor de defesa do defensor.
        return personagens[defensor]["defesa"]

    esquerda = calcular_dano(atacante, defensor, no.esq) # Chamada recursiva para calcular o valor do sub-ramo esquerdo (ataque).
    direita = calcular_dano(atacante, defensor, no.dir) # Chamada recursiva para calcular o valor do sub-ramo direito (defesa).

    return max(1, esquerda - direita) # Retorna o dano: o Ataque menos a Defesa, garantindo um mínimo de 1 de dano.

# ==========================================================
# HEAPSORT – RANKING POR VIDA
# ==========================================================

def heapify(arr, n, i): # Função auxiliar para manter a propriedade de Max Heap.
    maior = i # Inicializa o maior como a raiz (i).
    e = 2 * i + 1 # Índice do filho esquerdo.
    d = 2 * i + 2 # Índice do filho direito.

    # O código utiliza a vida (índice 1 da tupla `(nome, vida)`) para comparação:
    if e < n and arr[e][1] > arr[maior][1]: # Se o filho esquerdo for maior que a raiz (comparando o valor da vida).
        maior = e # Atualiza o índice do maior.

    if d < n and arr[d][1] > arr[maior][1]: # Se o filho direito for maior que o atual maior (comparando o valor da vida).
        maior = d # Atualiza o índice do maior.

    if maior != i: # Se o maior não for a raiz:
        arr[i], arr[maior] = arr[maior], arr[i] # Troca a raiz com o maior elemento.
        heapify(arr, n, maior) # Chama heapify recursivamente na sub-árvore afetada.


def heapsort(lista): # Função principal do algoritmo Heapsort.
    n = len(lista) # Obtém o tamanho da lista (número de reinos).

    # Constrói o Max Heap (reorganiza a lista):
    for i in range(n // 2 - 1, -1, -1): # Loop de trás para frente, começando do último nó não folha.
        heapify(lista, n, i) # Aplica heapify em todos os sub-heaps.
    
    # 

    # Extrai elementos um por um do heap:
    for i in range(n - 1, 0, -1): # Loop de trás para frente (do final da lista até o segundo elemento).
        lista[i], lista[0] = lista[0], lista[i] # Move a raiz (maior elemento) para o final da sub-lista não ordenada.
        heapify(lista, i, 0) # Chama heapify no heap restante (tamanho 'i').

    lista.reverse() # Inverte a lista para obter o ranking em ordem decrescente (do maior para o menor).
    return lista # Retorna a lista ordenada.

# ==========================================================
# COMPRA DE VIDA
# ==========================================================

def comprar_vida(reino): # Função para permitir que um reino compre vida usando moedas.
    moedas = personagens[reino]["moedas"] # Obtém o saldo de moedas do reino.
    print(f"\n{reino} possui {moedas} moeda(s). 1 moeda = +25 vida") # Informa o saldo e o custo.

    escolha = input("Comprar vida? (1 = sim, 0 = não): ") # Pede a entrada do usuário.

    if escolha == "1": # Se o usuário escolheu comprar:
        if moedas >= 1: # Verifica se o reino tem moedas suficientes (pelo menos 1).
            personagens[reino]["vida"] += 25 # Aumenta a vida do reino em 25.
            personagens[reino]["moedas"] -= 1 # Diminui o saldo de moedas em 1.
            print("Vida comprada com sucesso!")
        else:
            print("Moedas insuficientes!") # Mensagem de erro se não tiver moedas.
    else:
        print("Compra cancelada.") # Mensagem se o usuário não quiser comprar.

# ==========================================================
# BATALHA
# ==========================================================

def batalha_rapida(r1, r2): # Função que simula uma única rodada de batalha entre dois reinos.
    historico.limpar() # Limpa o histórico anterior, pois este é um log de batalha rápida.

    print(f"\n🔥 Batalha: {r1} vs {r2}") # Imprime o título da batalha.

    atacante, defensor = random.sample([r1, r2], 2) # Escolhe aleatoriamente quem ataca e quem defende.

    dano = calcular_dano(atacante, defensor, arvore_dano) # Calcula o dano usando a Árvore Binária.
    personagens[defensor]["vida"] -= dano # Reduz a vida do defensor pelo valor do dano.

    historico.adicionar(f"{atacante} atacou {defensor} causando {dano} de dano.") # Registra o ataque no histórico.
    historico.adicionar(f"{defensor} ficou com {personagens[defensor]['vida']} de vida.") # Registra a vida restante do defensor.

    vencedor = atacante # Define o atacante como o vencedor da rodada.
    perdedor = defensor # Define o defensor como o perdedor da rodada.

    personagens[vencedor]["moedas"] += 1 # O vencedor ganha 1 moeda.
    personagens[perdedor]["moedas"] += max(1, dano // 10) # O perdedor ganha moedas baseadas no dano sofrido (no mínimo 1/10 do dano, ou 1).

    historico.adicionar(f"{vencedor} venceu a batalha!") # Registra a vitória.

    print(f"🏆 {vencedor} venceu!") # Imprime o vencedor.
    return vencedor # Retorna o nome do reino vencedor.

# ==========================================================
# LISTAR REINOS
# ==========================================================

def listar_reinos(): # Função para exibir os atributos atuais de todos os reinos.
    print("\n--- REINOS ---")
    for nome, dados in personagens.items(): # Itera sobre os itens do dicionário 'personagens'.
        print(f"{nome} | Vida: {dados['vida']} | Atq: {dados['ataque']} | Def: {dados['defesa']} | Moedas: {dados['moedas']}") # Imprime os dados formatados.

# ==========================================================
# MENU
# ==========================================================

def menu(): # Função principal que implementa o loop do menu do jogo.
    while True: # Loop infinito do menu.
        print("\n=== BATALHA ENTRE REINOS ===") # Título do menu.
        print("1 - Listar reinos") # Opção 1.
        print("2 - Iniciar batalha") # Opção 2.
        print("3 - Mostrar ranking") # Opção 3.
        print("4 - Comprar vida") # Opção 4.
        print("5 - Ver histórico") # Opção 5.
        print("6 - Sair") # Opção 6 para sair.

        op = input("Escolha: ") # Solicita a entrada do usuário.

        if op == "1": # Se a opção for 1:
            listar_reinos() # Chama a função para listar os reinos.

        elif op == "2": # Se a opção for 2:
            listar_reinos() # Lista os reinos para ajudar na escolha.
            r1 = input("Primeiro reino: ") # Pede o nome do primeiro reino.
            r2 = input("Segundo reino: ") # Pede o nome do segundo reino.

            if r1 in personagens and r2 in personagens and r1 != r2: # Valida se os reinos existem e são diferentes.
                batalha_rapida(r1, r2) # Inicia a batalha.
            else:
                print("Reinos inválidos!") # Mensagem de erro se a validação falhar.

        elif op == "3": # Se a opção for 3:
            # Cria uma lista de tuplas [(nome_reino, vida)] a partir do dicionário.
            ranking = heapsort([(k, v["vida"]) for k, v in personagens.items()]) 
            print("\n--- Ranking por Vida ---")
            for r in ranking: # Itera sobre a lista de ranking ordenada pelo Heapsort.
                print(f"{r[0]} — {r[1]}") # Imprime o nome do reino e sua vida.

        elif op == "4": # Se a opção for 4:
            listar_reinos() # Lista os reinos para ajudar na escolha.
            reino = input("Escolha o reino: ") # Pede o nome do reino.
            if reino in personagens: # Verifica se o reino é válido.
                comprar_vida(reino) # Chama a função de compra de vida.

        elif op == "5": # Se a opção for 5:
            texto = historico.gerar_texto() # Obtém o histórico formatado da Lista Encadeada.
            print(texto if texto else "Nenhuma batalha registrada.") # Imprime o histórico ou uma mensagem de vazio.

        elif op == "6": # Se a opção for 6:
            print("Saindo...")
            break # Sai do loop while e encerra o programa.

        else: # Para qualquer outra entrada:
            print("Opção inválida.") # Mensagem de opção inválida.

# ==========================================================
# EXECUÇÃO
# ==========================================================

menu() # Chama a função menu para iniciar a execução do jogo.