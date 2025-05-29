
def launch_rsa():
    """
    Función para lanzar el sistema de cifrado RSA.
    Esta función permite al usuario elegir entre dos implementaciones de RSA:
    - RSA básico: Implementación simple de RSA.
    - RSA avanzado: Implementación avanzada utilizando la biblioteca PyCryptodome.
    """

    # Menú de opciones
    print("Bienvenido al sistema de cifrado RSA")
    print("1. RSA básico")
    print("2. RSA avanzado")
    choice = input("Seleccione una opción (1 o 2): ")

    if choice == '1':

        #### Basic RSA Implementation ####

        from RSA.Basic_RSA.classes.bas_rsa import RSA

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
    
    elif choice == '2':
        
        #### Advanced RSA Implementation ####

        from RSA.Advanced_RSA.adv_rsa import AdvancedRSA

        # Creamos un objeto RSA avanzado
        rsa = AdvancedRSA()

        # Este será el mensaje que vamos a cifrar
        message = b'capture the flag'
        print(f'Mensaje original: {message.decode()}')

        # Generamos las claves pública y privada
        public_key, private_key = rsa.generate_keys()
        print('Claves generadas:')
        print(f'Clave pública: {public_key.decode()}')
        print(f'Clave privada: {private_key.decode()}')

        # Ciframos el mensaje
        encrypted_message = rsa.encrypt(message)
        print(f'Mensaje cifrado: {encrypted_message.decode()}')

        # Desciframos el mensaje
        decrypted_message = rsa.decrypt(encrypted_message)
        print(f'Mensaje descifrado: {decrypted_message.decode()}')


    else:
        print("Opción no válida. Saliendo del programa.")
        exit()