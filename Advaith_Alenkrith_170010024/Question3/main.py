import math
import random
import numpy
import copy
import matplotlib.pyplot as plt

def Energy(lattice_values):
    energy = 0
    modified_lattice = []
    row = []
    for i in range(0,12):
        row.append(0)
    for i in range(0,12):
        c = copy.deepcopy(row)
        modified_lattice.append(c)
    for i in range(1,11):
        for j in range(1,11):
            temp = lattice_values[i - 1][j - 1]
            modified_lattice[i][j] = temp
    for i in range(1,11):
        modified_lattice[0][i] = modified_lattice[10][i]
    for i in range(1,11):
        modified_lattice[11][i] = modified_lattice[1][i]
    for i in range(1,11):
        modified_lattice[i][0] = modified_lattice[i][10]
    for i in range(1,11):
        modified_lattice[i][11] = modified_lattice[i][1]
    for i in range(1,11):
        for j in range(1,11):
            energy = energy + 0.5 * (-1 * modified_lattice[i][j] * modified_lattice[i-1][j]) + 0.5 * (-1 * modified_lattice[i][j] * modified_lattice[i+1][j]) + 0.5 * (-1 * modified_lattice[i][j] * modified_lattice[i][j-1]) + 0.5 * (-1 * modified_lattice[i][j] * modified_lattice[i][j+1])
    return energy
def Magnetism():
    Temperatures = [1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4]
    m_values = []
    for i in Temperatures:
        print("Temp - ",i)
        avg_mu = 0
        lattice_values = []
        row = []
        for a in range(0, 10):
            row.append(1)
        for a in range(0, 10):
            c = copy.deepcopy(row)
            lattice_values.append(c)
        U = Energy(lattice_values)
        for j in range(0,100000):
            for k in range(0,10):
                for l in range(0,10):
                    U0 = U
                    r1 = random.random()
                    r2 = random.random()
                    x = int(r1 * 10)
                    y = int(r2 * 10)
                    lattice_values[x][y] = -1 * lattice_values[x][y]
                    Un = Energy(lattice_values)
                    diff = Un - U0
                    p = math.exp((-1 * diff) / (1*i))
                    p = min(1,p)
                    r3 = random.random()
                    if r3 <= p:
                        U = Un
                    else:
                        U = U0
                        lattice_values[x][y] = -1 * lattice_values[x][y]
            mu = 0
            for k in range(0,10):
                for l in range(0,10):
                    mu = mu + lattice_values[k][l]
            mu = mu/100
            avg_mu = avg_mu + mu
        m_values.append(avg_mu/100000)
    plt.plot(Temperatures, m_values)
    plt.xlabel('Temperatures')
    plt.ylabel('Magnetic Moments')
    plt.show()


if __name__ == "__main__":
    Magnetism()