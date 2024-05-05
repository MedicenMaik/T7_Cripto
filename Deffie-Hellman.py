import random
from sympy import isprime

def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

def find_primitive_roots(q):
    primitive_roots = []
    for i in range(2, q):
        if isprime(i) and pow(i, (q-1)//2, q) != 1:
            primitive_roots.append(i)
            if len(primitive_roots) == 10:
                break
    return primitive_roots

def generate_keys(q, alpha):
    private_key = random.randint(2, q-1)
    public_key = mod_exp(alpha, private_key, q)
    return public_key, private_key


q = 65537
primitives = find_primitive_roots(q)
print("Raíces primitivas encontradas:")
for i, root in enumerate(primitives, 1):
    print(f"Raiz {i} => ", root)


alpha = random.choice(primitives)
print("\nRaíz primitiva seleccionada:", alpha)


ana_public_key, ana_private_key = generate_keys(q, alpha)
print("Clave pública de Ana:", ana_public_key)
print("Clave privada de Ana:", ana_private_key)


bob_public_key, bob_private_key = generate_keys(q, alpha)
print("Clave pública de Bob:", bob_public_key)
print("Clave privada de Bob:", bob_private_key)


shared_secret_ana = mod_exp(bob_public_key, ana_private_key, q)
shared_secret_bob = mod_exp(ana_public_key, bob_private_key, q)

print("Clave compartida calculada por Ana:", shared_secret_ana)
print("Clave compartida calculada por Bob:", shared_secret_bob)
