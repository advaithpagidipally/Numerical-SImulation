import random
import math
import matplotlib.pyplot as plt

def S_1():
    Total_Number_Of_Particles = 100000
    Random_Numbers = []
    Values = []
    frequencies = []
    X = []
    initial = 0
    rows = 1
    columns = 2
    fig = plt.figure(figsize=(20,20))
    for i in range(0, Total_Number_Of_Particles):
        got = 0
        while got == 0:
            r1 = random.random()
            rz = math.exp(-1 * (r1 - 0.5) * (r1 - 0.5) / 0.05)
            r2 = random.random()
            if rz > r2:
                got = 1
        Random_Numbers.append(r1)
    for i in range(0,100):
        initial = initial + 0.01
        Values.append([initial, initial + 0.01])
    for i in range(0,100):
        frequencies.append(0)
    for i in range(0, Total_Number_Of_Particles):
        for j in range(0,100):
            if Random_Numbers[i] >= Values[j][0] and Random_Numbers[i] < Values[j][1]:
                frequencies[j] = frequencies[j] + 1
    for i in range(0,100):
        frequencies[i] = frequencies[i]/100000
    for i in Values:
        X.append(str(i[0]))
    fig.add_subplot(rows, columns, 1)
    plt.plot(X, frequencies)
    plt.xlabel('Values')
    plt.ylabel('Probability Distribution')
    fig.add_subplot(rows, columns, 2)
    plt.hist(Random_Numbers, bins = 100)
    plt.xlabel('Numbers')
    plt.ylabel('Frequencies')
    plt.show()

if __name__ == "__main__":
    S_1()