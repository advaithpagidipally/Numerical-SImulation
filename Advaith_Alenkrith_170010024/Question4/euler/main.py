import matplotlib.pyplot as plt
def Harmonic_Oscillator(mass, k, initial_pos, initial_vel, initial_time, dt, max_time, w):
   time = []
   position = []
   velocity = []
   Kinetic_Energy = []
   Potential_ENergy = []
   Total_Energy = []
   time.append(initial_time)
   position.append(initial_pos)
   velocity.append(initial_vel)
   Kinetic_Energy.append(0.5 * initial_vel * initial_vel)
   Potential_ENergy.append(0.5 * initial_pos * initial_pos)
   Total_Energy.append(0.5 * initial_vel * initial_vel + 0.5 * initial_pos * initial_pos)
   while initial_time < max_time:
       temp = initial_pos
       initial_pos = initial_pos + initial_vel * dt
       initial_vel = initial_vel - ((w * w) * temp * dt)
       initial_time = initial_time + dt
       time.append(initial_time)
       position.append(initial_pos)
       velocity.append(initial_vel)
       Kinetic_Energy.append(0.5 * initial_vel * initial_vel)
       Potential_ENergy.append(0.5 * initial_pos * initial_pos)
       Total_Energy.append(0.5 * initial_vel * initial_vel + 0.5 * initial_pos * initial_pos)
   plt.plot(time, position,label = 'position')
   plt.plot(time, velocity,label = "velocity")
   plt.plot(time, Kinetic_Energy, label = "K.E")
   plt.plot(time, Potential_ENergy, label = "P.E")
   plt.plot(time, Total_Energy, label = "T.E")
   plt.xlabel('x - axis')
   plt.ylabel('y - axis')
   plt.show()

if __name__ == "__main__":
   Harmonic_Oscillator(1,1,0,1,0,0.01,100,1)