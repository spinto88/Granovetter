import networkx as nx 
import numpy as np
import warnings

class GranovetterModel(nx.Graph):

	""" GranovetterModel. Arguments:

	n = number of agents in the system
	topology = ... of the network. 'complete' for a complete graph or 'scale-free' for a Barabasi-Albert graph with m = 2
	threshold = type of threshold distribution. 'uniform' for a uniform distribution between 0 and 1, and 'normal' for a truncated normal distribution betweeen 0 and 1. The normal distribution parameters can be passed as 'mu' and 'sigma'.
	"""

	def __init__(self, n, topology = 'complete', threshold = 'uniform', **kwargs):

		self.n = n
		# Graph initialization
		nx.Graph.__init__(self)

		# Setting network topology
		if topology == 'complete':
			nx.complete_graph(n, create_using = self)
		elif topology == 'scale-free':
			aux_graph = nx.barabasi_albert_graph(n, m = 2, seed = np.random.randint(10**5)) 
			nx.empty_graph(create_using = self)
			self.add_edges_from(aux_graph.edges())

		# Positions to network visualization 
		nodes_positions = nx.spring_layout(self)
		for node in self.nodes():
			self.node[node]['pos'] = nodes_positions[node]
            
		self.topology = topology

		self.set_nodes_threshold(threshold, **kwargs)

	def set_nodes_threshold(self, threshold, **kwargs):

		""" Threshold setting """
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

	def threshold_histogram(self, file2save = None):
        
		""" Threshold histogram: it can be used to visualize the histogram. This figure can be saved in file2save."""
		hist, edges = np.histogram([self.node[node]['threshold'] for node in self.nodes()], bins = np.arange(-0.05, 1.15, 0.1), density = True)

		import matplotlib.pyplot as plt
		plt.figure(1)
		plt.plot([(edges[i] + edges[i+1])*0.5 for i in range(len(hist))], hist, '.-', markersize = 20, alpha = 0.75)
		plt.xlabel('Threshold', size = 12)
		plt.grid(True)
		if file2save == None:
			plt.show()
		else:
			plt.savefig(file2save, dpi = 300)

	def activate_nodes(self, initial_number_of_active = 1):
        
		""" Activate a certain number of agents to start the dynamics."""
		for node in self.nodes():
			self.node[node]['active'] = False

		active_initial_nodes = np.random.choice(range(self.n), initial_number_of_active, replace = False)
		for node in active_initial_nodes:
			self.node[node]['active'] = True

	def number_of_active_nodes(self):
		""" Number of active nodes in the system """ 
		return len([node for node in self.nodes() if self.node[node]['active'] == True])

	def checkconvergence(self):
		""" Check if there is at least one non-active agent that would be able to become active. In this case, the condition of convergence is False """
		for node in self.nodes():
			active_neighbors = [True for nod in self.neighbors(node) if self.node[nod]['active'] == True]
			if (self.node[node]['threshold'] < (float(len(active_neighbors)) / self.degree(node))) and self.node[node]['active'] == False:
			return False

		return True

	def evolve(self):
		""" One step of evolution. It tries to activate all the non-active nodes """
		deactive_nodes = [node for node in self.nodes() if self.node[node]['active'] == False]
		if len(deactive_nodes) == 0:
			return 'All nodes activated'
		else:
			for step in range(len(deactive_nodes)):

				random_node = deactive_nodes[np.random.choice(range(len(deactive_nodes)))]

				active_neighbors = [True for node in self.neighbors(random_node) if self.node[node]['active'] == True]

				if (float(len(active_neighbors)) / self.degree(random_node)) > self.node[random_node]['threshold']:
					self.node[random_node]['active'] = True

			return None

	def evol2convergence(self):

		""" Evolve to convergenge: it does all the necessary steps to arrive to the final state, when no change is possible to do."""
		steps = 0
		while self.checkconvergence() == False:
			self.evolve()
			steps += 1
		return steps

	def image(self, fig, file2save = None):

		""" Image of the configuration: the fig argument is a matplotlib.pyplot figure.
		In the main file call: 
		import matplotlib.pyplot as plt

		fig = plt.figure()
		self.image(fig = fig)

		With plt.ion() ... plt.ioff() the image is displayed in an interactive way."""

		import matplotlib.pyplot as plt

		fig.clf()
		ax = fig.add_subplot(1,1,1)
        
		if self.topology == 'complete':
			nx.draw_networkx(self, pos = dict([(node, self.node[node]['pos']) for node in self.nodes()]), edgelist = [], node_size = 500, alpha = 0.5, labels = dict([(node, '{:.2f}'.format(self.node[node]['threshold'])) for node in self.nodes()]), node_color = ['b' if self.node[node]['active'] == False else 'r' for node in self.nodes()], font_size = 10)

		else:
			nx.draw_networkx(self, pos = dict([(node, self.node[node]['pos']) for node in self.nodes()]), node_size = [5 * self.degree(node) for node in self.nodes()], alpha = 0.75, node_color = ['b' if self.node[node]['active'] == False else 'r' for node in self.nodes()], width = 0.5, font_size = 10, with_labels = False)

		ax.set_xticks([])
		ax.set_yticks([])
		ax.set_title('Active nodes: {}'.format(self.number_of_active_nodes()))
		fig.canvas.draw()

		if file2save is not None:
			fig.set_size_inches(13, 13)
			fig.savefig(file2save, dpi = 300)
		else:
			plt.show()
