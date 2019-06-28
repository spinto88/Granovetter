from granovetter import GranovetterModel
import matplotlib.pyplot as plt
import numpy as np

# Random seed setted
np.random.seed(123575)

# Model parameters
n = 1000 # Number of agents in the system.
topology = 'complete' # 'complete' or 'scale-free'. This last one is a Barabasi-Albert scale-free network with m = 2. 
threshold = 'normal' # Threshold distribution. 'uniform' or truncated 'normal' with 'mu' and 'sigma' that can be also passed to the function.
mu = 0.5
sigma = 1.00/4

# Model definition
model = GranovetterModel(n = n, topology = topology)

for mu in [0.5]:#, 0.2, 0.4, 0.6, 0.8, 1.0]:

    for sigma in [0.25]:#, 0.2, 0.4, 0.6, 0.8, 1.0]:

        thresholds = []

        for i in range(100):

            model.set_nodes_threshold(threshold = 'normal', mu = mu, sigma = sigma)
            thresholds += [model.node[node]['threshold'] for node in model.nodes]

        thresholds = sorted(thresholds)

        proba_dist = lambda x: np.float(len([t for t in thresholds if t <= x]))/len(thresholds)

	plt.figure(1)
	plt.clf()
        plt.axes([0.15, 0.15, 0.75, 0.75])
        plt.plot(np.arange(0.00, 1.01, 0.01), [proba_dist(x) for x in np.arange(0.00, 1.01, 0.01)], '-', linewidth = 3, alpha = 0.75, label = 'Threshold distribution')
        plt.plot(np.arange(0.00, 1.01, 0.01), np.arange(0.00, 1.01, 0.01), '-', label = 'Identity function', linewidth = 3, alpha = 0.75)
        plt.grid(True, alpha = 0.25)
        plt.xlim([-0.05, 1.05])
        plt.ylim([-0.05, 1.05])
        plt.xticks(size = 15)
        plt.yticks(size = 15)
        plt.xlabel('Active agents', size = 15)
        plt.legend(loc = 'best', fontsize = 12)
        plt.title('Truncated normal $\mu$ = {} $\sigma$ = {:.3f}'.format(mu, sigma), size = 12)
        plt.savefig('Threshold_truncated_mu{:.3f}_sigma{:.3f}.png'.format(mu, sigma), dpi = 300)
	plt.show()

