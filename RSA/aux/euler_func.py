def euler(n, p, q):
    """
    Calcula la función de Euler φ(n), que cuenta los números enteros positivos hasta n que son coprimos con n. Como en RSA N=p*q, podemos simplificar el cálculo de φ(n) como φ(p*q) = (p-1)*(q-1), ya que p y q son primos.

    Args:
        n (int): Número para el cual se calcula φ(n).
        p (int): Primer factor primo de n.
        q (int): Segundo factor primo de n.
    
    Returns:
        int: Valor de φ(n).
    """

    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        result = (p - 1) * (q - 1)
        
    return result