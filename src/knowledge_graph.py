
import json
import networkx as nx

class KnowledgeGraph:
    def __init__(self, json_file):
        self.G = nx.DiGraph()  # Directed graph for relations
        self.load_graph(json_file)

    def load_graph(self, json_file):
        with open(json_file, 'r') as f:
            data = json.load(f)
        for triple in data:
            self.G.add_edge(triple['concept'], triple['target'], relation=triple['relation'])

    def query_concept(self, concept):
        # Return all directly connected nodes
        if concept in self.G:
            neighbors = list(self.G.neighbors(concept))
            return neighbors
        else:
            return []

# Example usage
kg = KnowledgeGraph('data/knowledge_graph_sample.json')
print(kg.query_concept("Photosynthesis"))


"""
all info about Knowledge tree is stored here it will load json file and build a directed knowledge graph using NetworkX. """
