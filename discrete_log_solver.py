import sympy.ntheory as nt
import math, random, time
# from Crypto.Util.number import getPrime

#Same goal as https://www.dcode.fr/modular-exponentiation but different alg (probably)
def power(x, g, p):
    dp = []
    cur_val = g
    k = 1
    while(k <= x):
        dp.append(cur_val)
        cur_val = (cur_val*cur_val) % p
        k = 2*k
    # print(dp)
    
    final_val = 1
    i = 0
    while(x > 0):
        if(x%2 == 1):
            final_val = (final_val * dp[i]) % p
        i+=1
        x = x//2
    # print(f"final_val: {final_val}")

    return final_val

def decode(A, g, p):
    #We're solving g^x = a (mod p)
    powers = {}
    b_power = {}

    # print(f"A: {A}, g: {g}, p: {p}")

    found = False
    i = 0
    while(not found):
        i+=1
        new_index = random.randint(1,p-1)
        # print(f"{i}th sample: x={new_index}")

        new_pow = power(new_index, g, p)
        b_pow = (new_pow * A) % p

        powers[new_pow] = new_index
        b_power[b_pow] = new_index

        if(new_pow in b_power):
            found = True
            secret_key = new_index - b_power[new_pow]
        
        if(b_pow in powers):
            found = True
            secret_key = powers[b_pow] - new_index
        
        if(found):
            # print(f"On the {i}th sample:")
            print(f"secret key: {secret_key}")
        
    
    # print(powers)
    # print(b_power)
    return i


def benchmarking():
    sim_length = 20

    #p,g,A = 1009,439,164
    # p,g,A = 15551, 7, 164
    # p,g,A = 5915587277, 2, 164  ###59348.6
    p,g,A = 228034214138645326956319840591508314961, 3, 164 ###


    sum_total = 0
    start_time = time.time()
    for _ in range (sim_length):
        sum_total += decode(A, g, p)

    print(f"average rounds: {sum_total/sim_length}")
    print(f"average time: {(time.time()-start_time)/sim_length}")


def main():
    #Public Vairables: 
    p = 1009
    g = 439 #sqrt(2). The order of g mod p is 1008=p-1

    #Private Key
    secret_key = 200

    #Published value (164 here)
    public_key = power(secret_key, g,  p) 

    print(f"public {g}^a (mod {p}) value: {public_key}")

    # mtma_break = decode(public_key, g, p)
    benchmarking()





if __name__ == "__main__":
    main()