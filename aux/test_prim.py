def is_prime(p):
    """
    Comprueba si un número p es primo.

    Args:
        p (int): Número a comprobar.
    Returns:
        bool: True si p es primo, False en caso contrario.
    """
    
    # Comprobamos si p es menor que 2
    if p < 2:
        return False
    
    # Comprobamos si p es 2
    elif p == 2:
        return True
    
    else:
        # Bucle para comprobar si p es primo, saltando los pares hasta la raíz cuadrada de p
        for i in range(3, int(p**0.5) + 1, 2):
            if p % i == 0:
                return False
        return True

