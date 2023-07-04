import os
import math
import itertools

from graph import building_graph,data_graph,find_central_node,find_linked_nodes

graph = building_graph()

while True:
    print('\t \
        1 - Quantos nos e arestas tem no grafo\n\t \
        2 - Encontrar no cetral do grafo\n\t \
        3 - Encontrar nos relacionados\n\t \
        4 - Simulacao de quantas paginas diferentes um usuario pode visitar\n\t \
        5 - Simulacao de quantas formas pode se formar uma comunidade\n\t \
        0 - Fechar')
    menu = int(input('Digite a opcao desejada: '))

    if(menu == 1):
        nodes,edges = data_graph(graph)
        print(f'O numero total de nos presentes no grafo: {nodes}')
        print(f'O numero total de arestas presentes no grafo: {edges}')
        input('Pressione Enter para continuar...')

    elif(menu == 2):
        label,id = find_central_node(graph)
        print(f'O no central do grafo e {label} com o id {id}')
        input('Pressione Enter para continuar...')
        
    elif(menu == 3):
        print('Os nos do grafo possuem id`s de 0 ha 619')
        node = int(input('Digite o no que deseja buscar as relacoes: '))
        linked_nodes = find_linked_nodes(graph,node)
        print(f'O no faz ligacoes com {len(linked_nodes)} outros nos segue alguns nos ao qual o no esta ligado')
        count = 0
        for i in linked_nodes:
            print(i)
            if count == 3:
                break
            count+=1
        input('Pressione Enter para continuar...')
    
    elif(menu == 4):
        n = int(input('Digite o numero de paginas exestentes na rede: '))
        k = int(input('Numero de paginas a visitar: '))

        combinations = math.comb(n, k)

        print(f"Número de combinações de {k} páginas em {n}: {combinations}")
        input('Pressione Enter para continuar...')

    elif(menu == 5):
        n = int(input('Digite o numero de paginas: '))
        k = int(input('Digite o numero de membros da comunidade: '))
        pessoas = list(range(1, n + 1))
        combinacoes = list(itertools.combinations(pessoas, k))
        print(f"Existem {len(combinacoes)} formas diferentes de formar uma comunidade de {k} membros:")
        for comunidade in combinacoes:
            print(comunidade)
        input('Pressione Enter para continuar...')

    elif(menu == 0):
        break
    os.system('cls' if os.name == 'nt' else 'clear')