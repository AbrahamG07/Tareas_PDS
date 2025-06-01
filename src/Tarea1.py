import numpy as np
import matplotlib.pyplot as plt

def triangular_wave(t, f):
    T = 1 / f
    mod = np.mod(t, T)
    return 4 * np.abs(mod / T - 0.5) - 1

f = 2  
t_start, t_end = -1, 5
t = np.linspace(t_start, t_end, 1000)  
Ts = 0.01  
n = np.arange(int((t_end - t_start)/Ts) + 1)
tn = t_start + n * Ts  

plt.figure(figsize=(12, 10))
plt.subplots_adjust(hspace=0.4)

x1_cont = np.sin(2 * np.pi * f * t)
x1_disc = np.sin(2 * np.pi * f * tn)

plt.subplot(4,1,1)
plt.plot(t, x1_cont, label='Señal continua', color='blue')
plt.stem(tn, x1_disc, linefmt='r-', markerfmt='ro', basefmt=" ", label='Señal muestreada')
plt.title('x₁(t) = sin(2π·f·t)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()

u = (t >= 0).astype(float)
u_disc = (tn >= 0).astype(float)
x2_cont = np.exp(-2 * t) * u
x2_disc = np.exp(-2 * tn) * u_disc

plt.subplot(4,1,2)
plt.plot(t, x2_cont, label='Señal continua', color='blue')
plt.stem(tn, x2_disc, linefmt='r-', markerfmt='ro', basefmt=" ", label='Señal muestreada')
plt.title('x₂(t) = e^(–2t)·u(t)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()

x3_cont = triangular_wave(t, f)
x3_disc = triangular_wave(tn, f)

plt.subplot(4,1,3)
plt.plot(t, x3_cont, label='Señal continua', color='blue')
plt.stem(tn, x3_disc, linefmt='r-', markerfmt='ro', basefmt=" ", label='Señal muestreada')
plt.title('x₃(t) = tri(t, f) - señal triangular periódica')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()

x4_cont = np.sign(np.sin(2 * np.pi * f * t))
x4_disc = np.sign(np.sin(2 * np.pi * f * tn))

plt.subplot(4,1,4)
plt.plot(t, x4_cont, label='Señal continua', color='blue')
plt.stem(tn, x4_disc, linefmt='r-', markerfmt='ro', basefmt=" ", label='Señal muestreada')
plt.title('x₄(t) = sq(t, f) - señal cuadrada periódica')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
