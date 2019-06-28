from granovetter import GranovetterModel
import matplotlib.pyplot as plt
import numpy as np
import cPickle as pk

# Random seed setted
np.random.seed(123575)

# Model parameters
n = 1000 # Number of agents in the system.
topology = 'complete' # 'complete' or 'scale-free'. This last one is a Barabasi-Albert scale-free network with m = 2. 
threshold = 'uniform' # Threshold distribution. 'uniform' or truncated 'normal' with 'mu' and 'sigma' that can be also passed to the function.

# Model definition
model = GranovetterModel(n = n, topology = topology)

mu = 0.5
sigma = 1.00/3

data2plot = []
deviation = []

for inaa in [1, 100, 250, 500, 750, 1000]:

    data = []

    for iteration in range(50):

        # Model definition
        model.set_nodes_threshold(threshold = threshold, mu = mu, sigma = sigma)

        # Activate random nodes
        model.activate_nodes(inaa)
        model.evol2convergence()

        data.append(model.number_of_active_nodes())

    data2plot.append(np.mean(data))
    deviation.append(np.std(data))

plt.axes([0.15, 0.15, 0.75, 0.75])
plt.errorbar([1, 100, 250, 500, 750, 1000], data2plot, deviation, fmt = '.-', markersize = 20, linewidth = 3, alpha = 0.75)
plt.plot([1, 100, 250, 500, 750, 1000], [1, 100, 250, 500, 750, 1000], '-', linewidth = 3, alpha = 0.75, label = 'Identity function')
plt.grid(True, alpha = 0.25)
plt.xlabel('Initial number of active agents', size = 15)
plt.ylabel('Riot size', size = 15)
plt.xticks(size = 15)
plt.yticks(size = 15)
plt.xlim([0, 1050])
plt.ylim([0, 1050])
#plt.title('Truncated normal $\mu = {}$ $\sigma = {:.3f}$'.format(0.5, sigma), size = 15)
#plt.savefig('RiotSize_mu{}_sigma{:.3f}.png'.format(0.5, sigma), dpi = 300)
plt.legend(loc = 'best', fontsize = 12)
plt.title('Uniform', size = 15)
plt.savefig('RiotSize_uniform.png',dpi = 300)
plt.show()
