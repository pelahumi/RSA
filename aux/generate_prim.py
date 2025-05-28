import random
from test_prim import is_prime

def generate_prime():
    """
    Genera un número primo aleatorio entre 100 y 500.
    
    Returns:
        int: Un número primo aleatorio.
    """
    while True:
        p = random.randint(100, 500)
        if is_prime(p):
            return p
        