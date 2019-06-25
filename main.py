from granovetter import GranovetterModel
import matplotlib.pyplot as plt
import numpy as np

# Random seed setted
np.random.seed(123578)

# Model parameters
n = 400 # Number of agents in the system.
topology = 'complete' # 'complete' or 'scale-free'. This last one is a Barabasi-Albert scale-free network with m = 2. 
threshold = 'normal' # Threshold distribution. 'uniform' or truncated 'normal' with 'mu' and 'sigma' that can be also passed to the function.
mu = 0.5
sigma = 0.6

# Model definition
model = GranovetterModel(n = n, topology = topology, threshold = threshold, mu = mu, sigma = sigma)

thresholds = sorted([model.node[node]['threshold'] for node in model.nodes])

proba_dist = lambda x: np.float(len([t for t in thresholds if t < x]))/len(thresholds)

plt.plot(np.arange(0.00, 1.05, 0.05), [proba_dist(x) for x in np.linspace(0.00, 1.05,21)], '-')
plt.plot(np.arange(0.00, 1.05, 0.05), np.arange(0.00, 1.05, 0.05))
plt.show()

initial_number_of_active_agents = 300

number_of_iterations = 100 # Evolution steps

# Model definition
model = GranovetterModel(n = n, topology = topology, threshold = threshold, mu = mu, sigma = sigma)

# Activate random nodes
model.activate_nodes(initial_number_of_active_agents)

# Show the threshold distribution histogram
model.threshold_histogram()

# Activate the matplotlib interactive mode
plt.ion()
fig = plt.figure(figsize = (13,13))

# Show the system
#model.image(fig)

for i in range(number_of_iterations):
	# Make one iteration and show the system
	model.evolve()
#	model.image(fig)
	print 'Step {} - Active agents {}'.format(i, np.float(model.number_of_active_nodes())/n)

#plt.ioff()

# Show the system
#model.image(fig)

# Save the final state
# fig = plt.figure()
# model.image(fig, 'Conf_final.png')


