from granovetter import GranovetterModel
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(12357)

model = GranovetterModel(100, topology = 'complete', threshold = 'normal', mu = 0.6, sigma = 0.30)

model.activate_nodes(1)

model.threshold_histogram()

plt.ion()

fig = plt.figure(figsize = (13,13))

model.image(fig)

for i in range(20):
    model.evolve()
    model.image(fig)
    print 'Step {}'.format(i)

plt.ioff()

model.image(fig)


