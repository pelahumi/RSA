import random
from .test_prim import is_prime

def generate_prime():
    """
    Genera un número primo aleatorio entre 1000 y 5000.
    
    Returns:
        int: Un número primo aleatorio.
    """
    while True:
        p = random.randint(1000, 5000)
        if is_prime(p):
            return p
        