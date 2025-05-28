from RSA.aux.euler_func import euler
from RSA.aux.prime import is_prime
from RSA.aux.generate_prim import generate_prime
import random
import math

class RSA():
    """
    Clase que representa el algoritmo RSA para cifrado y descifrado de mensajes.
    """

    def __init__(self):
        self.p = generate_prime()
        self.q = generate_prime()
        self.n = None
        self.e = None
        self.d = None
        self.phi = None

    def generate_keys(self):
        """
        Genera las claves pública y privada.
        """

        # Comprobar que p =! q, en caso contrario generar un nuevo q
        while self.p == self.q:
            self.q = generate_prime()

        # Calcular N
        self.n = self.p * self.q

        # Calcular φ(N)
        self.phi = euler(self.n, self.p, self.q)

        # Elegir el exponente público e
        self.e = random.randint(2, self.phi - 1)

        # Asegurarse de que e y phi(N) son coprimos
        while math.gcd(self.e, self.phi) != 1:
            self.e = random.randint(2, self.phi - 1)

        # Calcular el exponente privado d
        self.d = pow(self.e, -1, self.phi)

        # Devuelve las claves
        print("Claves generadas:")
        print(f"Clave pública: ({self.n}, {self.e})")
        print(f"Clave privada: ({self.n}, {self.d})")
        return (self.n, self.e), (self.n, self.d)



        
        
