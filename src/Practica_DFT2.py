import numpy as np
import matplotlib.pyplot as plt
from src.utils.codigoDFT import mi_DFT

def graficas_DFT_con_ruido():
    fs = 256
    T = 6
    N = int(fs * T)
    ts = 1/fs
    f1 = 8
    f2 = 20

    n = np.arange(N)
    xn = np.sin(2*np.pi*f1*n*ts) + 0.5*np.sin(2*np.pi*f2*n*ts)
    ruido = 0.3 * np.sin(2*np.pi*50*n*ts)
    xn_ruido = xn + ruido

    delta_f = fs / N
    print(f"Resolución de frecuencia Δf = {delta_f:.2f} Hz")

    # Señales originales
    fig1 = plt.figure(figsize=(12,4))
    plt.subplot(1,2,1)
    plt.plot(n*ts, xn)
    plt.title("Señal original")
    plt.grid(True)

    plt.subplot(1,2,2)
    plt.plot(n*ts, xn_ruido)
    plt.title("Señal con ruido")
    plt.grid(True)

    # DFT de las seññales
    Xn = mi_DFT(xn)
    Xn_ruido = mi_DFT(xn_ruido)
    freqs = np.arange(N)*fs/N

    fig2 = plt.figure(figsize=(12,6))
    plt.subplot(2,1,1)
    plt.stem(freqs, np.abs(Xn))
    plt.title("Espectro señal original")
    plt.grid(True)

    plt.subplot(2,1,2)
    plt.stem(freqs, np.abs(Xn_ruido))
    plt.title("Espectro señal con ruido")
    plt.grid(True)

    # --- Mostrar todas las figuras al mismo tiempo ---
    plt.show()

