from granovetter import GranovetterModel
import matplotlib.pyplot as plt
import numpy as np

# Random seed setted
np.random.seed(123575)

# Model parameters
n = 100 # Number of agents in the system.
topology = 'complete' # 'complete' or 'scale-free'. This last one is a Barabasi-Albert scale-free network with m = 2. 
threshold = 'normal' # Threshold distribution. 'uniform' or truncated 'normal' with 'mu' and 'sigma' that can be also passed to the function.
mu = 0.6
sigma = 0.4

# Model definition
model = GranovetterModel(n = n, topology = topology, threshold = threshold, mu = mu, sigma = sigma)

initial_number_of_active_agents = 1

#number_of_iterations = 100 # Evolution steps

# Activate random nodes
model.activate_nodes(initial_number_of_active_agents)
number_of_iterations = 40
# Show the threshold distribution histogram
#model.threshold_histogram()

# Activate the matplotlib interactive mode
#plt.ion()
fig = plt.figure(figsize = (13,13))

# Show the system
#model.image(fig)


for i in range(number_of_iterations):
	# Make one iteration and show the system
	model.image(fig, 'Conf{}.png'.format(i))
	model.evolve()


