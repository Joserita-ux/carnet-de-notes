'ce programme sert a convertir un nombre decimal a du binaire puis de l"hexadecimale'

nombre = int(input("choisis ton nombre decimal:"))
resultat_binaire = bin(nombre) 
print("binaire :", resultat_binaire)
resultat_hexa = hex(nombre)
print("hexadecimale:", resultat_hexa)
print("decimale : ", nombre)
