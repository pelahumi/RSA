from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64


class AdvancedRSA():

    """
    Clase que representa el algoritmo RSA avanzado para cifrado y descifrado de mensajes.
    Esta clase utiliza la biblioteca PyCryptodome para manejar las claves RSA y el cifrado.
    Esta implementación permite generar claves RSA de un tamaño específico y realizar operaciones de cifrado y descifrado.
    """

    def __init__(self, key_size=2048):
        self.key_size = key_size  # Tamaño de la clave RSA
        self.key = None # Clave RSA generada
        self.public_key = None # Clave pública RSA
        self.private_key = None # Clave privada RSA



    def generate_keys(self):
        """
        Genera las claves pública y privada. 
        """

        # Generamos una clave RSA de 2048 bits
        self.key = RSA.generate(self.key_size)

        # Generamos las claves pública y privada
        self.public_key = self.key.publickey().export_key()
        self.private_key = self.key.export_key()

        return self.public_key, self.private_key
    


    def encrypt(self, message):
        """
        Cifra un mensaje con la clave pública.

        Args:
            message (bytes): Mensaje a cifrar en formato de bytes.
        Returns:
            bytes: Mensaje cifrado en formato de bytes.
        """

        # Importamos la clave pública
        public_key = RSA.import_key(self.public_key)

        # Creamos un objeto de cifrado con padding OAEP y la clave pública
        cipher = PKCS1_OAEP.new(public_key)

        # Ciframos el mensaje
        c = cipher.encrypt(message)

        # Codificamos el mensaje en base64
        c = base64.b64encode(c)

        return c
    

    def decrypt(self, c):
        """
        Descifra un mensaje con la clave privada.

        Args:
            c (bytes): Mensaje cifrado codificado en base64.
        Returns:
            bytes: Mensaje descifrado en formato de bytes.
        """

        # Decodificamos el mensaje cifrado de base64
        c = base64.b64decode(c)

        # Importamos la clave privada
        private_key = RSA.import_key(self.private_key)

        # Creamos un objeto de descifrado con padding OAEP y la clave privada
        cipher = PKCS1_OAEP.new(private_key)

        # Desciframos el mensaje
        m = cipher.decrypt(c)

        return m




    