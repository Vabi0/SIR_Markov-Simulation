import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 1000
I0 = 10
R0 = 0
S0 = N - I0 - R0

beta = 0.3
gamma = 0.1
days = 100

# Initialize arrays
S = np.zeros(days)
I = np.zeros(days)
R = np.zeros(days)
new_infections_daily = np.zeros(days)  # array for daily new infections

S[0] = S0
I[0] = I0
R[0] = R0

# Simulation
for t in range(1, days):
    new_infections = beta * S[t-1] * I[t-1] / N
    new_recoveries = gamma * I[t-1]
    
    S[t] = S[t-1] - new_infections
    I[t] = I[t-1] + new_infections - new_recoveries
    R[t] = R[t-1] + new_recoveries
    
    new_infections_daily[t] = new_infections  # store new infections

# Find peak infection
peak_day = np.argmax(I)
peak_infections = I[peak_day]
print(f"Peak infections: {int(peak_infections)} on day {peak_day}")

# Plot total populations
plt.figure(figsize=(10,6))
plt.plot(S, label='Susceptible', color='blue')
plt.plot(I, label='Infected', color='red')
plt.plot(R, label='Recovered', color='green')
plt.scatter(peak_day, peak_infections, color='red')  # mark peak
plt.text(peak_day, peak_infections+10, f'Peak Day {peak_day}', ha='center')
plt.xlabel('Days')
plt.ylabel('Population')
plt.title('SIR Model Disease Spread Simulation')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('SIR_simulation_plot.png')

# Plot daily new infections
plt.figure(figsize=(10,6))
plt.plot(new_infections_daily, label='Daily New Infections', color='orange')
plt.xlabel('Days')
plt.ylabel('New Infections')
plt.title('Daily New Infections')
plt.grid(True)
plt.show()
plt.savefig('SIR_daily_infections.png')