# Importa librerias
import sys

# Lee el largo del script, para asegurarse de ingresar la cantidad de argumentos correctos
largo = len(sys.argv)

# Solo si la cantidad de argumentos ingresados es correcta se realizan los calculos
if largo > 3:
    numero1 = int(sys.argv[1]) # lee el primer argumento del script : primer numero
    numero2 = int(sys.argv[2]) # lee el segundo argumento del script : segundo numero
    numero3 = int(sys.argv[3]) # lee el tercer argumento del script : tercer numero
        
    # Compara numero1 con numero2
    if numero1 > numero2:
        mayor = numero1
    else:
        mayor = numero2
    
    # Compara mayor con numero3
    if mayor > numero3:
        print(mayor)   
    else:
        mayor = numero3
        print(mayor)

else:
    # Mensaje al usuario
    print("Hay argumentos que faltan. Por favor intente de nuevo.")

# Fin del programa