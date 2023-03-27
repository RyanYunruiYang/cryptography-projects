import sympy.ntheory as nt
import math 


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

def decode(a, g, p):
    #We're solving g^x = a (mod p)

    appeared = [i for i in range(p)] #tracks if value has appeared

    random_attacks = [i for i in range(1,p)]

    



    return 


def main():
    #Public Vairables: 
    p = 1009
    g = 439 #sqrt(2). The order of g mod p is 1008=p-1

    #Private Information
    secret_key = 200

    #Published value
    public_key = power(secret_key, g,  p)

    print(f"public {g}^a (mod {p}) value: {public_key}")

    mtma_break = decode(public_key, g, p)






if __name__ == "__main__":
    main()