import gmpy2

#Anger = M
M = 74416097491057521514388961432586142697403691516696112331121897342736517429078

#Envy = d
d = 60593057491154512226701032657065488268296024400159469662277171905109178746973
e = 65537

kfi = d*e-1
#2^(127) < p,q < 2^(128)
#2^(254) < (p-1)*(q-1) < 2^(256)
lower = int(kfi/(1<<256))
upper = int(kfi/(1<<254))+1000

for k in range(lower, upper):
	if(kfi % k == 0):
		print(f"k: {k}")
		fi = kfi/k

		# if()

		print(int(fi))




		# d0 = gmpy2.invert(e,int(fi))
		# print(d0)
		# if(d == d0):
		# 	print(fi)
		# 	not_found = False