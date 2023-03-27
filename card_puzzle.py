s = "10101100100110011001101101100101101101001010100101011010010101101001001101101"

s = s[::-1]
print(s)

print(s[0])
print(s[1])

for i in range(len(s)):
    # print(s[i])
    x = int(s[i])
    if(x==1):
        print(".",end='')
    else:
        print("-",end='')