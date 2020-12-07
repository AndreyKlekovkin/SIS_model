from EoN import *
import matplotlib.pyplot as plt

class TestSample:
    def test_SIS_simulations(self):
        g = nx.watts_strogatz_graph(n=24, k=4, p=0.6)
        gamma = 0.2
        beta = 3.2
        nx_kwargs = {}
        # Выполняет моделирование SIS для эпидемий в сетях с взвешенными границами или без них
        # в аргумента - граф, tau=скорость передачи, gamma=скорость восстановления
        sim = EoN.Gillespie_SIS(g, tau=beta, gamma=gamma, return_full_data=True)
        for i in range(0, 5, 1):
            sim.display(time=i, **nx_kwargs)
            plt.axis('off')
            plt.title("Iteration {}".format(i))
            plt.draw()
            plt.show()


test = TestSample()
test.test_SIS_simulations()
