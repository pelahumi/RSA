import numpy as np
from qiskit import QuantumCircuit

def qft(n):
    """
    Implementación de la Transformada de Fourier Cuántica (QFT) en un circuito cuántico de n qubits.

    Args:
        n (int): Número de qubits en el circuito cuántico.
    Returns:
        qc (QuantumCircuit): Circuito cuántico que implementa la QFT.
    """
    # Creamos el circuito cuántico con n qubits
    qc = QuantumCircuit(n) 

    # Aplicamos un bucle para recorrer los qubits en orden invers
    for i in range(n-1, -1, -1):
        # Aplicamos la puerta Hadamard a cada qubit
        qc.h(i)

        # Aplicamos otro bucle para tener en cuenta los qubits que están por encima del qubit actual
        for j in range(i-1, -1, -1):
            # Aplicamos la puerta CP 
            angle = np.pi / 2**(i - j)
            qc.cp(angle, j, i)

        
    
    for i in range(n // 2):
        # Aplicamos la compuerta SWAP para intercambiar los qubits
        qc.swap(i, n - i - 1)
    
    # Hacemos que sea una puerta cuántica
    gate = qc.to_gate()
    gate.name = "QFT"

    return gate