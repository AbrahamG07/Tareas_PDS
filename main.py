import sys
from src import tarea1, tarea2, tarea3, tarea4, Practica_DFT, Practica_DFT2

def main():
    if len(sys.argv) < 2:
        print("Debes indicar la tarea a ejecutar.")
        return

    tarea = sys.argv[1].lower()

    if tarea == "tarea1":
        tarea1.grafica_senales()

    elif tarea == "tarea2":
        if len(sys.argv) < 3:
            print("Por favor da una frecuencia. Ejemplo: python main.py tarea2 5")
            return
        frecuencia = sys.argv[2]
        tarea2.frec_variable(frecuencia)

    elif tarea == "tarea3":
        if len(sys.argv) < 5:
            print("Por favor indica amplitud, frecuencia y fase. Ejemplo: python main.py tarea3 1 1 0")
            return
        amplitud = float(sys.argv[2])
        frecuencia = float(sys.argv[3])
        fase = float(sys.argv[4])
        tarea3.sin_modificado(amplitud, frecuencia, fase)

    elif tarea == "tarea4":
        if len(sys.argv) < 3:
            print("Debes proporcionar el número de bits. Ejemplo: python main.py tarea4 8")
            return
        num_bits = sys.argv[2]
        tarea4.resolver_tarea_4(num_bits)
    
    elif tarea == "practica_dft":
        Practica_DFT.graficas_DFT()
        
    elif tarea == "practica_dft2":
        Practica_DFT2.graficas_DFT_con_ruido()

    else:
        print("Tarea no reconocida. Usa: tarea1, tarea2, tarea3, tarea4, practica_dft o ptractica_dft2")

if __name__ == "__main__":
    main()

