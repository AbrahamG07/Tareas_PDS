import numpy as np
import matplotlib.pyplot as plt

def frec_variable(frecuencia):
    try:
        f = float(frecuencia)
    except ValueError:
        print("Frecuencia inválida.")
        return

    t = np.linspace(0, 1, 1000)
    x_t = np.sin(2 * np.pi * f * t)

    plt.plot(t, x_t)
    plt.title(f"Onda senoidal con f = {f} Hz")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.grid(True)
    plt.show()

