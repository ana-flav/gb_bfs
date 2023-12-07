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
    print(len(graph))
    visatado = [False] * (len(graph)+1)  
    papi = [-1] * (len(graph)+1)  
    level = [-1] * (len(graph)+1)  
    fila = [start]
    visatado[start] = True
    level[start] = 0
    papi[start] = 0

    while fila != []:
        current = fila.pop(0)
        print(f'current: {current}')
        for neighbor in graph[current]:
            print(f'neighbor: {neighbor}')
            if not visatado[neighbor]:
                visatado[neighbor] = True
                papi[neighbor] = current
                level[neighbor] = level[current] + 1
                fila.append(neighbor)

    return papi, level

def aresta_tipo(graph, parent, level):
    conjunto = {'arestas pai': [], 'arestas irmão': [], 'arestas primo': [], 'arestas tio': []}
    for node, connections in graph.items():
        for connection in connections:
            if parent[connection] == node and level[node] == level[connection] - 1:
                if (node, connection) not in conjunto['arestas pai']:
                    conjunto['arestas pai'].append((node, connection))
                print(f'{node} -> {connection} é aresta de pai')
            elif level[node] == level[connection] and parent[node] == parent[connection]:
                if (node, connection) not in conjunto['arestas irmão']:
                    conjunto['arestas irmão'].append((node, connection))
                print(f'{node} -> {connection} é aresta de irmão')
            elif level[node] == level [connection] and parent[node] != parent[connection]:
                if (node, connection) or (connection, node) not in conjunto['arestas primo']:
                    conjunto['arestas primo'].append((node, connection))
                print(f'{node} -> {connection} é aresta de primo')
            elif level[connection] == level[node] + 1 and parent[node] != parent[connection]:
                if (node, connection) not in conjunto['arestas tio']:
                    conjunto ['arestas tio'].append((node, connection))
                print(f'{node} -> {connection} é aresta de tio')

    print(conjunto)

          

def main():
    numero = int(input('Informe um número de uma matris que você hosgtato de pegar?: '))
    with open('matriz.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        matrizes = conteudo.split('\n\n')
        print (matrizes)
        # ver se ele e conexo ou nao 
        for indice, matriz in enumerate(matrizes, start=1):
            if numero == indice:
                graph = make_graph(matriz)
                plot_graph(graph)
                
                start = int(input('Informe o nó inicial: '))
                parent, level = bfs(graph, start)
                print(f'Parent: {parent}')
                print(f'Level: {level}')
                aresta_tipo(graph, parent, level)
               
main()

# TODO: Criar um grafo a partir de uma matriz de adjacências
# TODO: Criar um grafo a partir de uma lista de adjacências 
