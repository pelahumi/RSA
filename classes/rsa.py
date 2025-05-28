from RSA.aux.euler_func import euler
from RSA.aux.prime import is_prime
import random

class RSA():
    """
    Clase que representa el algoritmo RSA para cifrado y descifrado de mensajes.
    """

    def __init__(self):
        self.p = None
        self.q = None
        self.n = None
        self.e = None
        self.d = None
        self.phi = None

    def generate_keys(self):
        """
        Genera las claves pública y privada.
        """

        # Generamos los primos p y q
        p = random.randint(100, 500)
