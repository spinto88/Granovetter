from granovetter import GranovetterModel
import matplotlib.pyplot as plt
import numpy as np
import cPickle as pk

# Random seed setted
np.random.seed(123575)

# Model parameters
n = 1000 # Number of agents in the system.
topology = 'complete' # 'complete' or 'scale-free'. This last one is a Barabasi-Albert scale-free network with m = 2. 
threshold = 'normal' # Threshold distribution. 'uniform' or truncated 'normal' with 'mu' and 'sigma' that can be also passed to the function.

# Model definition
model = GranovetterModel(n = n, topology = topology)

data = []
for mu in np.arange(0.00, 1.01, 0.10):

	for sigma in np.arange(0.00, 1.01, 0.10):

	    for iteration in range(10):

		# Model definition
		model.set_nodes_threshold(threshold = threshold, mu = mu, sigma = sigma)

		initial_number_of_active_agents = 1

		# Activate random nodes
		model.activate_nodes(initial_number_of_active_agents)
		model.evol2convergence()

		print '{},{},{}'.format(mu, sigma, model.number_of_active_nodes())
		data.append([mu, sigma, model.number_of_active_nodes()])

pk.dump(data, file('Data.pk','w'))
