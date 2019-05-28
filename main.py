from granovetter import GranovetterModel

model = GranovetterModel(25, threshold = 'normal', mu = 0.3, sigma = 0.50)

model.activate_nodes(1)

model.image()

print model.number_of_active_nodes()

model.evol2convergence()

print model.number_of_active_nodes()

model.image()

