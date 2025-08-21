import numpy as np
def mi_DFT(x):
    N= len(x) # cantidad de muestras
    X = np.zeros(N, dtype=complex)#contenedores de frecuencia
    #fabricamos cada uno de las compnenrtes de la frecuencia
    for m in range(N):
        suma = 0.0
        for n in range(N):
            arg = (2*np.pi*m*n)/N
            suma = suma + x[n]*(np.cos(arg) - 1j*np.sin(arg) )

        X[m] = suma

    return X

def mi_IDFT(X):
    N= len(X) # cantidad de muestras
    x = np.zeros(N, dtype=complex)#contenedores de frecuencia
    #fabricamos cada uno de las compnenrtes de la frecuencia
    for n in range(N):
        suma = 0.0
        for m in range(N):
            arg = (2*np.pi*m*n)/N
            suma = suma + X[m]*(np.cos(arg) - 1j*np.sin(arg) )

        x[n] = suma

    return x/N
        
        
