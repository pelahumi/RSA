from Basic_RSA.classes.rsa import RSA

if __name__ == "__main__":
    # Creamos un objeto RSA
    rsa = RSA()

    # Este será el mensaje que vamos a cifrar
    message = 'capture the flag'
    print(f'Mensaje original: {message}')

    # Generamos las claves pública y privada
    public_key, private_key = rsa.generate_keys()
    print('Claves generadas:')
    print(f'Clave pública: {public_key}')
    print(f'Clave privada: {private_key}')

    # Ciframos el mensaje
    encrypted_message= rsa.encrypt(message)
    print(f'Mensaje cifrado: {encrypted_message}')

    # Desciframos el mensaje
    decrypted_message = rsa.decrypt(encrypted_message)
    print(f'Mensaje descifrado: {decrypted_message}')

   