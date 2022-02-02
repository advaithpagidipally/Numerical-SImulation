import random
import math
import matplotlib.pyplot as plt

def PI():
    Total_Number_Of_Particles = [i for i in range(0,100000)]
    Ratios = []
    Points_inside_circle = 0
    Points_inside_square = 0
    for i in range(0,100000):
        r1 = random.uniform(-1,1)
        r2 = random.uniform(-1,1)
        while math.sqrt(r1 * r1 + r2 * r2) > 1:
            r1 = random.uniform(-1, 1)
            r2 = random.uniform(-1, 1)
        Points_inside_circle = Points_inside_circle + 1
        if r1 <= (1/math.sqrt(2)) and r1 >= -1 * (1/math.sqrt(2)):
            if r2 <= (1/math.sqrt(2)) and r2 >= -1 * (1/math.sqrt(2)):
                Points_inside_square = Points_inside_square + 1
        Ratios.append(2 * (Points_inside_circle/max(1,Points_inside_square)))
    plt.plot(Total_Number_Of_Particles, Ratios)
    plt.xlabel('Number of points')
    plt.ylabel('PI value')
    plt.show()



if __name__ == "__main__":
    PI()