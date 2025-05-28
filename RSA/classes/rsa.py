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
        self.p = generate_prime() # Genera un número primo aleatorio, p
        self.q = generate_prime() # Genera un número primo aleatorio, q
        self.n = None # Módulo y producto de p y q
        self.e = None # Exponente público
        self.d = None # Exponente privado
        self.phi = None # Función de Euler φ(N)

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
    
    def encrypt(self, m):
        """
        Cifra un mensaje usando la clave pública.

        Args:
            message (str): Mensaje a cifrar (texto plano).
        Returns:
            c (int): Mensaje cifrado.
        """

         # Convertir el mensaje a bytes
        m_int = int.from_bytes(m.encode('utf-8'), byteorder='big')

        # Comprobar que el mensaje es menor que N
        if m_int >= self.n:
            raise ValueError("El mensaje es demasiado grande para ser cifrado.")
        
        # Cifrar el mensaje usando la fórmula c = m^e mod N
        c = pow(m_int, self.e, self.n)

        return c
    
    def decrypt(self, c):
        """
        Descifra un mensaje usando la clave privada.

        Args:
            c (int): Mensaje cifrado.
        Returns:
            m (str): Mensaje descifrado (texto plano).
        """

        # Descifrar el mensaje usando la fórmula m = c^d mod N
        m_int = pow(c, self.d, self.n)

        # Convertir el mensaje de bytes a string
        m = m_int.to_bytes((m_int.bit_length() + 7) // 8, byteorder='big').decode('utf-8')

        return m





        
        
