#sumar 2 numeros y mostrar el resultado
#paarametro es la variable que se defune cuando se crea la funcion.

def getsum(num1, num2):
        return num1 + num2

def showResult(message, result):
     return f"{message} {result}"

print("Dime un numero")
num1 = float(input())
print("Dime otro numero")
num2 = float(input())

#El argumento es el valor que se envia a la funcion cuando se llama.
sum = getsum(num1, num2)
print(showResult("El resultado de la suma es:", sum))