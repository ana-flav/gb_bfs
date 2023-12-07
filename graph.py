import matplotlib.pyplot as plt
import networkx as nx
import os

def construir_grafo(matriz):
    linhas = matriz.strip().split('\n')
    matriz_numerica = []
    for linha in linhas:
        numeros = [int(num) for num in linha.split()]
        matriz_numerica.append(numeros)
    grafo = {}
    num_linhas = len(matriz_numerica)
    for i in range(num_linhas):
        adjacentes = []
        for j in range(len(matriz_numerica[i])):
            if matriz_numerica[i][j] != 0:
                adjacentes.append(j+1)
        grafo[i+1] = adjacentes
    return grafo

def plot_grafo(grafo):
    plt.figure()
    g = nx.Graph(grafo)
    for no, adjacentes in grafo.items():
        for adjacente in adjacentes:
            g.add_edge(no, adjacente)
            
    nx.draw(g, with_labels=True, font_weight='bold', node_color='pink')
    plt.savefig('graph.png')

def bfs(grafo, raiz):
    visitado = [False] * (len(grafo)+1)  
    pai = [-1] * (len(grafo)+1)  
    nivel = [-1] * (len(grafo)+1)  
    fila = [raiz]
    visitado[raiz] = True
    nivel[raiz] = 0
    pai[raiz] = 0
    largura = [0] * (len(grafo)+1)
    i = 0
    
    while fila != []:
        i += 1
        atual = fila.pop(0)
        for vizinho in grafo[atual]:
            if not visitado[vizinho]:
                visitado[vizinho] = True
                pai[vizinho] = atual
                nivel[vizinho] = nivel[atual] + 1
                fila.append(vizinho)
       
        largura[i] = atual
        print(f'largura: {largura}')
    return pai, nivel

def aresta_tipo(grafo, pai, nivel):
    conjunto = {'arestas pai': [], 'arestas irmão': [], 'arestas primo': [], 'arestas tio': []}
    
    for no, adjacentes in grafo.items():
        for adjacente in adjacentes:
            if pai[adjacente] == no and nivel[no] == nivel[adjacente] - 1:
                if (no, adjacente) not in conjunto['arestas pai'] and (adjacente, no) not in conjunto['arestas pai']:
                    conjunto['arestas pai'].append((no, adjacente))
            elif nivel[no] == nivel[adjacente] and pai[no] == pai[adjacente]:
                if (no, adjacente) not in conjunto['arestas irmão'] and (adjacente, no) not in conjunto['arestas irmão']:
                    conjunto['arestas irmão'].append((no, adjacente))
            elif nivel[no] == nivel [adjacente] and pai[no] != pai[adjacente]:
                if (no, adjacente) not in conjunto['arestas primo'] and (adjacente, no) not in conjunto['arestas primo']:
                    conjunto['arestas primo'].append((no, adjacente))
            elif nivel[adjacente] == nivel[no] + 1 and pai[no] != pai[adjacente]:
                if (no, adjacente) not in conjunto['arestas tio'] and (adjacente, no) not in conjunto['arestas tio']:
                    conjunto['arestas tio'].append((no, adjacente))
                    
    if conjunto['arestas irmão'] == [] and conjunto['arestas primo'] == []:
        print('é bipartido')
    else:
        print(f'Não é bipartido pois tem arestas de irmão {conjunto["arestas irmão"]} ou primo {conjunto["arestas primo"]}')
       
    print(conjunto)

def main():

    with open('matriz.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        matrizes = conteudo.split('\n\n')
    
    print(conteudo)
    print(f"\nForam carregadas {len(matrizes)} matrizes.")
    numero = int(input(f"Informe a matriz que você gostaria de manipular de 1 a {len(matrizes)}: "))


    for indice, matriz in enumerate(matrizes, start=1):
        if numero == indice:
            grafo = construir_grafo(matriz)
            plot_grafo(grafo)
            print("Os vértices são: ", list(grafo.keys()))

    op = 0
    opcoes = [1, 2, 3]
    while(op not in opcoes):
        op = int(input('''\n\n---------------------------------------------------------
            \nDigite a opção desejada:
            \n---------------------------------------------------------
            \n1|Verificar se o grafo é conexo
            \n2|Aplicar busca em largura
            \n3|Encontrar bipartição
            \n---------------------------------------------------------
            \nOpção escolhida: '''))
        
    if op == 1:
        print("Inserir aqui função que verifica se o grafo é conexo")

    elif op == 2:
        raiz = int(input('Informe o nó raiz: '))
        pai, nivel = bfs(grafo, raiz)
        aresta_tipo(grafo, pai, nivel)

    else:
        print("Inserir aqui função de encontrar bipartição")
        

               
main()

# TODO: Criar um grafo a partir de uma matriz de adjacências
# TODO: Criar um grafo a partir de uma lista de adjacências 
