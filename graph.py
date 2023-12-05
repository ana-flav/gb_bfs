import matplotlib.pyplot as plt
import networkx as nx

def make_graph(matriz):
    linhas = matriz.strip().split('\n')
    matriz_numerica = []
    for linha in linhas:
        numeros = [int(num) for num in linha.split()]
        matriz_numerica.append(numeros)
    graph = {}
    num_linhas = len(matriz_numerica)
    for i in range(num_linhas):
        connections = []
        for j in range(len(matriz_numerica[i])):
            if matriz_numerica[i][j] != 0:
                connections.append(j+1)
        graph[i+1] = connections
    
    print('Grafo (representação de adjacências):')
    for node, connections in graph.items():
        print(f'Node {node}: {connections}')

    return graph


def plot_graph(graph):
    plt.figure()
    g = nx.Graph(graph)
    for node, connections in graph.items():
        print(f'conekd: {connections}')
        for connection in connections:
            g.add_edge(node, connection)
            
    nx.draw(g, with_labels=True, font_weight='bold', node_color='pink')
    plt.savefig('graph.png')

# TODO: Aplicar busca em largura no grafo

def bfs(graph, start):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbours = graph[node]
            for neighbour in neighbours:
                queue.append(neighbour)
    return visited

def main():
    numero = int(input('Informe um número de uma matriz que você gostaria de pegar?: '))
    with open('matriz.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        matrizes = conteudo.split('\n\n')

        for indice, matriz in enumerate(matrizes, start=1):
            if numero == indice:
                graph = make_graph(matriz)
                plot_graph(graph)
                
            else:
                print(f'Não existe matriz com o número {numero}')
                break

main()

# TODO: Criar um grafo a partir de uma matriz de adjacências
# TODO: Criar um grafo a partir de uma lista de adjacências 
