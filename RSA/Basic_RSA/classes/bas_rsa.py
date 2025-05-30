from Basic_RSA.aux.generate_prim import generate_prime
import math

class BasicRSA():
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

        print(f"p: {self.p}, q: {self.q}")

        # Calcular N
        self.n = self.p * self.q

        # Calcular φ(N)
        self.phi = (self.p - 1) * (self.q - 1)

        # Elegir el exponente público e
        self.e = 65537  # Un valor común para e, debe ser coprimo con φ(N)
        if self.e >= self.phi:
            raise ValueError(f"El exponente público e {self.e} debe ser menor que φ(N) {self.phi}.")
        if math.gcd(self.e, self.phi) != 1:
            raise ValueError(f"El exponente público e {self.e} no es coprimo con φ(N) {self.phi}.")

        # Calcular el exponente privado d
        self.d = pow(self.e, -1, self.phi)

        # Devuelve las claves
        return (self.n, self.e), (self.n, self.d)
    
    def encrypt(self, m):
        """
        Cifra un mensaje caracter a caracter usando la clave pública.

        Args:
            message (str): Mensaje a cifrar (texto plano).
        Returns:
            c (int): Mensaje cifrado.
        """

        cipher = []

        # Convertir el mensaje a bytes y luego a un entero
        for char in m:
            m_int = ord(char)
            if m_int >= self.n:
                raise ValueError(f"El carácter '{char}' es demasiado grande para ser cifrado.")
            c = pow(m_int, self.e, self.n)
            cipher.append(c)

        return cipher
    
    def decrypt(self, c):
        """
        Descifra un mensaje usando la clave privada.

        Args:
            c (int): Mensaje cifrado.
        Returns:
            m (str): Mensaje descifrado (texto plano).
        """

        m = ''

        # Descifrar cada carácter del mensaje cifrado
        for c_int in c:
            m_int = pow(c_int, self.d, self.n)
            m += chr(m_int)
        return m





        
        
