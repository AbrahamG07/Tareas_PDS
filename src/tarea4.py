import numpy as np
import matplotlib.pyplot as plt

def resolver_tarea_4(num_bits):
    """
    Ejecuta la simulación de un DAC para un número específico de bits.
    """
    VFS = 5.0  # Voltaje de escala completa (5V)
    N = int(num_bits)

    niveles = 2 ** N
    paso = VFS / (niveles - 1)
    resolucion = (paso / VFS) * 100

    print(f"\n Tarea 4 - DAC de {N} bits")
    print(f"🔹 Niveles posibles: {niveles}")
    print(f"🔹 Tamaño del paso: {paso:.6f} V")
    print(f"🔹 Resolución porcentual: {resolucion:.4f} %")

    # Crear vector de entrada digital y salida analógica
    entrada_digital = np.arange(niveles)
    salida_analogica = entrada_digital * paso

    # Graficar la salida analógica del DAC
    plt.stem(entrada_digital, salida_analogica, basefmt=" ", )
    plt.title(f"Salida del DAC para N = {N} bits")
    plt.xlabel("Entrada digital")
    plt.ylabel("Voltaje analógico (V)")
    plt.grid(True)
    plt.show()

