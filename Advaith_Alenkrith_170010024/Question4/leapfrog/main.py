import matplotlib.pyplot as plt
def Harmonic_Oscillator(mass, k, initial_pos,initial_vel, initial_time, dt, max_time, w):
   position_time = []
   velocity_time = []
   position = []
   velocity = []
   Kinetic_Energy = []
   Potential_ENergy = []
   Total_Energy = []
   while initial_time < max_time:
       initial_time = initial_time + dt
       position_time.append(initial_time)
       initial_pos = initial_pos + initial_vel * dt
       position.append(initial_pos)
       velocity_time.append(initial_time - (dt/2))
       initial_vel = initial_vel - w * w * initial_pos * dt
       velocity.append(initial_vel)
       Kinetic_Energy.append(0.5 * initial_vel * initial_vel)
       Potential_ENergy.append(0.5 * initial_pos * initial_pos)
       Total_Energy.append(0.5 * initial_vel * initial_vel + 0.5 * initial_pos * initial_pos)
   plt.plot(position_time, position,label = 'position')
   plt.plot(velocity_time, velocity,label = "velocity")
   plt.plot(position_time, Kinetic_Energy, label = "K.E")
   plt.plot(position_time, Potential_ENergy, label = "P.E")
   plt.plot(position_time, Total_Energy, label = "T.E")
   plt.xlabel('x - axis')
   plt.ylabel('y - axis')
   plt.show()

if __name__ == "__main__":
   Harmonic_Oscillator(1,1,0,1,0,0.01,100,1)