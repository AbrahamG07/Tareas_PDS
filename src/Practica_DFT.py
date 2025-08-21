import numpy as np
from src.utils.codigoDFT import mi_DFT
import matplotlib.pyplot as plt

def graficas_DFT():
    fm = 0.5 
    fc = 8 
    m_mod = 0.5  

    
    t = np.linspace(0, 0.001, 500)
    xt = (1 + m_mod * np.cos(2 * np.pi * fm * t)) * np.sin(2 * np.pi * fc * t)

    
    fs = 1000
    n = np.arange(20)
    xn = (1 + m_mod * np.cos(2 * np.pi * fm * n / fs)) * np.sin(2 * np.pi * fc * n / fs)
    xn = np.ravel(xn)

    
    plt.figure(figsize=(12,4))

    # Señal continua
    plt.subplot(1,2,1)
    plt.plot(t, xt, 'm')
    plt.title("Señal continua")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.grid(True)

    # Señal discreta
    plt.subplot(1,2,2)
    plt.stem(n/fs, xn)
    plt.title("Señal discreta")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.grid(True)

    plt.tight_layout()
    plt.show()

    # Obtención de la transformada discreta de Fourier
    xm = mi_DFT(xn)

    tol = 1e-14
    xm.real[np.abs(xm.real) < tol] = 0
    xm.imag[np.abs(xm.imag) < tol] = 0

    N = len(n)
    m_idx = np.arange(N)
    fan = m_idx * fs / N

    plt.figure(figsize=(10,6))

    plt.subplot(2,2,1)
    plt.stem(fan, xm.real)
    plt.grid()
    plt.title('Parte real')

    plt.subplot(2,2,2)
    plt.stem(fan, xm.imag)
    plt.grid()
    plt.title('Parte imaginaria')

    plt.subplot(2,2,3)
    plt.stem(fan, np.abs(xm))
    plt.grid()
    plt.title('Magnitud')

    plt.subplot(2,2,4)
    plt.stem(fan, np.angle(xm, deg=True))
    plt.grid()
    plt.title('Ángulo de fase')

    plt.tight_layout()
    plt.show()

