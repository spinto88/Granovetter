import cPickle as pk
import matplotlib.pyplot as plt
import numpy as np


data = pk.load(file('Data.pk','r'))

mu = np.arange(0.00, 1.01, 0.10)
sigma = np.arange(0.00, 1.01, 0.10)

plt.figure(1)
plt.axes([0.20, 0.15, 0.70, 0.75])
for m in [mu[0], mu[4], mu[8]]:

    data2plot = []

    for s in sigma:

        data2plot.append(np.mean([d[2] for d in data if d[0] == m and d[1] == s]))

    plt.plot(sigma, data2plot, '.-', markersize = 20, label = '$\mu$ = {}'.format(m), linewidth = 3, alpha = 0.75)

plt.yticks(size = 15)
plt.xticks(size = 15)
plt.grid(True, alpha = 0.25)
plt.xlabel('$\sigma$', size = 20)
plt.ylabel('Riot size', size = 15)
plt.xlim([-0.10, 1.10])
plt.ylim([-50, 1050])
plt.title('N = 1000', size = 15)
plt.legend(loc = 'best', fontsize = 12)
plt.savefig('Function_of_sigma.png', dpi = 600)

plt.figure(2)
plt.axes([0.20, 0.15, 0.70, 0.75])
for s in [sigma[0], sigma[4], sigma[8]]:

    data2plot = []

    for m in mu:

        data2plot.append(np.mean([d[2] for d in data if d[0] == m and d[1] == s]))

    plt.plot(mu, data2plot, '.-', markersize = 20, label = '$\sigma$ = {}'.format(s), linewidth = 3, alpha = 0.75)

plt.yticks(size = 15)
plt.xticks(size = 15)
plt.grid(True, alpha = 0.25)
plt.xlabel('$\mu$', size = 20)
plt.ylabel('Riot size', size = 15)
plt.xlim([-0.10, 1.10])
plt.ylim([-50, 1050])
plt.legend(loc = 'best', fontsize = 12)
plt.title('N = 1000', size = 15)
plt.savefig('Function_of_mu.png', dpi = 600)

plt.show()



