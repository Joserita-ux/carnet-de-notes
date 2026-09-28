nb10= int(input("ton nombre: "))
convertbin = bin(nb10)[2:]
print('binaire :',convertbin)
bin_inverse = "".join("1" if bit == "0" else "0" for bit in convertbin)
binnega = bin(int(bin_inverse, 2) + 1)[2:]
print("binaire negatif :", binnega)

          