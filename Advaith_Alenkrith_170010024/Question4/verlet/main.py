import matplotlib.pyplot as plt
def Harmonic_Oscillator(mass, k, initial_pos1,initial_pos2, initial_vel, initial_time, dt, max_time, w):
   time = []
   position = []
   velocity = []
   Kinetic_Energy = []
   Potential_ENergy = []
   Total_Energy = []
   initial_pos2 = initial_pos1 + initial_vel * dt
   time.append(initial_time)
   position.append(initial_pos2)
   velocity.append(initial_vel)
   Kinetic_Energy.append(0.5 * initial_vel * initial_vel)
   Potential_ENergy.append(0.5 * initial_pos2 * initial_pos2)
   Total_Energy.append(0.5 * initial_vel * initial_vel + 0.5 * initial_pos2 * initial_pos2)
   while initial_time < max_time:
       initial_time = initial_time + dt
       time.append(initial_time)
       temp = initial_pos2
       initial_pos2 = 2 * initial_pos2 - initial_pos1 - (initial_pos2 * k * dt * dt / mass)
       position.append(initial_pos2)
       initial_vel = (0.5 * (initial_pos2 - initial_pos1)) / dt
       velocity.append(initial_vel)
       Kinetic_Energy.append(0.5 * initial_vel * initial_vel)
       Potential_ENergy.append(0.5 * initial_pos2 * initial_pos2)
       Total_Energy.append(0.5 * initial_vel * initial_vel + 0.5 * initial_pos2 * initial_pos2)
       initial_pos1 = temp
   plt.plot(time, position,label = 'position')
   plt.plot(time, velocity,label = "velocity")
   plt.plot(time, Kinetic_Energy, label = "K.E")
   plt.plot(time, Potential_ENergy, label = "P.E")
   plt.plot(time, Total_Energy, label = "T.E")
   plt.xlabel('x - axis')
   plt.ylabel('y - axis')
   plt.show()

if __name__ == "__main__":
   Harmonic_Oscillator(1,1,0,0.01,1,0,0.01,100,1)