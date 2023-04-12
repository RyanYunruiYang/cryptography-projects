import random
from Crypto.Util.number import getPrime

def rabinFunction(m: int, public_key: int):
    return (m*m % public_key)

class Generator:
    def __init__(self, seed, public_key):
        self.x = seed
        self.public_key = public_key
        self.occ = [0,0]

        self.seed = seed
        self.compromised_index = -1
    
    def next_bit(self): 
        self.x = (self.x**2 % self.public_key)
        
        self.occ[self.x % 2] += 1

        # print(self.x % 2)
        return (self.x % 2)


def main():
    k = 80
    p,q = getPrime(k), getPrime(k)
    public_key = p*q

    print(f"n = {p} * {q} = {public_key}")

    x = random.randint(0,public_key)
    print(f"seed: {x}")

    gen = Generator(x, public_key)

    for i in range(1000):
        print(gen.next_bit(), end=' ')
    
    print(gen.occ)






if __name__ == "__main__":
    main()