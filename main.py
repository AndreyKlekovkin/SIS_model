import EoN
import networkx as nx
import matplotlib.pyplot as plt
# генерируем граф малого мира, с n=100 вершинами,
# Каждый узел связан с k=4 ближайшими соседями в кольцевой топологии,
# p=0.6 вероятность повторного соединения
g=nx.watts_strogatz_graph(n=100, k=4, p=0.6)
gamma = 0.2
beta = 3.2
nx_kwargs = {}
# Выполняет моделирование SIS для эпидемий в сетях с взвешенными границами или без них
# в аргумента - граф, tau=скорость передачи, gamma=скорость восстановления
sim = EoN.Gillespie_SIS(g, tau = beta, gamma=gamma, return_full_data=True)
for i in range(0,5,1):
    sim.display(time = i,  **nx_kwargs)
    plt.axis('off')
    plt.title("Iteration {}".format(i))
    plt.draw()
    plt.show()