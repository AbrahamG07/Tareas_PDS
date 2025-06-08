# src/tarea_3.py

import numpy as np
import matplotlib.pyplot as plt

def sin_modificado(amplitud, frecuencia, fase):
    try:
        A = float(amplitud)
        f = float(frecuencia)
        phi = float(fase)
    except ValueError:
        print("Error: Asegúrate de ingresar valores numéricos válidos (amplitud, frecuencia, fase).")
        return

    t = np.linspace(0, 1, 1000)
    x_t = A * np.sin(2 * np.pi * f * t + phi)

    x_ref = np.sin(2 * np.pi * 1 * t)

    Ts = 0.01
    n = np.arange(0, 1, Ts)
    x_n = A * np.sin(2 * np.pi * f * n + phi)
    x_n_ref = np.sin(2 * np.pi * 1 * n)

    print(f"\n Tarea 3 - Señales Senoidales")
    print(f"🔹 Amplitud: {A}")
    print(f"🔹 Frecuencia: {f} Hz")
    print(f"🔹 Fase: {phi} rad")

  
    plt.figure(figsize=(10, 4))
    plt.plot(t, x_t, label='Señal modificada', color='blue')
    plt.plot(t, x_ref, '--', label='Señal de referencia (A=1, f=1Hz, ϕ=0)', color='gray')
    plt.title(f"Señal Continua: A={A}, f={f} Hz, ϕ={phi} rad")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Amplitud")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

  
    plt.figure(figsize=(10, 4))
    plt.stem(n, x_n, linefmt='b-', markerfmt='bo', basefmt=" ", label='Señal modificada')
    plt.stem(n, x_n_ref, linefmt='k--', markerfmt='ko', basefmt=" ", label='Referencia (A=1, f=1Hz, ϕ=0)')
    plt.title(f"Señal Discreta: A={A}, f={f} Hz, ϕ={phi} rad")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Amplitud")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
