from granovetter import GranovetterModel
import matplotlib.pyplot as plt
import numpy as np

# Random seed setted
np.random.seed(12357)

# Model parameters
n = 400 # Number of agents in the system.
topology = 'scale-free' # 'complete' or 'scale-free'. This last one is a Barabasi-Albert scale-free network with m = 2. 
threshold = 'normal' # Threshold distribution. 'uniform' or truncated 'normal' with 'mu' and 'sigma' that can be also passed to the function.
mu = 0.2
sigma = 0.4

initial_number_of_active_agents = 1

number_of_iterations = 10 # Evolution steps

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
model.image(fig)

for i in range(number_of_iterations):
	# Make one iteration and show the system
	model.evolve()
	model.image(fig)
	print 'Step {} - Active agents {}'.format(i, model.number_of_active_nodes())

plt.ioff()

# Show the system
model.image(fig)

# Save the final state
# fig = plt.figure()
# model.image(fig, 'Conf_final.png')


