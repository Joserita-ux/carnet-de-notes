numbahhh = float(input("choisit ton nombre: "))

# 1. Partie entière
entiere_part = int(numbahhh)
dec_entier = bin(entiere_part)[2:]

# 2. Partie décimale (après la virgule)
partieaftervir = numbahhh - entiere_part
bits = []

for _ in range(8):  # Fait au maximum 8 tours
    if partieaftervir == 0:
        break  # S'arrête plus tôt si la conversion est terminée
    
    partieaftervir *= 2 #fait un max de 8 tour 
    bits.append(str(int(partieaftervir)))
    partieaftervir %= 1

print(f"En binaire : {dec_entier}.{''.join(bits)}")
