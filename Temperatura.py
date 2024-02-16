# Ejercicio No.2 programa para convertir una cantidad grados C a su equivalente a K y  F

# input

C= input("Digite la cantidad de grados C a convertir:")
C= int(C)

# Processing

F= (C * (9/5)) + 32
K= C + 273.15

#Output

print ("Grados Fahrenheit: " + str(F))
print ("Grados Kelvin: " + str(K))