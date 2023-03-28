from Crypto.Util.number import getPrime, inverse, bytes_to_long
from string import ascii_letters, digits
from random import choice

m = "".join(choice(ascii_letters + digits) for _ in range(16))
m_long = bytes_to_long(m.encode())
p = getPrime(128)
q = getPrime(128)
N = p * q
e = 65537
d = inverse(e, (p - 1) * (q - 1))

M = pow(bytes_to_long(m.encode()), e, N)

de_neg1 = d*e - 1

print(f"{m = }")
print(f"{m_long = }")
print(f"{p = }")
print(f"{q = }")
print(f"{N = }")
print(f"{e = }")
print(f"{d = }")
print(f"{M = }")
print(f"{de_neg1 = }")