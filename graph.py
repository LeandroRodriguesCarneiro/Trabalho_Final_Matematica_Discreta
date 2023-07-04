import pandas as pd
import networkx as nx

from recurcive_function import encontrar_no_central, encontrar_nos_conectados

# Loading data nodes
data_nodes = pd.read_csv('csv\\fb-pages-food-nodes.csv')

# Loading data edges
data_edges = pd.read_csv('csv\\fb-pages-food-edges.csv')

def building_graph():
    # Create object graph
    graph = nx.Graph()

    # Add nodes on graph
    for _, node in data_nodes.iterrows():
        graph.add_node(node["Id"], Label=node["Label"])

    # Add edges on graph
    for _, edges in data_edges.iterrows():
        graph.add_edge(edges["Source"], edges["Target"])

    return graph

def data_graph(graph):
    # Printing data of graph
    return graph.number_of_nodes(), graph.number_of_edges()

def find_central_node(graph):
    central_node = encontrar_no_central(graph)
    return f"{data_nodes.loc[data_nodes['Id']==central_node]['Label'].to_list()[0]}",f"{data_nodes.loc[data_nodes['Id']==central_node]['Id'].to_list()[0]}"

def find_linked_nodes(graph, node_search):
    return encontrar_nos_conectados(graph,node_search)