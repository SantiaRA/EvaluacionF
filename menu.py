from individual import individuales
from multiple import multiples
from representation import ascii

def menu():
   print("Las opciones son: \n 1: representacion caracter individual \n 2: representacion palabra de caracteres \n 3: representacion ASCII");
   opcion = int(input("Elige una opcion: "));
   if (opcion == 1):
     caracter = str(input("Ingresa tu caracter: "))
     resultado = caracter_a_bits(caracter);
     return resultado;
   elif (opcion == 2):
     cadena = str(input("Ingresa tu cadena de caracteres: "));
     resultado = palabra_a_bits(cadena);
     return resultado;
   elif (opcion == 3):
     byte = int(input("Ingrese el byte: "));
     resultado = byte_a_ascii(byte);
     return resultado
   else:
     print("Opcion incorrecta");

