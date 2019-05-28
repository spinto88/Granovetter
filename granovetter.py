import networkx as nx 
import numpy as np
import warnings

class GranovetterModel(nx.Graph):

    def __init__(self, n, topology = 'complete', threshold = 'uniform', **kwargs):

        self.n = n

        nx.Graph.__init__(self)

        if topology == 'complete':
            nx.complete_graph(n, create_using = self)

        nodes_positions = nx.spring_layout(self)
        for node in self.nodes():
             self.node[node]['pos'] = nodes_positions[node]
            
        self.topology = topology

        self.set_nodes_threshold(threshold, **kwargs)

    def set_nodes_threshold(self, threshold, **kwargs):

        for node in self.nodes():
            if threshold == 'uniform':
                self.node[node]['threshold'] = np.random.random()
            elif threshold == 'normal':
                self.node[node]['threshold'] = np.random.normal(loc = kwargs['mu'], scale = kwargs['sigma'])
                if self.node[node]['threshold'] < 0.00:
                    self.node[node]['threshold'] = 0.00
                elif self.node[node]['threshold'] > 1.00:
                    self.node[node]['threshold'] = 1.00
                else:
                    pass

    def threshold_histogram(self):

        hist, edges = np.histogram([self.node[node]['threshold'] for node in self.nodes()], \
                                       bins = np.arange(-0.05, 1.05, 0.1), density = True)

        import matplotlib.pyplot as plt
        plt.figure(1)
        plt.plot([(edges[i] + edges[i+1])*0.5 for i in range(len(hist))], hist, '.-', markersize = 20, alpha = 0.5)
        plt.grid(True)
        plt.show()

    def activate_nodes(self, initial_number_of_active = 1):

        for node in self.nodes():
            self.node[node]['active'] = False

        active_initial_nodes = np.random.choice(range(self.n), initial_number_of_active, replace = False)
        for node in active_initial_nodes:
            self.node[node]['active'] = True

    def number_of_active_nodes(self):

        return len([node for node in self.nodes() if self.node[node]['active'] == True])

    def checkconvergence(self):

        for node in self.nodes():
            active_neighbors = [True for nod in self.neighbors(node) if self.node[nod]['active'] == True]
            if (self.node[node]['threshold'] < (float(len(active_neighbors)) / self.degree(node))) and self.node[node]['active'] == False:
                return False
        return True

    def evolve(self, steps = 1):

        for step in range(steps):

            deactive_nodes = [node for node in self.nodes() if self.node[node]['active'] == False]
            if len(deactive_nodes) == 0:
                break

            random_node = deactive_nodes[np.random.choice(range(len(deactive_nodes)))]

            active_neighbors = [True for node in self.neighbors(random_node) if self.node[node]['active'] == True]

            if (float(len(active_neighbors)) / self.degree(random_node)) >= self.node[random_node]['threshold']:
                self.node[random_node]['active'] = True

    def evol2convergence(self):

        steps = 0
        while self.checkconvergence() == False:
            self.evolve(100)
            steps += 100
        return steps

    def image(self):

        import matplotlib.pyplot as plt

        plt.figure(figsize = (13, 13))

        if self.topology == 'complete':
            nx.draw_networkx(self, pos = dict([(node, self.node[node]['pos']) for node in self.nodes()]), \
		edgelist = [], node_size = 500, alpha = 0.5, \
		labels = dict([(node, '{:.2f}'.format(self.node[node]['threshold'])) for node in self.nodes()]),\
		node_color = ['b' if self.node[node]['active'] == False else 'r' for node in self.nodes()],\
                font_size = 10)

        plt.show()


